from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    
    <title>Document</title>
</head>
<body>
    <header>
    </header>
    <h1>web-сервер на flusk</h1>
    <footer>
    </footer>
</body>
</html>
"""