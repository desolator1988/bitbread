<html>
  <head>
    <title>${title if title else 'Hi'} - 朋友</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">
    <link rel="stylesheet" href="/static/css/welcome.css">
</head>
<body>
<div id="wrapper">
  <div id="info">
    <div id="info-content">
      <h1>
          <a style="text-decoration:none; color: white" href="${url_for('index.home_view')}">Welcome!</a>
      </h1>
      <p>想要屹立不倒, 必须冷静思考.</p>
    </div>
  </div>
</div><!-- #wrapper -->
</body>
</html>