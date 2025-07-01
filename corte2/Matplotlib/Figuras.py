# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt                      # Para gráficos
from mpl_toolkits.mplot3d import Axes3D              # Para crear gráficos en 3D
import numpy as np                                   # Para cálculos numéricos

# Creamos valores de X e Y: 100 puntos entre -5 y 5
valores_x = np.linspace(-5, 5, 100)
valores_y = np.linspace(-5, 5, 100)

# Creamos una malla (rejilla) 2D a partir de los vectores x e y
# Esto nos da matrices X e Y para evaluar la función Z en una superficie
malla_X, malla_Y = np.meshgrid(valores_x, valores_y)

# Calculamos los valores de Z en cada punto (X, Y)
# La función evaluada es z = sin(raíz(x² + y²))
superficie_Z = np.sin(np.sqrt(malla_X**2 + malla_Y**2))

# ------------------------------
# PRIMERA GRÁFICA: Gráfico 3D de superficie
# ------------------------------
# Creamos una figura
figura_3d = plt.figure()

# Añadimos un eje 3D a la figura
ejes_3d = figura_3d.add_subplot(111, projection='3d')

# Dibujamos la superficie con un mapa de color (colormap) tipo 'viridis'
ejes_3d.plot_surface(malla_X, malla_Y, superficie_Z, cmap='viridis')

# Título del gráfico
plt.title("Gráfica 3D de Superficie")

# Mostramos el gráfico 3D
plt.show()

# ------------------------------
# SEGUNDA GRÁFICA: Mapa de contorno 2D
# ------------------------------
# Creamos un gráfico de contorno relleno (contourf)
plt.contourf(malla_X, malla_Y, superficie_Z, cmap='viridis')

# Añadimos una barra de color para indicar los valores de Z
plt.colorbar(label='Valor de Z')

# Títulos y etiquetas
plt.title("Mapa de Contorno 2D")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostramos el gráfico 2D
plt.show()
