import sys
import os
import pandas as pd
from pathlib import Path

#Agarro los datos desde el excel y no los hardcodeo por simple hecho que voy a subir esto a github
#y que es una buena práctica, más si alguna empresa revisa mis repositorios


#lee archivo 
def leerArchivo(nombreArchivo) :

    try:
        # Si corre como ejecutable PyInstaller, usa _MEIPASS
        if getattr(sys, 'frozen', False):
            base = Path(sys._MEIPASS)
        else:
            base = Path(__file__).parent.parent

        directorioPrincipal = base / "datosAnios.xlsx"

        datosExcel  = pd.read_excel(directorioPrincipal, sheet_name = 18, header = 1)

        print(f"[Repository] Datos crudos sin separar del excel : {str(nombreArchivo)}")
        print(datosExcel)

        print(f"[Repository] Los datos de los años son: {datosExcel['anio'].tolist()}")
        print(f"[Repository] Los datos de los años son: {datosExcel['porcentaje'].tolist()}")
        
        #Retorna los datos del excel año y porcentaje
        return datosExcel

    except FileNotFoundError as e:
        print(f"no se encontró el archivo {nombreArchivo} con el error e: {e}")
    except Exception as e :
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__" :
    leerArchivo("datosAnios.xlsx")