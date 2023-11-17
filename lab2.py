from flask import Blueprint, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route("/lab2/example")
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

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/anime')
def anime_char():
    return render_template('anime.html')