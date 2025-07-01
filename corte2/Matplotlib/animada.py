# Importamos las bibliotecas necesarias
import numpy as np                    # Para cálculos numéricos y manejo de arrays
import matplotlib.pyplot as plt       # Para crear gráficos
import matplotlib.animation as anim   # Para animaciones en matplotlib

# Creamos un conjunto de valores en el eje x: 100 puntos entre 0 y 10
x_values = np.linspace(0, 10, 100)

# Calculamos los valores de y como el seno de x
y_values = np.sin(x_values)

# Creamos la figura y los ejes para graficar
figura, eje = plt.subplots()

# Dibujamos la línea inicial con los valores de x e y. El símbolo "," es para desempaquetar una tupla con un solo elemento.
linea_animada, = eje.plot(x_values, y_values)

# Definimos una función que actualiza los datos de la línea para cada cuadro de la animación
def actualizar_cuadro(numero_cuadro):
    # Cambiamos los valores de y aplicando un desfase (para dar efecto de movimiento)
    nuevo_y = np.sin(x_values + numero_cuadro / 10)
    linea_animada.set_ydata(nuevo_y)
    return linea_animada,  # La coma es necesaria porque se devuelve una tupla

# Creamos la animación
# - figura: la figura donde se dibujará la animación
# - actualizar_cuadro: función que actualiza cada cuadro
# - frames=range(100): 100 cuadros, desde 0 hasta 99
# - blit=True: optimiza la animación actualizando solo lo necesario
animacion = anim.FuncAnimation(figura, actualizar_cuadro, frames=range(100), blit=True)

# Mostramos la animación en pantalla
plt.show()
