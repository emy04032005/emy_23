from flask import Flask

app = Flask(_name_)

@app.route('/suma/<int:num1>,<int:num2>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>')
def suma(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resultado}</h1></center>'

@app.route('/resta/<int:num1>,<int:num2>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>')
def resta(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resultado}</h1></center>'

@app.route('/')
def hello_world():
    return '<center><h1>5to B Infiormatica</h1></center>'

if _name_ == '_main_':
    app.run()