def saludar(nombre):
    return f"Hola, {nombre}!"

#-----------------------------------------------------------#

def cargar_v(vector, n):
    """
    <b>Cargar datos de un vector por teclado</b>
    Args:
        vector (number[]): Es el vector en donde se cargan los datos 
        n (int): Cantidad de datos
    """
    print("Ingresar los valores del vector de dimensión ", n, ":")
    for i in range(0, n):
        vector.append(int(input()))

#-----------------------------------------------------------#

def cargar_m(matriz, column, fil):
    """
    <b>Cargar datos de una matriz por teclado</b>
    Args:
        matriz (number[]): Es la matriz en donde se cargan los datos 
        column (int): cantidad de columnas
        fil (int): Cantidad de filas
    """
    print("Ingresar los valores de la matriz de dimensión ", column, "x", fil, ":")
    for n in range(0, column):
        vector = []
        for m in range(0, fil):
            vector.append(int(input()))
        matriz.append(vector)
        

#-----------------------------------------------------------#


def matriz_archivo(path, nombre, matriz, caracter=" "):
    """
    <b>Cargar Matriz desde un archivo</b>

    Args:
        path (path): Ruta en donde se encuentra el archivo 
        nombre (string): Es el nombre del archivo a abrir 
        matriz (number[]): Es la matriz en donde se cargan los datos 
        
    Ejemplo de uso:
        import os
        os.chdir(os.path.dirname(__file__))

        from milib import matriz_archivo

        matriz = [] # Se asigan un vector vacío
        matriz_archivo(__package__, "2columnas", matriz, ",")
    """
    with open(path + nombre + ".txt", "r") as file: 
    # Abrimos el archivo desde la carpeta actual (/.) en modo lectura ("r")
        for linea in file:
            vector = []
            numeros = linea.split(caracter)
            for number in numeros:
                vector.append(float(number))
            matriz.append(vector)
            
        