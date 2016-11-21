# coding: utf8

from flask import (
    Blueprint,
    redirect,
    url_for,
    request,
    session,
)
from flask.ext.mako import render_template
from common.models.web.home import TestBitbread

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/index')
@index_blueprint.route('/')
def index_view():
    test_bitbread = TestBitbread.objects.first()
    return render_template('/index.mako', title='Welcome')


@index_blueprint.route('/home')
def home_view():
    return render_template('/base.mako', title='Home')
