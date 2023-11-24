from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#separamos las operaciones en funciones para no inclumplir el principio de responsabilidad única
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: No se puede dividir por cero.'
    
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    
@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacion = request.form['operacion']

    if operacion == 'sumar':
        resultado = sumar(num1, num2)
    elif operacion == 'restar':
        resultado = restar(num1, num2)
    elif operacion == 'multiplicar':
        resultado = multiplicar(num1, num2)
    elif operacion == 'dividir':
        resultado = dividir(num1, num2)
    elif operacion == 'factorial':
        resultado = factorial_recursivo(num1)
    elif operacion == 'potencia':
        resultado = num1 ** num2
    elif operacion == 'raiz':
        resultado = num1 ** (1/num2)
    else:
        resultado = 'Error: Operación no válida.'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
