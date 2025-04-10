while True:
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        print("Número ingresado:", numero)

        if numero > 0:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es: {factorial}")
        else:
            print("Por favor, ingresa un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número entero.")
