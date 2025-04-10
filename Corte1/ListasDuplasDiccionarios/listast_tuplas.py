# Lista de colores
colores = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(colores)
print("Tipo de variable:", type(colores))
print("Elemento en la posición 2:", colores[2])

# Tamaño de la lista
print("Cantidad de elementos:", len(colores))

# Rebanado (slice)
print("Primeros dos colores:", colores[0:2])
print("Primeros dos colores (forma abreviada):", colores[:2])

# Agregar un elemento al final
colores.append('Blanco')
print("Después de agregar 'Blanco':", colores)

# Insertar en una posición específica
colores.insert(3, 'Negro')
print("Después de insertar 'Negro' en la posición 3:", colores)

# Extender con otra lista
colores += ['Marrón', 'Gris']
print("Después de extender:", colores)

# Obtener el índice de un elemento
indice_azul = colores.index('Azul')
print("Índice de 'Azul':", indice_azul)

# Eliminar un elemento por nombre
colores.remove('Marrón')
print("Después de eliminar 'Marrón':", colores)

# Insertar nuevamente 'Marrón' en la posición 8
colores.insert(8, 'Marrón')
print("Después de reinsertar 'Marrón':", colores)

# Eliminar el último elemento con pop
ultimo = colores.pop()
print("Elemento eliminado con pop:", ultimo)

# Tamaño actual
print("Tamaño actual:", len(colores))

# Multiplicar lista (repetir contenido)
colores_repetidos = colores * 3
print("Lista repetida:", colores_repetidos)

# Ordenar alfabéticamente
colores.sort()
print("Colores ordenados:", colores)

# Lista de números
numeros = list(range(10, 0, -1))  # [10, 9, ..., 1]
print("Números antes de ordenar:", numeros)

# Orden ascendente
numeros.sort()
print("Orden ascendente:", numeros)

# Orden descendente
numeros.sort(reverse=True)
print("Orden descendente:", numeros)
print("\n" + "#" * 30)
print("########## TUPLAS ##########")
print("#" * 30)

# Crear una tupla a partir de una lista
tupla_colores = tuple(colores)
print("Tupla creada:", tupla_colores)

# Acceder a elementos por índice
print("Primer color:", tupla_colores[0])
print("Tercer color:", tupla_colores[2])

# Verificar si existe un elemento
print("¿'Rojo' está en la tupla?", 'Rojo' in tupla_colores)
print("¿Cuántas veces aparece 'Rojo'?:", tupla_colores.count('Rojo'))

# Tupla unitaria 
tupla_unitaria = ('Blanco',)
print("Tupla con un solo elemento:", tupla_unitaria)

# Empaquetado de tupla 
info = 'Gaspar', 5, 8, 1999
print("Tupla empaquetada:", info)

# Desempaquetado de tupla
nombre, dia, mes, anio = info
print("Nombre:", nombre)
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)
print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {anio}")

# Convertir tupla a lista
lista_info = list(info)
print("Tupla convertida en lista:", lista_info)
