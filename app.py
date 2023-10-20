from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/lab2/example")
def example():
    name = 'Кирилл Кадралеев'
    return render_template('example.html', name=name)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab1/student")
def user_inf():
        return '''
    <!DOCTYPE html>
<html lang="ru">
<head>
    
    <title>Лаба1</title>
</head>
<body>
    <header>
    <h1>КАДРАЛЕЕВ КИРИЛЛ АЛЕКСЕЕВИЧ</h1>
    </header>
    <main>
    <img src="''' + url_for('static', filename='NSTU_logo.png') + '''">
    <a href="http://127.0.0.1:5000/lab1" target="_blank">lab1</a>
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
'''
@app.route("/lab1/python")
def py_inf():
    return '''
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
     Python это скриптовый язык программирования. 
     Он универсален, поэтому подходит для решения разнообразных задач 
     и для многих платформ: начиная с iOS и Android и заканчивая серверными операционными системами. 
     Как и где применяется Python. Это интерпретируемый язык, а не компилируемый, как C++ или Java. 
     Программа на Python представляет собой обычный текстовый файл.

     Python используют много где: от веб-разработки до машинного обучения и научных исследований. 
     Наш курс посвящён только созданию бэкенда сайтов и веб-приложений. 
     Бэкенд — это внутренняя часть программы, которая отвечает за логику. 
     Бэкенд-разработчики пишут код, чтобы основные функции программы работали как надо.
     <img src="''' + url_for('static', filename='Python.jpg') + '''">
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
'''
@app.route("/lab1/bloodborn")
def dark_souls():
    return '''
        <!DOCTYPE html>
<html lang="ru">
<head>
    
    <title>Лаба1</title>
</head>
<body>
    <header>
    НГТУ, ФБ, Лаболраторная работа 1
    </header>
    <main>
    <a href="http://127.0.0.1:5000/lab1" target="_blank">lab1</a>
     Действие игры начинается в охваченном эпидемией чумы вымышленном городе Ярнам, 
     созданном в викторианско-готическом стиле. Игрок принимает управление за странника, 
     который прибыл в город для излечения своей болезни, но стал так называемым «охотником» 
     вследствие местного ритуала переливания крови. Сюжет игры, подобно предыдущим играм FromSoftware, 
     не объясняется напрямую, поэтому одной из основных целей игрока остаётся исследование 
     игровых локаций и уничтожение «добычи» — боссов.

    Bloodborne была высоко оценена игроками и критиками. 
    Из положительных сторон выделяют: проработанный дизайн игровых локаций, 
    персонажей и игровых предметов; динамичные и продуманные сражения, «ускоренные» по сравнению 
    с предыдущими играми FromSoftware. К минусам относят ограниченный выбор оружия и некоторые проблемы 
    с загрузкой локаций на момент релиза игры.
     <img src="''' + url_for('static', filename='Bloodborne.jpeg') + '''">
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
'''
@app.route("/menu")
def menu():
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
@app.route('/lab1/oak')
def oak():
    return '''
    <!DOCTYPE html>
<html lang="ru">
<head>
    
    <title>Лаба1</title>
</head>
<body>
    <h1>ДУБ</h1>
    <img src="''' + url_for('static', filename='oak.jpg') + '''">
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
'''
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
    <a href="http://127.0.0.1:5000/menu" target="_blank">меню</a>
    <h2>Реализованные роуты</h2>
    <a href="http://127.0.0.1:5000/lab1/oak" target="_blank">дуб</a>
    <a href="http://127.0.0.1:5000/lab1/student" target="_blank">студент</a>
    <a href="http://127.0.0.1:5000/lab1/python" target="_blank">питон</a>
    <a href="http://127.0.0.1:5000/lab1/bloodborn" target="_blank">бладборн</a>
    </main>
    <footer>
    Кадралеев Кирилл , ФБИ-11, 3 курс, 2023
    </footer>
</body>
</html>
"""