

# ------------------------------------------------
#                Metodo de Euler
# ------------------------------------------------


def y_euler(y_n, y_prima, h): 
    return y_n + h*y_prima

def puntos_aprox_euler(y_0, y_prima, h, x_buscado):
    puntos = [y_0]
    n = int (x_buscado / h)
    y_n = y_0
    for i in range(n):
        x_n = i*h
        y_plus = y_euler(y_n, y_prima(x_n, y_n), h)
        y_n = y_plus
        # print(y_plus)
        puntos.append(y_plus)
    
    return puntos
        

# ------------------------------------------------
#                Metodo de Heung
# ------------------------------------------------

def y_heung(y_n, y_prima_actual, y_prima_siguiente, h): 
    return y_n + h*((y_prima_actual + y_prima_siguiente)/2)

def puntos_aprox_heung(y_0, y_prima, h, x_buscado):
    puntos = [y_0]
    n = int (x_buscado / h)
    y_n = y_0
    for i in range(n):
        x_n = i*h
        y_auxiliar = y_euler(y_n, y_prima(x_n, y_n), h)
        y_siguiente = y_heung(y_n, y_prima(x_n, y_n), y_auxiliar, h)
        y_n = y_siguiente
        # print(y_siguiente)
        puntos.append(y_siguiente)
        
    return puntos