import numpy as np
import math as mt
import matplotlib.pyplot as plt

def minimos_cuadrados(matriz):
    n = len(matriz)
    sum_x = sum_y = sum_xy = sum_x2 = 0

    for i in range(n):
        x, y = matriz[i]
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x * x

    a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    a0 = (sum_y - a1 * sum_x) / n

    return a0, a1

def f_minimo_cuadrado(x, a0, a1):
    return a0 + a1 * x

def error_cuadratico_medio(matriz, a0, a1):
    """
        Error por estimacion: e = y - a_0 - a_1 * x <p>
        Error cuadratico medio: ECM = (1/n) * SUM[(y_i - y_ei)^2]
        siendo: n = cantidad de datos, y_i = valor del  dato i, y_ei = valor estimado del dato i
    """
    x = [fila[0] for fila in matriz]
    y = [fila[1] for fila in matriz]
    y_ei = []
    for i in x:
        y_ei.append(f_minimo_cuadrado(i, a0, a1))
    
    sumatoria = 0
    for i in range(len(x)):
        sumatoria += (y[i] - y_ei[i]) ** 2
        
    return mt.sqrt( sumatoria / len(x) )
    



def graficar_recta_puntos(matriz):
    min = matriz[0][0]
    max = matriz[-1][0]
    x = np.linspace(min, max, 50)
    y = []
    a0, a1 = minimos_cuadrados(matriz)
    for i in x:
        y.append(f_minimo_cuadrado(i, a0, a1))
        
    x_puntos = [fila[0] for fila in matriz]
    y_puntos = [fila[1] for fila in matriz]
    
    plt.figure
    plt.plot(x, y, label=r"$y = a_0 + a_1*x$", color="red", linestyle="--")
    plt.scatter(x_puntos, y_puntos, color= "purple", marker="o")
    
    plt.title("Aproximación por Minimos Cuadrados")
    plt.xlabel("x") # Nombre del eje x
    plt.ylabel("y") # Nombre del eje y
    plt.grid(False)  # Se puede poner "False" para sacar el cuadriculado del fondo
    
    plt.show()