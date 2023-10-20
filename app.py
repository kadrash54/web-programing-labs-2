from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/lab2/example")
def example():
    name = ''#Кирилл Кадралеев
    srok = '3 ходка'
    number = 'часть 2'
    group = 'ФБИ-11'
    title_name = 'Кадрашевский 54'
    fruits = [
        {'name': 'яблоки', 'price':100},
        {'name': 'груша', 'price': 120},
        {'name': 'апельсин', 'price':80},
        {'name': 'мандаринф', 'price': 95},
        {'name': 'манго', 'price':321}
    ]
    books = [
        {'name': 'Warlock of the Magus World', 'author': 'Wen Chao Gong', 'pages': 610, 'genre': 'Попаданцы'},
        {'name': 'Реинкарнация безработного', 'author': 'Рифудзин-на Магонотэ', 'pages': 5000, 'genre': 'Попаданцы'},
        {'name': 'Грозовой перевал', 'author': 'Эмили Бронте', 'pages': 416, 'genre': 'роман'},
        {'name': 'Сто лет одиночества', 'author': 'Габриэль Гарсия Маркес', 'pages': 416, 'genre': 'роман'},
        {'name': 'Великий Гэтсби', 'author': 'Фрэнсис Скотт Фицджеральд', 'pages': 448, 'genre': 'роман'},
        {'name': 'Приключения Шерлока Холмса', 'author': 'Артур Конан Дойл', 'pages': 704, 'genre': 'детектив'},
        {'name': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'pages': '420-480 в зависимости от издания', 'genre': 'роман'},
        {'name': 'Атлант расправил плечи', 'author': 'Айн Рэнд', 'pages': 1398, 'genre': 'роман'},
        {'name': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'pages': 484, 'genre': 'роман'},
        {'name': 'Робинзон Крузо', 'author': 'Даниель Дефо', 'pages': 230, 'genre': 'роман'}
    ]
    return render_template('example.html', name=name, srok=srok, number=number, group=group,fruits=fruits,books=books)

    @app.route('/lab2/')
    def lab2():
        return render_template('lab2.html')
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
    <a href="/lab1/student" target="_blank">lab1</a>
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