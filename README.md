# SPAGHETTI-CODE

El link al repositorio es el siguiente: https://github.com/Germiprogramer/SPAGHETTI-CODE.git

# Identificación de características de "Spaghetti Code": Debes ser capaz de identificar las características de "Spaghetti Code" en el código proporcionado. (20%)

El código proporcionado tiene algunas características de "Spaghetti Code".

Falta de Estructura:
El código carece de una estructura clara y organización. Todas las operaciones están en el mismo bloque de código, lo que dificulta la lectura y comprensión.

Uso de "Print" para Mensajes de Error:
En lugar de lanzar excepciones, se utiliza la función print para mostrar mensajes de error en la consola. Esto puede ser problemático, ya que no proporciona una forma efectiva de manejar errores en otras partes del programa.

Lógica de Control Confusa:
El uso de múltiples bloques if sin else if o elif puede hacer que la lógica sea confusa. Todos los bloques if se evalúan, incluso si uno de ellos ya fue verdadero, lo que puede llevar a comportamientos inesperados.

Operación no Soportada:
En lugar de lanzar una excepción o manejar de manera más elegante el caso de una operación no soportada, simplemente se imprime un mensaje en la consola. Esto podría dificultar la identificación de errores y la depuración.

Falta de Modularidad:
La función calcular podría beneficiarse de una mayor modularidad. Separar las operaciones en funciones más pequeñas y bien definidas haría que el código sea más fácil de entender y mantener.

# Refactorización de código: Debes ser capaz de refactorizar el código para mejorar su legibilidad y mantenibilidad. Esto podría incluir la eliminación de la lógica de control basada en cadenas de texto, la modularización del código, y la mejora del manejo de errores. (60%)

# Justificación de cambios: Debes ser capaz de justificar los cambios que has hecho al código, explicando cómo estos cambios mejoran el código y cómo evitan las características de "Spaghetti Code". (20%)

Vamos a refactorizar la función calcular para mejorar su estructura y legibilidad. Aquí hay una versión mejorada:
      
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


Principales cambios realizados:

Manejo de Excepciones:
Se utiliza un bloque try-except para manejar excepciones, especialmente aquellas relacionadas con la conversión de cadenas a números.

Diccionario de Operaciones:
Se utiliza un diccionario (OPERACIONES) para almacenar las operaciones válidas, lo que simplifica la lógica de verificación.

Función realizar_operacion:
Se ha introducido una función realizar_operacion para manejar la lógica de ejecutar la operación seleccionada. Esto hace que el código sea más modular y fácil de entender.

Uso de globals():
Se utiliza globals()[operacion] para llamar a la función de operación directamente desde el espacio de nombres global, evitando múltiples declaraciones if/elif.
