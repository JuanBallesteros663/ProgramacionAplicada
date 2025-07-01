# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np               # Para generar datos numéricos aleatorios

# ------------------------------
# Generación de datos simulados
# ------------------------------

# Generamos 1000 resultados con distribución normal (media=70, desviación estándar=10)
puntajes_simulados = np.random.normal(loc=70, scale=10, size=1000)

# ------------------------------
# Creación del diagrama de caja (boxplot)
# ------------------------------

# Graficamos el diagrama de caja que resume la distribución de los puntajes
plt.boxplot(puntajes_simulados)

# Título del gráfico
plt.title("Diagrama de Caja de Resultados")

# Etiqueta del eje Y
plt.ylabel("Puntajes")

# Mostramos el gráfico en pantalla
plt.show()
