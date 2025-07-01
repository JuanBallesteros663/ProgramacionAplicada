# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para generar gráficos
import numpy as np               # Para cálculos numéricos y generación de datos

# ------------------------------
# Generación de datos
# ------------------------------

# Creamos un conjunto de 10,000 valores equiespaciados de 0 a 100
valores_x = np.linspace(0, 100, 10000)

# Generamos una señal senoidal con algo de ruido aleatorio
valores_y = np.sin(valores_x) + np.random.normal(loc=0, scale=0.1, size=valores_x.shape)

# ------------------------------
# Promediado por intervalos
# ------------------------------

# Dividimos el eje X en 100 intervalos equidistantes
limites_intervalos = np.linspace(0, 100, 100)

# Calculamos el promedio de Y en cada intervalo de X
promedios_por_intervalo = [
    np.mean(valores_y[(valores_x >= limites_intervalos[i]) & (valores_x < limites_intervalos[i + 1])])
    for i in range(len(limites_intervalos) - 1)
]

# ------------------------------
# Gráfico del resultado promediado
# ------------------------------

# Graficamos el promedio de Y para cada intervalo en función del centro de ese intervalo
plt.plot(limites_intervalos[:-1], promedios_por_intervalo)

# Título y etiquetas
plt.title("Gráfica de Datos Promediados por Intervalo")
plt.xlabel("Eje X")
plt.ylabel("Valor Promedio de Y")

# Mostramos el gráfico
plt.show()
