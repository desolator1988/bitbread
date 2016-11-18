<html>
<head>

</head>
<body>
<p>this is index page...</p>
<div>
    ${table(test_bitbread)}
</div>

<%def name="table(test_bitbread)">
    <p>
        ${test_bitbread.name}
    </p>
</%def>
</body>
</html>