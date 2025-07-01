# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt  # Para crear gráficos
import numpy as np               # Para generar datos numéricos

# ------------------------------
# Generación de datos simulados
# ------------------------------

# Días del mes de abril (del 1 al 30)
dias_del_mes = np.arange(1, 31)

# Generamos temperaturas aleatorias entre 10°C y 30°C para cada día
temperaturas_diarias = np.random.randint(10, 30, size=30)

# ------------------------------
# Gráfico de la serie temporal de temperatura
# ------------------------------

plt.plot(
    dias_del_mes,               # Eje X: días
    temperaturas_diarias,       # Eje Y: temperaturas
    color='orange',             # Color de la línea
    marker='x',                 # Marcador en forma de 'x' en cada punto
    linestyle='-'               # Línea continua
)

# Título y etiquetas con tamaños de fuente personalizados
plt.title("Temperatura Diaria en Abril", fontsize=16)
plt.xlabel("Día", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)

# Activamos la cuadrícula para facilitar la lectura
plt.grid(True)

# Agregamos una leyenda en la esquina superior derecha
plt.legend(['Temperatura'], loc='upper right')

# ------------------------------
# Anotación: Día más caluroso
# ------------------------------

# Identificamos el día con la temperatura más alta
dia_mas_caluroso = dias_del_mes[np.argmax(temperaturas_diarias)]
temperatura_maxima = np.max(temperaturas_diarias)

# Añadimos una anotación con flecha al punto de mayor temperatura
plt.annotate(
    'Día más caluroso',
    xy=(dia_mas_caluroso, temperatura_maxima),           # Punto al que apunta la flecha
    xytext=(dia_mas_caluroso + 1, temperatura_maxima - 4),  # Posición del texto
    arrowprops=dict(facecolor='black', arrowstyle='->')  # Estilo de flecha
)

# Ajustamos los márgenes automáticamente para evitar que se solapen elementos
plt.tight_layout()

# Mostramos el gráfico en pantalla
plt.show()
