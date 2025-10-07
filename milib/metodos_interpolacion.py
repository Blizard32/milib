#------------------------------------------------------
#               Interpolacion de Lagrange
#------------------------------------------------------


def peso(vector, posicion, valor):
    """
    Calcula el peso de Lagrange para un punto en especifico
    Args:
        vector (vector): Son los datos de la tabla x-espaciados.
        posicion (int): Es la posicion del vector que se esta evaluando.
        valor (float): Es el valor en el que se quiere evaluar la funcion.
        
    Returns:
        peso (float): Es el peso de lagrange para el punto en especifico.
    """
    peso = 1
    for i in range(len(vector)):
        if i != posicion:
            peso *= (valor - vector[i]) / (vector[posicion] - vector[i])
            
    return peso

#------ Usando vectores de puntos x e y ------
def interpol_lagrange(x, y, valor):
    """Interpolacion de lagrange mediante puntos obtenidos de una tabla

    Args:
        x (vector): Son los datos de la tabla x-espaciados.
        y (vetcor): Son los datos que representan cada x.
    """
    interpolacion = 0
    for i in range(len(x)):
        interpolacion += y[i] * peso(x, i, valor)

    return interpolacion

#------ Usando matriz directamente ------
def interpol_lagrange(matriz, valor):
    """Interpolacion de lagrange mediante matriz pasada como argumento

    Args:
        x (vector): Son los datos de la tabla x-espaciados.
        y (vetcor): Son los datos que representan cada x.
    """
    x = [fila[0] for fila in matriz]  # Se extraen los valores de la columna 0  [x]
    y = [fila[1] for fila in matriz]  # Se extraen los valores de la columna 1 [f(x)]
    interpolacion = 0
    for i in range(len(x)):
        interpolacion += y[i] * peso(x, i, valor)

    return interpolacion



#------------------------------------------------------
#               Interpolacion de Newton
#------------------------------------------------------

def a_n(n, x, y):
    """Calcula el coeficiente a_n,k de la tabla de diferencias divididas

    Args:
        n (int): Es el indice del coeficiente a calcular
        k (int): Es el orden actual del coeficiente
        matriz (vector): Es la matriz que contiene los datos y las diferencias divididas
    """
    if n > 1:
        k = len(x)
        # print("Comienzo recursividad") # Ayuda para debuggear
        return (a_n(n-1, x[1:], y[1:]) - a_n(n-1, x[:-1], y[:-1])) / (x[n-1] - x[n-k])
    else:
        # print("Se devolvio f(k): ", y) # Ayuda para debuggear
        return y[0]

def interpol_newton(matriz, valor):
    """Interpolacion de Newton mediante matriz pasada como argumento
    Args:
        matriz (matrix): Es la matriz que contiene los datos y las diferencias divididas
        valor (float): Es el valor en el que se quiere evaluar la funcion.
        
    Returns:
        polinomio_x (float): Es el valor del polinomio de Newton evaluado en "valor".

    """
    x = [fila[0] for fila in matriz]  # Se extraen los valores de la columna 1  [x]
    y = [fila[1] for fila in matriz]  # Se extraen los valores de la columna 2 [f(x)]
    if len(x) != len(y):
        raise ValueError("Las listas x e y deben tener la misma longitud.")
    n = len(x)  # Se evalua la cantidad de puntos que se tienen
    polinomio_x = 0
    for i in range(1, n+1):
        coef = i        # Nos sirve para cuando i = n, cambiar i = n*2, j sigue siendo n
        if(i == n):
            i = n*2  # Para cuando tengamos la uultima iteracion, se ejecuta la lista completa
             
        # print(x[:-(n-i)], y[:-(n-i)]) # Ayuda para debuggear
        adicion = a_n(coef, x[:-(n-i)], y[:-(n-i)])
        for j in range(coef-1):
            adicion *= (valor - x[j])
            
        polinomio_x += adicion
        
    return polinomio_x