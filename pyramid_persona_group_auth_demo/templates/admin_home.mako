<html>
<head>
    <script type="text/javascript"
            src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
    </script>
    <script src="https://login.persona.org/include.js"></script>
    <script >${request.persona_js}</script>
</head>
<body>
    <h1>Pyramid Persona Group Auth Demo Admin</h1>
    Welcome to the admin side, ${userid}
    ${request.persona_button}
</body>
</html>
