# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear los gráficos
import numpy as np               # Para generar datos aleatorios

# Definimos las zonas geográficas
nombres_zonas = ['Norte', 'Sur', 'Este', 'Oeste']

# Nombres de los meses del año
nombres_meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

# Generamos datos aleatorios de asistencia por zona y por mes
# Matriz de 4 filas (zonas) x 12 columnas (meses)
asistencias_por_zona = np.random.randint(100, 2000, size=(4, 12))

# Creamos una figura con 4 subgráficos (2x2)
figura, ejes = plt.subplots(2, 2, figsize=(10, 8))

# Título general de la figura
figura.suptitle('Asistencia Mensual por Zona')

# Recorremos cada zona para graficarla individualmente
for indice, nombre_zona in enumerate(nombres_zonas):
    # Determinamos la posición del subplot (fila, columna)
    fila = indice // 2
    columna = indice % 2
    eje_actual = ejes[fila, columna]

    # Graficamos los datos de asistencia para esa zona
    eje_actual.plot(nombres_meses, asistencias_por_zona[indice], marker='o')

    # Título y etiquetas de cada subgráfico
    eje_actual.set_title(nombre_zona)
    eje_actual.set_xlabel("Mes")
    eje_actual.set_ylabel("Asistencia (Personas)")

# Ajustamos automáticamente los espacios para que no se sobrepongan
plt.tight_layout()

# Mostramos el gráfico en pantalla
plt.show()
