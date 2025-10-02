#------------------------------------------------------
#               Interpolacion de Lagrange
#------------------------------------------------------


def peso(vector, posicion, valor):
    peso = 1
    for i in range(len(vector)):
        if i != posicion:
            peso *= (valor - vector[i]) / (vector[posicion] - vector[i])
            # print(f"posicion: {posicion}, i: {i}, valor: {valor}, "
            #     + "vector[i]: {vector[i]}, vector[posicion]: {vector[posicion]}, cosiente: {(valor - vector[i])}, divisor: {(vector[posicion] - vector[i])} peso: {peso}")
            
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