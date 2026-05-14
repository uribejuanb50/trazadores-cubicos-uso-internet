import pandas as pd
from pathlib import Path

#Agarro los datos y no los hardcodeo por simple hecho que voy a subir esto a github
#y que es una buena práctica, más si alguna empresa revisa mis repositorios


#lee archivo 
def leerArchivo(nombreArchivo) :

    #indicar directorio actual
    directorioActual = Path(__file__).parent

    #subir al nivel del directorio principal
    directorioPrincipal = directorioActual.parent / "datosAnios.xlsx"

    datosExcel  = pd.read_excel(directorioPrincipal, sheet_name = 18, header = 2)

    print(datosExcel)

if __name__ == "__main__" :
    leerArchivo("datosAnios")