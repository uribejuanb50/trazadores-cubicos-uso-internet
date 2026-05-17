# Interpolación Numérica: Trazadores Cúbicos para Análisis de Adopción de Internet

## Descripción del Proyecto

Este proyecto implementa un algoritmo de **interpolación numérica usando trazadores cúbicos naturales** para estimar datos faltantes en series de tiempo. Específicamente, utiliza datos de adopción de internet (porcentaje de población) en el período 1994-2023, donde faltan cinco años de información.

**Objetivo:** Interpolar los cinco años faltantes usando todas los datos conocidos disponibles y generar una visualización de la serie completa.

---

## ¿Cómo Funciona?

### Algoritmo: Trazadores Cúbicos Naturales

Un trazador cúbico es un conjunto de **polinomios cúbicos** (grado 3) que se conectan suavemente entre los puntos conocidos. En lugar de usar un único polinomio gigante de grado 24 (inestable), se construyen polinomios pequeños entre cada par consecutivo de puntos.

#### Pasos del Algoritmo:

**1. Separación de Datos**
   - Se leen los datos del archivo Excel
   - Se separan los años conocidos de los faltantes
   - Se eliminan las filas con valores NaN

**2. Cálculo de Espacios (h)**
   ```
   h[i] = año[i+1] - año[i]
   ```
   Como los años no siempre son consecutivos, estos espacios varían.

**3. Construcción del Sistema Tridiagonal (Ax = b)**
   
   Se construye una matriz tridiagonal basada en las condiciones:
   - Continuidad en los puntos
   - Continuidad de la primera derivada (pendiente)
   - Continuidad de la segunda derivada (curvatura)
   - Condiciones de frontera natural: M₀ = M_n = 0

   Donde M son las "segundas derivadas" (momentos) en cada punto.

**4. Resolución: Eliminación Gaussiana**
   
   Se resuelve el sistema Ax = b usando **eliminación gaussiana**:
   - Eliminación hacia adelante (triangularización)
   - Sustitución hacia atrás (despeje)
   
   Resultado: vector M con todas las segundas derivadas.

**5. Evaluación del Spline**
   
   Para cada año faltante, se encuentra en qué intervalo [año_i, año_{i+1}] cae y se aplica la fórmula del trazador cúbico:
   
   ```
   S(t) = (M[i]/(6h[i])) × (x_{i+1}-t)³ 
        + (M[i+1]/(6h[i])) × (t-x_i)³
        + (y[i]/h[i] - M[i]×h[i]/6) × (x_{i+1}-t)
        + (y[i+1]/h[i] - M[i+1]×h[i]/6) × (t-x_i)
   ```

---

## Ventajas de Trazadores Cúbicos vs Otros Métodos

| Característica | Lagrange | Diferencias Divididas | Hermite | Trazadores Cúbicos |
|---|---|---|---|---|
| Estabilidad con muchos puntos | ❌ Oscila (Runge) | ❌ Oscila | ❌ Oscila | ✅ Estable |
| Suavidad | ❌ Discontinua | ❌ Discontinua | ✅ C¹ continua | ✅ C² continua |
| Complejidad computacional | O(n²) | O(n²) | O(n²) | O(n) tridiagonal |
| Uso en industria | Educativo | Educativo | Especializado | **Estándar CAD/ML** |

---

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Opción 1: Desde el código fuente (Linux/macOS)

```bash
# Clonar el repositorio
git clone https://github.com/uribejuanb50/trazadores-cubicos-uso-internet.git
cd trazadores-cubicos-uso-internet

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python3 main.py
```

### Opción 2: Usar el ejecutable (Sin instalar Python)

**Windows:**
```cmd
trazador-cubico.exe
```

**Linux/macOS:**
```bash
./trazador-cubico
```

Los ejecutables están disponibles en la sección **Releases** o en los **Artifacts** de GitHub Actions.

### Opción 3: Desde Windows (instalando Python)

1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca "Add Python to PATH"
3. Abre CMD y corre:
   ```cmd
   pip install pandas matplotlib openpyxl
   git clone https://github.com/uribejuanb50/trazadores-cubicos-uso-internet.git
   cd trazadores-cubicos-uso-internet
   python main.py
   ```

---

## 🚀 Uso

### Ejecución Básica

```bash
python3 main.py
```

**Salida esperada:**
1. Imprime los datos crudos del Excel
2. Calcula los 5 valores interpolados
3. Genera una gráfica `Grafica_JuanBernardoUribe.png`
4. Muestra la gráfica en pantalla

### Resultados

El programa interpola los siguientes años:
- **1996:** 0.11824%
- **2006:** 19.06842%
- **2015:** 41.37396%
- **2016:** 47.35346%
- **2018:** 58.52376%

Todos los valores tienen **5 decimales** como se requiere.

---

## Estructura del Proyecto

```
trazadores-cubicos-uso-internet/
│
├── main.py                          # Orquestador principal
├── datosAnios.xlsx                  # Datos del Excel
├── requirements.txt                 # Dependencias Python
├── main.spec                        # Configuración PyInstaller
│
├── repository/
│   └── dataRepository.py            # Capa de lectura de datos
│
├── trazadorCubico/
│   └── trazadorCubico.py            # Lógica del algoritmo
│       ├── separarFunciones()       # Limpia datos
│       ├── calcularH()              # Calcula espacios
│       ├── construirSistema()       # Arma matriz A y vector b
│       ├── eliminacion_gaussiana()  # Resuelve Ax=b
│       └── trazadorCubico()         # Evalúa spline en puntos
│
├── grafica/
│   └── grafica.py                   # Visualización matplotlib
│
├── .github/
│   └── workflows/
│       └── build.yml                # CI/CD para compilar ejecutables
│
└── README.md                        # Este archivo
```

---

## Arquitectura por Capas

El proyecto sigue un patrón **de capas** para facilitar mantenimiento y escalabilidad:

### Capa de Repositorio (`repository/`)
- Responsable de la **entrada/salida de datos**
- Lee el archivo Excel usando pandas
- Gestiona la búsqueda y rutas de archivos
- Maneja excepciones de archivos

### Capa de Lógica (`trazadorCubico/`)
- Contiene el **algoritmo numérico puro**
- Completamente independiente de datos/visualización
- Funciones:
  - `separarFunciones()`: prepara datos
  - `calcularH()`: calcula distancias
  - `construirSistema()`: arma Ax=b
  - `eliminacion_gaussiana()`: resuelve el sistema
  - `trazadorCubico()`: evalúa el spline
  - `iterarListaParaBuscarDatos()`: itera sobre años faltantes

### Capa de Presentación (`grafica/`)
- Visualización con **matplotlib**
- Muestra puntos conocidos vs interpolados
- Genera gráfica PNG para el informe

### Orquestador (`main.py`)
- Coordina el flujo entre capas
- Inyección de dependencias
- Punto de entrada único

---

## Dependencias

```
pandas          # Lectura/manipulación de Excel
matplotlib      # Visualización gráfica
openpyxl        # Motor de lectura para .xlsx
pyinstaller     # Compilación a ejecutable
```

Instálalas con:
```bash
pip install -r requirements.txt
```

---

## Validación

Para verificar que el algoritmo funciona:

1. **Datos de entrada:** 25 años con datos válidos, 5 faltantes
2. **Sistema resultante:** Matriz tridiagonal 25×25
3. **Solución M:** Vector de 25 segundas derivadas
4. **Valores interpolados:** 5 números con 5 decimales cada uno
5. **Gráfica:** Curva suave que pasa por todos los puntos

---

## Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas
```

### Error: "File is not a zip file" (Windows)
Asegúrate de que Git LFS está configurado:
```bash
git lfs install
```

### La gráfica no aparece
Si usas SSH, asegúrate de que tienes un servidor X11 o usa WSL2 en Windows.

### El ejecutable en Windows se queda en negro
Corre desde CMD para ver los errores:
```cmd
cd "C:\ruta\al\ejecutable"
trazador-cubico.exe
```

---

## Notas Matemáticas

- El sistema es **bien condicionado** por ser tridiagonal
- Complejidad: **O(n)** para resolver, donde n es número de puntos
- Error de redondeo: controlado por eliminación gaussiana
- Continuidad: C² (segunda derivada continua)

---

## Autor

**Juan Bernardo Uribe**
- Curso: Análisis Numérico
- Universidad: Pontificia Universidad Javeriana
- Fecha: Mayo 2026

---

## Referencias

- Burden, R.L., Faires, J.D. (2015). *Numerical Analysis*. Cengage Learning.
- Spline interpolation: [Wikipedia](https://en.wikipedia.org/wiki/Spline_interpolation)
- [Documentación de pandas](https://pandas.pydata.org/)

---

## Licencia

Este proyecto es de carácter educativo para el curso de Análisis Numérico.

---

**Última actualización:** Mayo 21, 2026