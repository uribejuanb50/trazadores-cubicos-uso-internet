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

def construirSistema(anios, porcentajes, dfLimpio) :
    return

def eliminacion_gaussiana(A, b) :
    return 

def trazadorCubico() :
    return

if __name__ == "__main__" :
    df = repository.leerArchivo("datosAnios.xlsx")
    separarFunciones(df)