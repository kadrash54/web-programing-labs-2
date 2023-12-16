from flask import Blueprint, render_template, request
import math
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html',
                           user=user,
                           age=age,
                           sex=sex,
                           errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')

    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/armor')
def armor1():
    x = request.args.get('x')
    n = request.args.get('n')
    result = 0
    if x != None and n != None:
        x = int(x)
        i = int(n)
        for i in range(i, 0, -1):
            result += (-1) ** i * x ** (2 * i + 1) / math.factorial((2 * i + 1))
    return render_template('armor2.html', x=x, n=n, result=result)

@lab3.route('/lab3/armor2')
def armor2():
    errors = {}
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    n3 = request.args.get('n3')
    n4 = request.args.get('n4')
    if n1:
        n1 = float(n1)
    if n2:
        n2 = float(n2)
    if n3:
        n3 = float(n3)
    if n4:
        n4 = float(n4)
    return render_template('armor.html', n1=n1, n2=n2, n3=n3, n4=n4)