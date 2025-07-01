# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np               # Para generar datos aleatorios

# Generamos 10,000 coordenadas aleatorias entre 0 y 1 para x y y
coordenadas_x = np.random.rand(10000)
coordenadas_y = np.random.rand(10000)

# ------------------------------
# PRIMER GRÁFICO: Sin transparencia (puede generar sobreposición visual)
# ------------------------------
# Creamos un diagrama de dispersión con puntos completamente opacos (alpha por defecto = 1)
plt.scatter(coordenadas_x, coordenadas_y)

# Títulos y etiquetas
plt.title("Dispersión con Alta Sobreposición")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

# Mostramos el gráfico
plt.show()

# ------------------------------
# SEGUNDO GRÁFICO: Con transparencia para mejorar la legibilidad
# ------------------------------
# Dibujamos el mismo diagrama pero con alpha=0.1 para hacer los puntos más transparentes
plt.scatter(coordenadas_x, coordenadas_y, alpha=0.1)

# Títulos y etiquetas
plt.title("Dispersión con Transparencia Reducida")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

# Mostramos el gráfico
plt.show()
