import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------------
#                Graficar Funciones Lineales 
#-----------------------------------------------------------


def grafico_lineal(x, y=[], ecuacion=[]):
    """Generacion de gráfico de funciones lineales.

    Args:
        x (line_space): Valores del eje x.
        y (list, optional): Funcion o funciones a graficar.
        ecuacion (list, optional): Ecuacion o ecuaciones en formato latex.
        
    Como usar:
        Generar una variable x con los valores del eje x (usando numpy.linspace).
        Generar funciones f(x), g(x), etc.
        Guardar los valores de y en una lista: y = [f(x), g(x), ...]
        Guardar las ecuaciones en formato latex en una lista: ecuacion = [r"$f(x)$", r"$g(x)$", ...]
        (Lo de ecuación es para que se imprima el nombre de las funciones graficadadas)
        
        Llamar a la función grafico_lineal(x, y, ecuacion)
    """
    colors = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray", "olive", "cyan"]
    plt.figure(figsize=(8, 5))
    
    # Caso 1: y es UNA función
    if callable(y):
        print("ESTOY USANDO ESTOOOOO")
        y_vals = y(x)
        plt.plot(x, y_vals, label=ecuacion, color="red", linestyle="--")

    # Caso 2: y es LISTA/TUPLA de funciones
    elif isinstance(y, (list, tuple)) and all(callable(f) for f in y):
        print("ESTOY USANDO ESTAAAAAA")
        for i, f in enumerate(y):
            y_vals = f(x)
            lbl = ecuacion[i] if isinstance(ecuacion, (list, tuple)) else ecuacion
            plt.plot(x, y_vals, label=lbl, color=colors[i % len(colors)], linestyle="--")
            
    elif isinstance(y, (list, tuple)) and all(isinstance(f, (np.ndarray, list)) for f in y):
        print("JAJAJAJAJAJJ")
        for i, f in enumerate(y):
            lbl = ecuacion[i] if isinstance(ecuacion, (list, tuple)) else ecuacion
            plt.plot(x, f, label=lbl, color=colors[i % len(colors)], linestyle="--")

    # Caso 3: y es un array ya evaluado
    elif isinstance(y, (np.ndarray, list)):
        plt.plot(x, y, label=ecuacion, color="red", linestyle="--")

    else:
        raise ValueError("El parámetro y debe ser una función, lista de funciones o vector de valores.")

        
                

    # Personalizar gráfico
    plt.title("Funciones $f(x)$ y $g(x)$ en [0,2]")
    plt.xlabel("x") # Nombre del eje x
    plt.ylabel("y") # Nombre del eje y
    plt.grid(False)  # Se puede poner "False" para sacar el cuadriculado del fondo
    plt.legend()    # Genera un recuado con los datos del "label" de cada función


    #------------ Cosas para modificar el cuadrito de las funciones ------------
    plt.legend(fancybox=True)
    plt.legend(shadow=True)
    plt.legend(facecolor="lightyellow", edgecolor="black")
    plt.legend(frameon=True)   # sin recuadro
    plt.legend(loc="lower right")
    plt.legend(fontsize=12)
    plt.legend(title="Funciones", title_fontsize=10)
    #---------------------------------------------------------------------------

    plt.show() # Muestra el gráfico de ptl
    
    
def grafico_puntos(x=[], y=[], titulo="", etiquetas=["Eje x", "Eje y"]):
    """Generacion de gráfico de puntos.

    Args:
        x (list): valores del eje x.
        y (list): valores del eje y.
        titulo (str): _Titulo del gráfico_. Defaults to "".
        etiquetas (list): _Nombre de ejes_. Defaults to ["Eje x", "Eje y"].
        
    Como usar:
        Generar una variable x con los valores del eje x (usando numpy.linspace).
        Generar funciones f(x), g(x), etc.
        Guardar los valores de y en una lista: y = [f(x), g(x), ...]
        Guardar las ecuaciones en formato latex en una lista: ecuacion = [r"$f(x)$", r"$g(x)$", ...]
        (Lo de ecuación es para que se imprima el nombre de las funciones graficadadas)
        
        Llamar a la función grafico_lineal(x, y, ecuacion)
    """
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color= "purple", marker="o")        

    # Personalizar gráfico
    plt.title(titulo)
    plt.xlabel(etiquetas[0]) # Nombre del eje x
    plt.ylabel(etiquetas[1]) # Nombre del eje y
    plt.grid(False)  # Se pone "False" para sacar el cuadriculado del fondo

    plt.show() # Muestra el gráfico de ptl