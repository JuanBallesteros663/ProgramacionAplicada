# SETS

# Se define un conjunto con animales, incluyendo un duplicado ('gato')
animales = {'gato', 'perro', 'pez dorado', 'canario', 'gato'}

# Al imprimir, el duplicado se elimina automáticamente (propiedad del conjunto)
print(animales)

# ----------------------------------------------------------------

# Se crean dos conjuntos numéricos
pares = {2, 4, 6, 8, 10}           # Conjunto de números pares
grandes = {6, 7, 8, 9, 10}        # Conjunto de números mayores o iguales a 6

# Diferencia: elementos en 'grandes' que no están en 'pares'
print(grandes - pares)

# Unión: todos los elementos presentes en cualquiera de los dos conjuntos
print(grandes | pares)

# Intersección: elementos que están en ambos conjuntos
print(grandes & pares)

# ----------------------------------------------------------------

# Se imprime el conjunto directamente (el orden puede variar)
print(animales)

# Se muestra el conjunto ordenado alfabéticamente como lista
print(sorted(animales))

# ----------------------------------------------------------------

# Un diccionario vacío ({} por defecto es un diccionario)
dicc_vacio = {}
print(dicc_vacio)

# Un conjunto vacío debe definirse con set()
conj_vacio = set()
print(conj_vacio)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# RANGES

# Convierte un rango de 0 a 9 en una lista
print(list(range(10)))

# Lista de 1 a 10 inclusive
print(list(range(1, 11)))

# Lista de impares entre 1 y 10 (saltos de 2)
print(list(range(1, 11, 2)))

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# CONVERSIONES ENTRE TIPOS DE COLECCIONES

# Lista con duplicado
animales_2 = ['cat', 'dog', 'goldfish', 'canary', 'cat']
print(animales_2)

# Eliminamos duplicados al convertir a conjunto
animals_conjunto = set(animales_2)
print(animals_conjunto)

# El conjunto se convierte a lista (elementos únicos)
animals_lista = list(animals_conjunto)
print(animals_lista)

# La lista se transforma en tupla (inmutable)
animals_tuple = tuple(animals_lista)
print(animals_tuple)

# ------------------------------------------------------------------

# Diccionario con colores y cantidad de canicas
canicas = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(canicas)

# Lista de claves (colores)
colours = list(canicas)
print(colours)

# Tupla con los valores (cantidades)
cantidad = tuple(canicas.values())
print(cantidad)

# Convertimos los pares clave-valor a un conjunto de tuplas
canicas_conj = set(canicas.items())
print(canicas_conj)

# ------------------------------------------------------------------

# Creamos un diccionario a partir de una lista de tuplas
# Cada tupla representa un par clave:valor
dicc1 = dict([(1, 2), (3, 4)])
print(dicc1)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# STRINGS

s = "abracadabra"

# Largo del string
print(len(s))

# Posición de la primera aparición de 'b'
print(s.index("b"))

# Primer caracter del string
print(s[0])

# Substring desde la posición 3 hasta antes de la 7
print(s[3:7])

# print(s[0] = "b")  # Error: los strings son inmutables

# ------------------------------------------------------------------

# Comprobamos si un caracter está en una cadena
print('q' in 'abcd')

# Verificamos si un substring está contenido en otro
print('cd' in 'abcd')

# Verificamos si una lista está dentro de otra (esto da False)
print(['a', 'b'] in ['a', 'b', 'c', 'd'])

# ------------------------------------------------------------------

# Lista de caracteres
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

# Unimos los caracteres sin separador
s = "".join(l)
print(s)

# ------------------------------------------------------------------

# Tupla con nombres de animales
animals = ('cat', 'dog', 'fish')

# Unimos con espacios
print(" ".join(animals))

# Unimos con comas
print(",".join(animals))

# Unimos con coma y espacio
print(", ".join(animals))

# ------------------------------------------------------------------

# Separaciones de strings con distintos delimitadores
print("cat    dog fish\n".split())
print("cat|dog|fish".split("|"))
print("cat, dog, fish".split(", "))
print("cat, dog, fish".split(", ", 2))

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# SECUENCIAS BIDIMENSIONALES

# Matriz 4x3 como lista de listas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

# Accedemos al elemento (0, 0)
print(matriz[0][0])

# Modificamos el valor en la posición (0, 0)
matriz[0][0] = 42

# Imprimimos la matriz completa
print(matriz)

# ------------------------------------------------------------------

# Lista con filas de diferente longitud (lista irregular)
lista2d = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print(lista2d)

# Lista tridimensional 2x2x2
lista3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]

# Mostramos el contenido total y accedemos a un elemento profundo
print(lista3d)
print(lista3d[0][0][0])

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# LISTAS REPETIDAS Y COMPRENSIONES

# Crea una lista con 100 ceros
lista_larga = [0] * 100
print(lista_larga)

# Lista con 24 strings vacíos
dia = [""] * 24
print(dia)

# Multiplica la lista 'dia' 7 veces (referencias compartidas)
timetable = dia * 7
print(timetable)

# Genera 7 listas distintas de 24 strings vacíos
# Cada día tiene su propia lista
timetable = [[""] * 24 for day in range(7)]
print(timetable)