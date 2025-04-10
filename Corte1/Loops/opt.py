limite = 30
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        print(numero)
    numero += 1
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break  # se detiene al encontrar el primer divisor
    if es_primo:
        print(numero)
    numero += 1
# Sin usar break
ciclos_sin_break = 0
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        ciclos_sin_break += 1
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        print(numero)
    numero += 1

print(f"Cantidad de ciclos sin break: {ciclos_sin_break}")

# Usando break
ciclos_con_break = 0
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        ciclos_con_break += 1
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
    numero += 1

print(f"Cantidad de ciclos con break: {ciclos_con_break}")
porcentaje = (ciclos_con_break / ciclos_sin_break) * 100
print(f"Se optimizó a un {porcentaje:.2f}% de ciclos aplicando break")
limite = 100

# Sin break
ciclos_sin_break = 0
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        ciclos_sin_break += 1
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        print(numero)
    numero += 1

print(f"Ciclos sin break hasta {limite}: {ciclos_sin_break}")

# Con break
ciclos_con_break = 0
numero = 0

while numero < limite:
    es_primo = True
    for divisor in range(2, numero):
        ciclos_con_break += 1
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
    numero += 1

print(f"Ciclos con break hasta {limite}: {ciclos_con_break}")
porcentaje = (ciclos_con_break / ciclos_sin_break) * 100
print(f"Se optimizó a un {porcentaje:.2f}% de ciclos aplicando break")
