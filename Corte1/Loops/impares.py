# Identificar números pares e impares del 1 al 20
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
        print(f"{i} es impar")  # Mismo mensaje dos veces como en el original

# Mostrar los cubos de los números del 0 al 5
for i in range(6):
    print(i ** 3)

# Solicitar un número y repetir un mensaje esa cantidad de veces (si es mayor que 0)
try:
    times = int(float(input("Ingresa un número para 'times': ")))
    print(type(times))
    print(times)

    if times == 0:
        print("No hagas nada")
    else:
        for i in range(1, times + 1):
            print(f"i = {i}")
except ValueError:
    print("Por favor, ingresa un número válido.")