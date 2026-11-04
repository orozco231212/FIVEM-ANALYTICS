# FiveM Analytics: diagnóstico inicial de calidad de datos

Proyecto de ciencia de datos sobre servidores de roleplay de FiveM GTA V. Esta entrega diagnóstica un escenario FiveM simulado y un dataset público de Kaggle que su autor también declara sintético. El informe documenta los resultados de esas fuentes; no son hallazgos de un servidor real.

> **Alcance de los datos:** no se dispone de un servidor propio. Los cuatro archivos FiveM son una simulación reproducible, no registros de un servidor real. El archivo público de Kaggle sí fue descargado, pero su autor también lo identifica como sintético. Se puede diagnosticar el caso simulado; no debe afirmarse que sus resultados describan una comunidad real. Consulta [data/examples/README.md](data/examples/README.md).
>
> **Identificación de la evidencia:** esta entrega corresponde a **EV05**. El título interno de la guía y la mención a EV06 son un error del profesor, según la aclaración del aprendiz.

## Proyecto y pregunta analítica

**Nombre:** Análisis de rendimiento, retención de jugadores y economía virtual en servidores de roleplay de FiveM GTA V.

**Propósito:** explorar la relación entre la actividad de los jugadores, el rendimiento del servidor y los movimientos de la economía virtual, para orientar mejoras en los sistemas de juego, la experiencia de la comunidad y el balance económico.

**Pregunta analítica:** ¿Cuáles son las actividades, trabajos y zonas del mapa con mayor concurrencia de jugadores dentro del servidor de FiveM, y cómo influye el balance económico (ingresos vs. gastos virtuales) en la retención y tiempo promedio de juego diario de la comunidad?

**Variables que orientan la recopilación:** fecha/hora de conexión y desconexión, duración de sesión, movimientos económicos, actividad/trabajo o recurso ejecutado, ubicación (X, Y, Z) y, cuando estén disponibles, métricas de rendimiento como tickrate, FPS y consumo de CPU/RAM. EP 2 también propone un identificador de jugador; debe anonimizarse y no publicarse en claro.

## Fuentes definidas en EP 3

| Fuente | Uso previsto | Estado en el repositorio |
|---|---|---|
| Escenario FiveM simulado | Examinar sesiones, economía, actividades y rendimiento como si provinieran de exportaciones de un servidor. | Cuatro CSV reproducibles en `data/examples/fivem/`; contienen datos inventados y anomalías sembradas para diagnosticar. |
| Kaggle: Predict Online Gaming Behavior Dataset | Comparar variables generales de engagement y hábitos de juego con el escenario FiveM. | CSV público en `data/examples/kaggle/`; versión 1. La ficha de Kaggle lo identifica explícitamente como sintético, no como telemetría real. |

**Fuente Kaggle y atribución:** Rabie El Kharoua, [Predict Online Gaming Behavior Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset), versión 1, licencia CC BY 4.0, última actualización indicada por Kaggle: 21-06-2024. Kaggle advierte que el dataset es sintético y generado con fines educativos. La descarga aporta una referencia pública; no convierte sus registros en datos reales de FiveM.

Consulta [data/README.md](data/README.md) para entender las fuentes. Los datos privados se excluyen de Git por defecto. Los CSV del escenario FiveM se regeneran con semilla fija; el CSV público de Kaggle se incluye con su atribución para que el Notebook funcione tras clonar el repositorio.

## Estructura

```text
fivem-analytics/
├── data/
│   ├── README.md
│   ├── examples/
│   │   ├── fivem/ (datos simulados)
│   │   └── kaggle/ (dataset público sintético)
│   └── raw/
│       ├── fivem/
│       └── kaggle/
├── notebooks/
│   └── diagnostico_calidad.ipynb
├── reports/
│   └── informe_diagnostico.md
├── scripts/
│   └── generar_datos_sinteticos.py
├── tests/
│   └── test_generar_datos_sinteticos.py
├── run_nb.py
├── .gitignore
└── requirements.txt
```

## Preparar el entorno en Windows

Desde PowerShell, en la raíz del proyecto:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name fivem-analytics --display-name "Python (fivem-analytics .venv)"
code .
```

En VS Code, abre el Notebook y selecciona el kernel **Python (fivem-analytics .venv)**. La configuración del workspace establece `.venv` como intérprete predeterminado; registrar el kernel permite seleccionarlo explícitamente desde el Notebook. No elijas el Python global si no tiene instaladas las dependencias del proyecto.

### Si VS Code muestra que falta `ipykernel`

Si aparece el cuadro **“La ejecución de celdas con Python 3.15.2 requiere el paquete ipykernel”**, pulsa **Cambiar Kernel** en ese cuadro. En el selector del Notebook, elige **Python (fivem-analytics .venv)** (o **Seleccionar otro kernel → Entornos de Python → `.venv\Scripts\python.exe`**). Después reinicia el kernel y vuelve a ejecutar las celdas. No es necesario instalar `ipykernel` en el Python global: ya está incluido en `requirements.txt` y en `.venv`.

## Validación automatizada del Notebook

Para ejecutar todas las celdas del Notebook sin abrir Jupyter, desde la raíz del proyecto:

```powershell
python run_nb.py
```

El script informa `OK` por celda y termina con `Notebook ejecutado correctamente.` si no hay errores. Los archivos auxiliares de salida no se versionan.

Para regenerar los cuatro archivos del escenario simulado, desde la raíz ejecuta:

```powershell
python scripts/generar_datos_sinteticos.py
```

El generador usa una semilla fija para que el escenario sea reproducible. En VS Code, instala/activa las extensiones Python y Jupyter, abre `notebooks/diagnostico_calidad.ipynb`, elige el kernel **Python (fivem-analytics .venv)** y ejecuta todas las celdas. Para inspeccionar fuentes seleccionadas del proyecto, coloca la exportación FiveM autorizada y anonimizada en `data/raw/fivem/`, el dataset de referencia en `data/raw/kaggle/` y cambia `DATA_MODE` a `"real"` en la celda de configuración. No llames reales a registros sintéticos ni combines poblaciones no comparables.

El proyecto trabaja con archivos CSV. Si alguno usa un delimitador distinto de coma o una codificación especial, ajusta los argumentos de `pd.read_csv` en el Notebook y documenta el cambio; no se adivina ni se transforma el contenido en silencio. Los problemas de carga se muestran con el archivo que los produjo. Para ejecutar la prueba del generador:

```powershell
python -m unittest discover -s tests
```

## Qué documenta el diagnóstico

Para cada archivo cargado, el Notebook registra o muestra:

- `head()` y `tail()` para inspeccionar muestras de inicio y final.
- `shape`, `columns`, `dtypes` e `info()` para describir estructura y tipos.
- `describe()` para variables numéricas y `describe(include='object')` cuando haya columnas `object`.
- Cantidad y porcentaje de valores faltantes por columna y cantidad de filas duplicadas.
- Notas de interpretación y preguntas de validación semántica. Los duplicados o valores atípicos no se eliminan automáticamente: se documentan y se decide su tratamiento con conocimiento del dominio.

El informe correspondiente está en [reports/informe_diagnostico.md](reports/informe_diagnostico.md). Sus conclusiones se refieren solamente al escenario sintético y al dataset de Kaggle (que también es sintético); no describen un servidor real.

Las salidas completas de todas las celdas del Notebook, ejecutadas con los archivos disponibles, están en [reports/salidas_notebook.md](reports/salidas_notebook.md). Este archivo es una captura textual independiente; no modifica ni guarda salidas dentro del Notebook.

## Flujo Git

El repositorio remoto indicado (`orozco231212/FIVEM-ANALYTICS`) estaba vacío al preparar esta estructura y la carpeta de trabajo no tenía un historial Git disponible. Para iniciar Git Flow con el primer incremento, ejecuta desde la raíz del proyecto:

```powershell
git init -b main
git remote add origin https://github.com/orozco231212/FIVEM-ANALYTICS.git
git switch -c develop
git switch -c feature/ev05-diagnostico-calidad
git add .gitignore README.md requirements.txt data notebooks reports scripts tests
git commit -m "feat: add EV05 FiveM data quality diagnosis"
git switch develop
git merge --no-ff feature/ev05-diagnostico-calidad
git push -u origin develop
git switch main
git merge --no-ff develop
git push -u origin main
git push -u origin feature/ev05-diagnostico-calidad
```

Después de esta entrega, crea cada incremento desde `develop` con `git switch -c feature/<tema>`. Antes de integrar, valida el Notebook con los datos autorizados y completa el informe. No incluyas archivos privados ni fuerces su inclusión en Git.

Convenciones:

- `main`: versión estable y entregable.
- `develop`: integración del trabajo.
- `feature/ev05-diagnostico-calidad`: implementación de esta evidencia; crear otras ramas `feature/<tema>` para nuevos incrementos.

Para futuros incrementos se pueden usar nombres como `feature/fivem-data-export`, `feature/kaggle-dataset`, `feature/player-retention` y `feature/economy-analysis`. Usa mensajes de commit descriptivos. No publiques datasets reales en ramas ni commits.

## Lista antes de entregar

- [x] Identificar la evidencia como EV05; la mención a EV06 en el título de la guía es un error del profesor, según la aclaración del aprendiz.
- [x] Identificar el dataset público de Kaggle, registrar su autor, URL, versión y licencia, y advertir que es sintético.
- [x] Crear datasets reproducibles para sesiones, transacciones, actividades y rendimiento FiveM; distinguirlos de telemetría observada.
- [x] Ejecutar y documentar el diagnóstico del escenario sintético.
- [ ] Si posteriormente se obtiene acceso a un servidor, añadir exportaciones autorizadas y anonimizadas antes de afirmar resultados reales.
- [x] Validar las celdas del Notebook sobre los CSV disponibles y documentar dimensiones, tipos, faltantes, duplicados, anomalías sembradas, impactos y límites en el informe.
- [ ] Ejecutar el Notebook con el kernel `.venv` en VS Code antes de la entrega final y revisar visualmente sus tablas.
- [ ] Revisar que el Notebook no guarde muestras sensibles en sus salidas y que Git no incluya datos privados.
- [ ] Publicar el repositorio y entregar su URL en Classroom.
