
#-----------------------------------------------------------
#                   Método de Bisección
#-----------------------------------------------------------

def biseccion(a, b, f, tolerancia_error, iteraciones_totales):
    """
    <b>Función para realizar el método de bisección</b><p>
    Encuentra una raíz de la función f en el intervalo [a, b] usando el método de bisección.
    
    Args:
        a (float): Extremo izquierdo del intervalo.
        b (float): Extremo derecho del intervalo.
        f (function): Función para la cual se busca la raíz. (se debe definir antes de llamar a bisección)
        tolerancia_error (float): Tolerancia para el error porcentual.
        iteraciones_totales (int): Número máximo de iteraciones permitidas.
    
    Returns:
        float: Aproximación de la raíz.
        int: Número de iteraciones realizadas.
    
    Precondición: Debe existir una raiz en el intervalo [a, b].<p> 
                (f(a) y f(b) deben tener signos opuestos)
    """
    if f(a) * f(b) >= 0:
        print("No se puede aplicar el método de bisección.")
        return None
    
    iteraciones = 0
    tolerancia_aceptable = False
    while not tolerancia_aceptable and iteraciones < iteraciones_totales:
        if ((b - a)/2)*100 < tolerancia_error:
            tolerancia_aceptable = True
        c = (a + b) / 2
        if f(c) == 0:
            a = b = c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    
    return (a + b) / 2, iteraciones




#-----------------------------------------------------------
#                   Método de Teylor-Raphson
#-----------------------------------------------------------

def teylor_raphson(x, f, f_dx, tol_e, i_tot):
    """
    Método de Taylor para aproximar la raíz de una función usando el método de Newton-Raphson.
    
    Args:
        x (float): Valor inicial.
        f (function): Función a evaluar.
        f_dx (function): Derivada de la función.
        tol_e (float): Tolerancia del error.
        i_tot (int): Número máximo de iteraciones.
    
    Returns:
        float: Aproximación de la raíz. 
    """
    iteraciones = 0
    tolerancia_aceptable = False
    while not tolerancia_aceptable and iteraciones < i_tot:
        raiz_aprox = x -(f(x)/f_dx(x))
        x = raiz_aprox
        iteraciones += 1
        if abs(f(raiz_aprox)*100) < tol_e:
            tolerancia_aceptable = True
    return raiz_aprox, iteraciones




#-----------------------------------------------------------
#                   Método de Secante
#-----------------------------------------------------------

def secante(x, f, tol_e, i_tot):
    """
    Método de la secante para encontrar una raíz de la función f.
    
    Args:
        x (float): Valor inicial.
        f (function): Función a evaluar.
        tol_e (float): Tolerancia del error.
        i_tot (int): Número máximo de iteraciones.
    
    Returns:
        float: Aproximación de la raíz.
        int: Número de iteraciones realizadas.
    """
    iteraciones = 1
    tolerancia_aceptable = False
    x_ant = x - 1
    while not tolerancia_aceptable and iteraciones < i_tot:
        raiz_aprox = x + (f(x)*(x_ant - x))/(f(x) - f(x_ant))
        x_ant = x
        x = raiz_aprox
        iteraciones += 1
        if(abs(f(raiz_aprox)*100) < tol_e):
            print(f"f({raiz_aprox}) = {f(raiz_aprox)}")
            tolerancia_aceptable = True
            
    return raiz_aprox, iteraciones




#-----------------------------------------------------------
#                Método de Falsa Posición
#-----------------------------------------------------------

def falsa_posicion(xi, xs, f, tol_e, i_tot):
    """ 
    Método de Falsa Posición para encontrar una raíz de la función f en el intervalo [xi, xs].
    
    Args:
        xi (float): Extremo izquierdo del intervalo.
        xs (float): Extremo derecho del intervalo.
        f (function): Función a evaluar.
        tol_e (float): Tolerancia del error.
        i_tot (int): Número máximo de iteraciones.
        
    Returns:
        float: Aproximación de la raíz.
        int: Número de iteraciones realizadas.
    
    Precondición: Debe existir una raíz en el intervalo [xi, xs]. (f(xi) y f(xs) deben tener signos opuestos)
    """
    if f(xi) * f(xs) > 0:
        print("No se puede aplicar el método de falsa posición.")
        print(f"{xi} * {xs} tiene que ser mayor a 0\nresult: {f(xi) * f(xs)}")
        return "null", "no se puede aplicar el método de falsa posición"
    
    iteraciones = 1
    tolerancia_aceptable = False
    while not tolerancia_aceptable and iteraciones < i_tot:
        m = xs - f(xs)*(xs - xi) / (f(xs) - f(xi))
        xi = m
        if abs(f(m)) < tol_e:
            tolerancia_aceptable = True
    
    return m, iteraciones