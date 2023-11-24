from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#separamos las operaciones en funciones para no inclumplir el principio de responsabilidad única

    
@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']

        if operacion in OPERACIONES:
            resultado = realizar_operacion(operacion, num1, num2)
            return render_template('index.html', resultado=resultado)
        else:
            return render_template('index.html', resultado='Error: Operación no válida.')

    except ValueError as e:
        return render_template('index.html', resultado=f'Error: {e}')

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
        raise ValueError("No se puede dividir por cero.")

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def realizar_operacion(operacion, num1, num2):
    if operacion == 'factorial':
        return factorial_recursivo(num1)
    elif operacion == 'potencia':
        return num1 ** num2
    elif operacion == 'raiz':
        return num1 ** (1/num2)
    else:
        return globals()[operacion](num1, num2)

# Lista de operaciones válidas
OPERACIONES = {'sumar', 'restar', 'multiplicar', 'dividir', 'factorial', 'potencia', 'raiz'}



if __name__ == '__main__':
    app.run(debug=True)

