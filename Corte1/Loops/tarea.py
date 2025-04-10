# Solicitar números al usuario
a = int(input("Ingresa un número entero (a): "))
b = float(input("Ingresa un número decimal (b): "))

# Suma de ambos valores
c = a + b

# Comparación de valores
if a == b:
    print("a y b son iguales")
else:
    print("a y b son diferentes")

# Mostrar tipos de datos
print("El tipo de 'a' es:", type(a))
print("El tipo de 'b' es:", type(b))
print("El valor de c (a + b) es:", c)

# Comparación de tipos
if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferente tipo")
