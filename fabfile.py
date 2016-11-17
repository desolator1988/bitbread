# -*- coding: utf-8 -*-

import os
import getpass

from fabric.api import (
    env,
    execute,
    task,
    hosts,
    settings,
    sudo,
    local,
    parallel,
)

from fabric.contrib.files import exists
from fabric.colors import (
    green,
)


PYPI_ADDR = 'http://mirrors.aliyun.com/pypi/simple/'
PYPI_ADDR = 'http://pypi.douban.com/simple/'
# PYPI_ADDR = None
FIX_PIP_VERSION = '7.1.0'

# fix env settings
env.use_ssh_config = True
env.keepalive = 60

env.deploying_commit = local('git rev-parse HEAD', capture=True)


DEPLOYMENT_PARAMS = {
    'repo': 'bitbread',
    'remote_user': 'www-data',
    'local_dir': os.path.dirname(os.path.realpath(__file__)),
    'remote_dir': '/srv/bitbread',
    'remote_exclude': 'rsync_exclude.txt',
    'requirements': 'pip-req.txt',
    'require_refresh': True,
    'virtualenv': '/srv/virtualenvs/bitbread',
}


WEB_DEPLOYMENT_PARAMS = DEPLOYMENT_PARAMS.copy()
WEB_DEPLOYMENT_PARAMS['services'] = ['web']


@task
@hosts(['106.14.31.54'])
def p_deploy_web():
    execute(deploy_web)


@task
def deploy_web():
    execute(python_deploy, **WEB_DEPLOYMENT_PARAMS)


def restart_service(service):
    with settings(warn_only=True):
        status = sudo('supervisorctl status {}'.format(service))
        if 'STOPPED' in status:
            info(
                '{} is restarted, because it was stopped for '
                'some reason on {}'.format(service, env.host_string)
            )
            return
        sudo('supervisorctl restart {}'.format(service))


def info(msg):
    print(green(msg))


def python_deploy(repo, local_dir, remote_dir, virtualenv,
                  services, remote_user, remote_exclude,
                  require_refresh=True, requirements=None):

    _common_rsync(local_dir, remote_dir, remote_user, remote_exclude)

    # make sure virtualenv exists
    if not exists(virtualenv):
        sudo('virtualenv {}'.format(virtualenv))
        if PYPI_ADDR:
            sudo('{0}/bin/pip install -i {1} -q -U distribute pip'.format(
                virtualenv, PYPI_ADDR))
        else:
            sudo('{0}/bin/pip install -q -U distribute pip'.format(
                virtualenv))

    # clean up build left overs
    sudo('rm -rf {0}/build'.format(virtualenv))

    if requirements:
        # sudo('{0}/bin/pip install -i {1} pip=={2}'.
        #      format(virtualenv, PYPI_ADDR, FIX_PIP_VERSION))
        #
        if PYPI_ADDR:
            sudo('{0}/bin/pip install -i {1} -r {2} --trusted-host pypi.douban.com'.
                 format(virtualenv, PYPI_ADDR, os.path.join(remote_dir, requirements)))
        else:
            sudo('{0}/bin/pip install -r {1}'.
                 format(virtualenv, os.path.join(remote_dir, requirements)))

    if require_refresh:
        python_refresh(remote_dir, virtualenv, services, remote_user)


def _common_rsync(local_dir, remote_dir, remote_user, remote_exclude):
    sudo('mkdir -p {}'.format(remote_dir))
    sudo("find . -name '*.pyc' -delete")
    sudo('chown {0} -R {1}'.format(env.user, remote_dir))
    commit_indicator = '.commit'
    with open(commit_indicator, 'w') as f:
        f.write(env.deploying_commit)
    local('rsync -azq --progress --force --delete --delay-updates '
          '--exclude-from={0} {1}/ {3}:{2}/ '
          '--include {4}'.format(
              os.path.join(local_dir, remote_exclude),
              local_dir,
              remote_dir,
              env.host_string,
              commit_indicator
          ))
    sudo('chown {0} -R {1}'.format(remote_user, remote_dir))


def python_refresh(remote_dir, virtualenv, services, remote_user):

    def _python_refresh(service):
        sudo('supervisorctl restart {}'.format(service))

    with settings(warn_only=True):
        for service in services:
            _python_refresh(service)
