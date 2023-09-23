from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def start():
    return """
    <!DOCTYPE html>
<html lang="ru">
<head>
    
    <title>Лаба1</title>
</head>
<body>
    <header>
    НГТУ, ФБ, Лаболраторная работа 1
    </header>
    <h1>web-сервер на flusk</h1>
    <main>
    <a href="http://127.0.0.1:5000/lab1" target="_blank">lab1</a>
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
    <!DOCTYPE html>
<html lang="ru">
<head>
    
    <title>Лаба1</title>
</head>
<body>
    <header>
    НГТУ, ФБ, Лаболраторная работа 1
    </header>
    <h1>web-сервер на flusk</h1>
    <main>
    Flask — фреймворк для создания веб-приложений на языке
    программирования Python, использующий набор инструментов
    Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
    называемых микрофреймворков — минималистичных каркасов
    веб-приложений, сознательно предоставляющих лишь самые ба-
    зовые возможности.  
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
"""