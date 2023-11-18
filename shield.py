#for23
from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


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
return render_template('armor.html', x=x, n=n, result=result)


#if 19
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
return render_template('armor2.html', n1=n1, n2=n2, n3=n3, n4=n4)
{% extends "base.html" %}