
#-----------------------------------------------------------
#               Aproximación de Horner
#-----------------------------------------------------------

def horner(coefs, x):
    """
    Evalúa un polinomio usando el método de Horner.
    
    Args:
        coefs (list): Coeficientes del polinomio en orden ascendente 
                      [a0, a1, ..., an]<p> donde P(x) = a0 + a1*x + ... + an*x^n
        x (float): Valor en el que se evalúa el polinomio.
    
    Returns:
        float: Resultado de P(x).
    """
    p = coefs[-1]  # coeficiente de mayor grado
    for i in range(len(coefs) - 2, -1, -1):
        p = p * x + coefs[i]
    return p





#-----------------------------------------------------------
#               Aproximación de Taylor
#-----------------------------------------------------------

def teylor(polinomio, x, x0):
    retorno = 0
    grado = len(polinomio)
    for i in range(0, grado):
        termino = polinomio[i] * ((x-x0)**(i))
        retorno = retorno + termino
    return retorno




#-----------------------------------------------------------
#               Factorial de un número
#-----------------------------------------------------------

def factorial(x):
    """ 
    Esta función calcula el factorial de un numero. 
    <p> Utiliza un bucle for para ir multiplicando los valores hasta x. 
    
    Args:
        x (int): Número al que se le quiere calcular el factorial.
        
    Returns:
        int: Factorial de x.
    """
    fact_n = 1
    for i in range(1,x+1):
        fact_n = fact_n * i
    return fact_n
