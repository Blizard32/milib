
#------------------------------------------------------------------------------
#                           MÉTODO DEL TRAPECIO
#------------------------------------------------------------------------------

def trapecio(f, a, b, n):
    h = (b - a) / n
    i= h 
    elementos_intermedios = 0
    while i < b:
        elementos_intermedios = elementos_intermedios + f(i)
        i = i + h
    integral = (h/2) * (f(a) + 2*elementos_intermedios + f(b))
    return integral



#------------------------------------------------------------------------------
#                           MÉTODO DE SIMPSON 1/3
#------------------------------------------------------------------------------

def simpson_13(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser un número par.")
    h = (b - a) / n
    i = h           #impares
    segmentos_medios = 0
    while i < b:
        segmentos_medios += f(i)
        i += 2 * h
    i = 2 * h       #pares
    segmentos_bordes = 0
    while i < b:
        segmentos_bordes += f(i)
        i += 2 * h
    integral = (h/3) * (f(a) + 4*segmentos_medios + 2*segmentos_bordes + f(b))
    return integral



#------------------------------------------------------------------------------
#                           MÉTODO DE SIMPSON 3/8
#------------------------------------------------------------------------------

def simpson_38(f, a, b, n):
    cont = 0
    if n % 3 != 0:
        raise ValueError("n debe ser múltiplo de 3.")
    h = (b - a) / n
    i = h          #Los segmentos medios izquierda
    segmentos_medios_izquierda = 0
    while i < b:
        segmentos_medios_izquierda += f(i)
        i += 3 * h
    i = 2 * h      #Los segmentos medios derecha
    segmentos_medios_derecha = 0
    while i < b:
        segmentos_medios_derecha += f(i)
        i += 3 * h
        
    segmentos_medios = segmentos_medios_izquierda + segmentos_medios_derecha
    
    i = 3 * h      #Los segmentos bordes
    segmentos_bordes = 0
    while i < b - 2*h:
        segmentos_bordes += f(i)
        i += 3 * h
    integral = ((3*h)/8) * (f(a) + 3*segmentos_medios + 2*segmentos_bordes + f(b))
    return integral



#------------------------------------------------------------------------------
#                           CUADRATURA DE GAUSS
#------------------------------------------------------------------------------

def cuadratura_gauss(f, a, b, n):
    
    if a != -1 or b != 1:
        f_original = f
        print("\nEl intervalo no es [-1, 1], se aplicará una transformación lineal.")
        # Transformación lineal para cambiar el intervalo [a, b] a [-1, 1]
        def g(x):
            return ((b - a) / 2) * x + (a + b) / 2
        def integrando_transformado(x):
            return f_original(g(x)) * (b - a) / 2
        f = integrando_transformado     # Ahora f cambia a la función transformada.
        # Esto hace que luego, en cada iteración del for, se evalua en la funcion transformada y se multiplica por (b-a)/2 cada sección.
    
    if n < 1 or n > 6:
        raise ValueError("n debe estar entre 1 y 6. Respetando los valores de la tabla.")
    
    # Tabla de raíces y pesos para n = 1 a 6
    tabla_valores_z = [
        [-0.5773502692, 0.5773502692], # n=2
        [-0.7745966692, 0.0, 0.7745966692], # n=3
        [-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116], # n=4
        [-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459], # n=5
        
        [-0.9324695142, -0.6612093865, -0.2386191861, 
            0.2386191861, 0.6612093865, 0.9324695142] # n=6
        ]
    tabla_pesos = [
        [1, 1], # n=2
        [5/9, 8/9, 5/9], # n=3
        [0.3478547451, 0.6521451549, 0.6521451549, 0.3478547451], # n=4
        [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851], # n=5
        
        [0.1713244924, 0.3607615730, 0.4679139346, 
            0.4679139346, 0.3607615730, 0.1713244924],  # n=6
        ]
    
    integral = 0
    v_tabla = n - 2 # Es el valor utilizado en las tablas, ya que empiezan en n=2
    for i in range(n):
        integral += tabla_pesos [ v_tabla ][i] * f(tabla_valores_z [ v_tabla ][i])
        
    return integral