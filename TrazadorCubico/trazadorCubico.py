import sys
from pathlib import Path

RAIZ = Path(__file__).parent.parent
sys.path.append(str(RAIZ))

import repository.dataRepository as repository

#quiebra los datos de excel en 3
def separarFunciones(dataFrame) :

    #quita los NaN
    dfLimpio = dataFrame.dropna()

    #Separación de listas
    anios = list(dfLimpio.iloc[:, 0].astype(int))
    porcentajes  = list(dfLimpio.iloc[:, 1].astype(float))

    #retorno de los datos
    return anios, porcentajes, dfLimpio

#calcula el espacio entre puntos
def calcularH(anios) :
    n = len(anios) - 1
    h = []

    for i in range(n) :
        h.append(anios[i + 1] - anios[i]) 

    #retorna una lista de hs
    return h

#Construye sistemas de ecuaciones lineales Ax = b
def construirSistema(anios, porcentajes, h) :

    #establece límites
    n = len(anios)

    #Construir matriz en 0s
    A = [[0.0]*n for _ in range( n )]
    b = [0.0]*n

    #condicion de frontera natural, 0 porque se exige que en los extremos sea 0
    A[0][0] = 1.0
    A[n - 1][n - 1] = 1.0

    #recorre los puntos internos del trazador
    for i in range (1, n - 1) :
        A[i][i - 1] = h[i - 1] #adigna el paso anterior a la subdiagonal
        A[i][i] = 2*(h[i - 1] + h[i]) #Calcula el peso del nodo actual. Es el doble de la suma de los pasos izquierdo y derecho
        A[i][i + 1] = h[i] #Asigna el valor del paso siguiente (hi) como coeficiente de la incógnita siguiente

        b[i] = 6*((porcentajes[i + 1] - porcentajes[i])/h[i] - (porcentajes[i] - porcentajes[i - 1])/h[i - 1])

    print(A)
    print(b)

    return A, b

def eliminacion_gaussiana(A, b) :
    return 

def trazadorCubico() :
    return

if __name__ == "__main__" :
    df = repository.leerArchivo("datosAnios.xlsx")

    anios, porcentajes, limpios = separarFunciones(df)

    h = calcularH(anios)

    construirSistema(anios, porcentajes, h)
