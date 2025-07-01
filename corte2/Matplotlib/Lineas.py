# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np               # Para generar y manipular datos numéricos

# Creamos un arreglo con los números de mes (del 1 al 49)
lista_meses = np.arange(1, 50)

# Generamos valores aleatorios para simular las ventas de cada mes (entre 2000 y 4000)
ventas_mensuales = np.random.randint(2000, 4000, size=len(lista_meses))

# ------------------------------
# Gráfico de línea con estilo personalizado
# ------------------------------
plt.plot(
    lista_meses,                # Eje X: meses
    ventas_mensuales,           # Eje Y: ventas
    color='blue',               # Color de la línea
    linestyle='--',             # Línea discontinua
    marker='o'                  # Marcador circular en cada punto
)

# Título del gráfico
plt.title("Venta de un Producto por Mes")

# Etiquetas de los ejes
plt.xlabel("Mes")
plt.ylabel("Venta")

# Activamos la cuadrícula para facilitar la lectura de valores
plt.grid(True)

# Mostramos el gráfico en pantalla
plt.show()
