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
        x_izquierda = x[:-1]  # Todos los elementos menos el ultimo
        x_derecha = x[1:]     # Todos los elementos menos el primero
        
        y_izquierda = y[:-1]  # Todos los elementos menos el ultimo
        y_derecha = y[1:]     # Todos los elementos menos el primero
        
        # f[x0, x1, ..., xn] = (f[x1, ..., xn] - f[x0, ..., xn-1]) / (xn - x0) 
        # donde tenemos: 
        #   x0 = x[n-k]
        #   nuestra funcion a_n requiere un nuevo n que representa el tamaño de la lista
        
        proxima_iteracion = n - 1
        return (a_n(proxima_iteracion, x_derecha, y_derecha) - a_n(proxima_iteracion, x_izquierda, y_izquierda)) / (x[n-1] - x[n-k])
    else:
        return y[0]

# Mejorado con uso de cache, utiliza "last recently used" para guardar resultados previos ya calculados.
# De esta manera no se necesita recalcular valores ya obtenidos para los siguientes a_k.
from functools import lru_cache
def a_n_mejorado(n, x, y):
    @lru_cache(maxsize=None)
    # Se crea una funcion interna recursiva para usar cache, i es el indice inicial
    def _a_n(n, i):  
        if n == 0:
            return y[i]
        return (_a_n(n-1, i+1) - _a_n(n-1, i)) / (x[i+n] - x[i])
    
    return _a_n(n-1, 0)

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
        raise ValueError("Las listas x e y deben tener la misma longitud.") # Da error si el archivo esta mal
    n = len(x)  # Se evalua la cantidad de puntos que se tienen
    polinomio_x = 0
    for i in range(1, n+1):
        coef = i        # Nos sirve para cuando i = n, cambiar i = n*2, j sigue siendo n
        if(i == n):
            i = n*2  # Para cuando tengamos la uultima iteracion, se ejecuta la lista completa
             
        adicion = a_n_mejorado(coef, x[:-(n-i)], y[:-(n-i)]) # Coeficiente a_0, luego a_1; a_2; ...; a_n
        for j in range(coef-1):
            adicion *= (valor - x[j])   # Multiplicacion por (x - x0)(x - x1)...(x - xk)
            
        polinomio_x += adicion
        
    return polinomio_x



#------------------------------------------------------
#               Interpolacion de Newton
#           Vector de coeficientes mutable
#------------------------------------------------------


def coeficientes(x, y):
    """
    Calcula los coeficientes de las diferencias divididas
    de Newton a partir de los puntos (x, y).
    """
    n = len(x)
    # Copiamos los valores iniciales de y
    coef = [yi for yi in y]

    # Construimos la tabla de diferencias divididas
    # Se cambian los valores del vector coef, haciendo que el nuevo valor de i sea 
    # el resultado del valor actual del i con el valor del i-1 dividido por la diferencia de x's
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef


def calcular_Px(coef, x, val):
    """
    Evalúa el polinomio de Newton en el valor 'val'
    usando los coeficientes obtenidos.
    Retorna P(val)=a0 + a1(x-x0) + a2(x-x0)(x-x1) + ...
    """
    n = len(coef)
    Px = coef[0] # El primer coeficiente es f(x0)

    for i in range(1, n):
        producto = 1
        for j in range(i):
            producto *= (val - x[j])    # (x - x0)(x - x1)...(x - x_(i-1))
        Px += coef[i] * producto        # a_i * [ (x - x0)(x - x1)...(x - x_(i-1)) ]

    return Px


def Interpol_Newton_2(x, y, val):
    """
    Función principal que construye el polinomio interpolador
    de Newton y lo evalúa en 'val'.
    """
    if len(x) != len(y):
        raise ValueError("Los vectores x e y deben tener la misma longitud.")

    # Obtener los coeficientes de Newton
    coef = coeficientes(x, y)

    # Calcular el valor interpolado
    return calcular_Px(coef, x, val)