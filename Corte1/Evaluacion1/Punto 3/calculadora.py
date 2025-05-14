class Calculadora:
    def __init__(self):
        print("Calculadora iniciada.")

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return a / b

def obtener_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def mostrar_menu():
    print("\n======= CALCULADORA POO - MICROPYTHON =======")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def ejecutar_operacion(calculadora, opcion):
    a = obtener_numero("Ingresa el primer número: ")
    b = obtener_numero("Ingresa el segundo número: ")

    try:
        if opcion == '1':
            resultado = calculadora.sumar(a, b)
            print(f"Resultado de la suma: {resultado}")
        elif opcion == '2':
            resultado = calculadora.restar(a, b)
            print(f"Resultado de la resta: {resultado}")
        elif opcion == '3':
            resultado = calculadora.multiplicar(a, b)
            print(f"Resultado de la multiplicación: {resultado}")
        elif opcion == '4':
            resultado = calculadora.dividir(a, b)
            print(f"Resultado de la división: {resultado}")
        else:
            print("Opción no válida.")
    except ZeroDivisionError as e:
        print("Error:", e)
    except Exception as e:
        print("Error inesperado:", e)
