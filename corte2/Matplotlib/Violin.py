# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np               # Para generar datos aleatorios

# ------------------------------
# Generación de datos
# ------------------------------

# Creamos un conjunto de 1000 valores simulando velocidades promedio
# loc=25: media de 25 km/h
# scale=5: desviación estándar de 5 km/h
# size=1000: cantidad de muestras
velocidades_promedio = np.random.normal(loc=25, scale=5, size=1000)

# ------------------------------
# Gráfico tipo violín (violin plot)
# ------------------------------

# Creamos un gráfico de violín para mostrar la distribución
plt.violinplot(velocidades_promedio)

# Añadimos título y etiqueta del eje Y
plt.title("Distribución de Velocidades Promedio")
plt.ylabel("Velocidad (km/h)")

# Mostramos el gráfico
plt.show()
