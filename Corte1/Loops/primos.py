import time

inicio = time.time()

# Verificar números primos del 0 al 30
for numero in range(0, 31):
    divisores = 0
    for n in range(1, numero + 1):
        if numero % n == 0:
            divisores += 1

    if divisores == 2:
        print(f"{numero} es un número primo")

fin = time.time()
tiempo_total = (fin - inicio) * 1000
print(f"Tiempo de ejecución: {tiempo_total:.2f} ms")
