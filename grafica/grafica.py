import sys
from pathlib import Path

RAIZ = Path(__file__).parent.parent
sys.path.append(str(RAIZ))

import trazadorCubico.trazadorCubico as TrazadorCubico
import matplotlib.pyplot as plt

def graficar(anios, porcentajes, faltantes, valoresInterpolados):

    datos = {}

    #Combinación de conocidos y desconocidos
    for i in range(len(anios)) :
        datos[anios[i]] = porcentajes[i]

    for i in range(len(faltantes)) :
        datos[faltantes[i]] = valoresInterpolados[i]

    #Ordenar años
    aniosCompletos = sorted(datos.keys())
    porcentajesCompletos = [datos[a] for a in aniosCompletos]

    #Graficar
    plt.figure(figsize=(12,6))

    #Linea completa
    plt.plot(aniosCompletos, porcentajesCompletos, '-', color = 'steelblue', label = 'Datos completos')

    #Puntos conocidos
    plt.scatter(anios, porcentajes, color = 'steelblue', zorder = 5, label = 'Datos conocidos')

    #puntos interpolados
    plt.scatter(faltantes, valoresInterpolados, marker = 'D', label = 'Datos interpolados', zorder = 6, color = 'red')

    #Etiquetas y estilo
    plt.title("porcentaje de personas que usan internet * año del  PAÍS 18")
    plt.xlabel("Año")
    plt.ylabel('% de personas que usan internet')
    plt.xticks(aniosCompletos, rotation = 45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True, linestyle = '--', alpha = 0.5)
    plt.savefig("Grafica_JuanBernardoUribe", dpi = 150)
    plt.show()

    return