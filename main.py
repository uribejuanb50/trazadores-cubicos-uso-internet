import grafica.grafica as graf
import repository.dataRepository as repo
import trazadorCubico.trazadorCubico as trazador

def main() :

    archivo = "datosAnios.xlsx"
    dataFrameExcel = repo.leerArchivo(archivo)

    anios, porcentajes, faltantes = trazador.separarFunciones(dataFrameExcel)
    h = trazador.calcularH(anios)
    A, b = trazador.construirSistema(anios, porcentajes, h)
    M = trazador.eliminacion_gaussiana(A, b)
    valoresInterpolados = trazador.iterarListaParaBuscarDatos(anios, porcentajes, faltantes, h, M)


    graf.graficar(anios, porcentajes, faltantes, valoresInterpolados)
    return  

if __name__ == "__main__" :
    main()