# main.py

from calculadora import Calculadora  #importamos la clase

def main():
    calc = Calculadora()

    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                resultado = calc.sumar(a, b)
            elif opcion == '2':
                resultado = calc.restar(a, b)
            elif opcion == '3':
                resultado = calc.multiplicar(a, b)
            elif opcion == '4':
                resultado = calc.dividir(a, b)
            else:
                print("Opción no válida.")
                continue

            print("Resultado:", resultado)

        except ValueError:
            print("Error: Ingresa un número válido.")
        except ZeroDivisionError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)

if __name__ == "__main__": 
    main()
