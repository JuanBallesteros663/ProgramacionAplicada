import time

inicio = time.time()

# Buscar e imprimir números primos del 1 al 30
for numero in range(1, 31):
    divisores = 0
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores += 1

    if divisores == 2:
        print(f"{numero} es un número primo\n")

fin = time.time()
duracion = (fin - inicio) * 1000
print(f"Tiempo de ejecución: {duracion:.2f} ms")
