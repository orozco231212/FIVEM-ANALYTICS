# FiveM Analytics: preparación y análisis de datos

Proyecto de ciencia de datos sobre servidores de roleplay de FiveM GTA V. Esta entrega diagnóstica un escenario FiveM simulado y un dataset público de Kaggle que su autor también declara sintético. El informe documenta los resultados de esas fuentes; no son hallazgos de un servidor real.

> **Alcance de los datos:** no se dispone de un servidor propio. Los nueve CSV FiveM son simulaciones reproducibles, no registros de un servidor real. El archivo público de Kaggle también es sintético según su autor. Los resultados sirven para practicar el flujo de análisis, no para afirmar cómo se comporta una comunidad real. Consulta [data/examples/README.md](data/examples/README.md).
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
| Escenario FiveM simulado | Practicar diagnóstico y análisis descriptivo de jugadores, sesiones, economía, vehículos, actividad y rendimiento. | Nueve CSV reproducibles en `data/examples/fivem/`, generados por dos scripts; todas las tablas y anomalías son sintéticas. |
| Kaggle: Predict Online Gaming Behavior Dataset | Comparar variables generales de engagement y hábitos de juego con el escenario FiveM. | CSV público en `data/examples/kaggle/`; versión 1. La ficha de Kaggle lo identifica explícitamente como sintético, no como telemetría real. |

**Fuente Kaggle y atribución:** Rabie El Kharoua, [Predict Online Gaming Behavior Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset), versión 1, licencia CC BY 4.0, última actualización indicada por Kaggle: 21-06-2024. Kaggle advierte que el dataset es sintético y generado con fines educativos. La descarga aporta una referencia pública; no convierte sus registros en datos reales de FiveM.

Consulta [data/README.md](data/README.md) para entender las fuentes. Los datos privados se excluyen de Git por defecto. Los CSV del escenario FiveM se regeneran con semilla fija; el CSV público de Kaggle se incluye con su atribución para que el Notebook funcione tras clonar el repositorio.

## Estructura

```text
fivem-analytics/
├── data/
│   ├── examples/ (fuentes sintéticas y Kaggle)
│   ├── raw/ (datos originales autorizados; no versionar)
│   └── processed/ (CSV limpios y tablas de análisis)
├── notebooks/
│   ├── data_quality.ipynb
│   ├── diagnostico_calidad.ipynb (nombre histórico)
│   └── data_preparation.ipynb
├── reports/
│   ├── data_quality.md
│   ├── informe_diagnostico.md
│   └── salidas_notebook.md
├── scripts/
│   ├── generar_datos_sinteticos.py
│   └── generar_datasets_ampliados.py
├── tests/
│   ├── test_generar_datos_sinteticos.py
│   └── test_generar_datasets_ampliados.py
├── .vscode/
│   └── settings.json
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

## Regenerar los datos sintéticos

Desde la raíz, ejecuta los dos generadores. El primero crea las cuatro tablas demostrativas originales y el segundo genera las cinco tablas relacionales ampliadas dentro de `data/examples/fivem/`; ninguno escribe datos a `data/raw/`.

```powershell
python scripts/generar_datos_sinteticos.py
python scripts/generar_datasets_ampliados.py
```

Ambos generadores usan semillas fijas. Para ejecutar la evidencia en VS Code, abre `notebooks/diagnostico_calidad.ipynb`, elige el kernel **Python (fivem-analytics .venv)** y ejecuta todas las celdas. El Notebook inspecciona automáticamente los CSV dentro de las subcarpetas de cada fuente, conserva los DataFrames originales y redacta identificadores en las muestras.

## Preparación de datos EV07

Ejecuta `notebooks/data_preparation.ipynb` desde la raíz del repositorio después de regenerar los datos ampliados. El Notebook conserva las fuentes bajo `data/examples/fivem/expanded/`, compara calidad antes/después, elimina solo duplicados exactos, estandariza categorías, convierte fechas y números y deja como faltantes los valores que no se pueden interpretar o validar. No imputa campos desconocidos.

El análisis aplica filtros de duración y referencias válidas, resume sesiones por actividad, trabajo y zona, calcula indicadores de juego y crea una fila por jugador mediante agregaciones de sesiones y transacciones con uniones validadas. La repetición a 7 días es una proxy con observación suficiente, no retención medida de un servidor real. Vehículos y rendimiento se exportan por separado porque no hay una relación analítica que justifique unirlos con sesiones. Todas las cifras describen únicamente la simulación sintética.

El Notebook genera en `data/processed/` los perfiles, sesiones, transacciones, vehículos y métricas de rendimiento limpios, tres resúmenes (`sessions_by_activity.csv`, `sessions_by_job.csv` y `sessions_by_zone.csv`), la tabla consolidada `player_analysis.csv` y `quality_comparison.csv`. Los perfiles exportados omiten `license`, `discord_id` y `username`; el `player_id` retenido es una clave ficticia de relación. Revisa [reports/data_quality.md](reports/data_quality.md) para el tratamiento y sus límites.

El diagnóstico anterior permanece disponible en `notebooks/diagnostico_calidad.ipynb` y `reports/informe_diagnostico.md`; `notebooks/data_quality.ipynb` conserva el nombre solicitado por la estructura de entrega.

Para analizar fuentes reales autorizadas, colócalas en `data/raw/fivem/` y `data/raw/kaggle/` y cambia `DATA_MODE` a `"real"`. No mezcles datos sintéticos con exportaciones reales como si tuvieran la misma procedencia.

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

El informe correspondiente está en [reports/informe_diagnostico.md](reports/informe_diagnostico.md). Sus conclusiones se refieren solamente a los escenarios sintéticos y al dataset de Kaggle (que también es sintético); no describen un servidor real.

Las salidas completas de todas las celdas del Notebook, ejecutadas con los archivos disponibles, están en [reports/salidas_notebook.md](reports/salidas_notebook.md). Es una captura textual independiente; el Notebook se mantiene sin resultados guardados para evitar muestras accidentales.

## Flujo Git

Para este incremento, crea la rama desde `develop` actualizada y publica únicamente la rama de trabajo:

Usa `feature/project-data-preparation` para este trabajo. Cuando `develop` esté disponible en el remoto, actualízala antes de crear futuras ramas:

```powershell
git fetch origin
git switch develop
git pull --ff-only origin develop
git switch -c feature/<topic>
```

Para registrar los hitos de esta evidencia, usa los mensajes `feat: clean and standardize project data`, `feat: implement data filtering and aggregation`, `feat: prepare and validate processed datasets` y `docs: update project README` en los commits que correspondan a cada cambio. Publica la rama con `git push -u origin feature/project-data-preparation`.

Fusiona la rama publicada con `develop` solo después de validar la ejecución y revisar que ningún dato privado se incluya. Mantén las fuentes autorizadas en `data/raw/`; nunca las fuerces al control de versiones.

Convenciones:

- `main`: versión estable y entregable.
- `develop`: integración del trabajo.
- `feature/ev05-diagnostico-calidad`: diagnóstico de calidad anterior.
- `feature/project-data-preparation`: preparación, análisis y exportación de los datasets procesados.

Para futuros incrementos se pueden usar nombres como `feature/fivem-data-export`, `feature/kaggle-dataset`, `feature/player-retention` y `feature/economy-analysis`. Usa mensajes de commit descriptivos. No publiques datasets reales en ramas ni commits.

## Lista antes de entregar

- [x] Identificar la evidencia como EV05; la mención a EV06 en el título de la guía es un error del profesor, según la aclaración del aprendiz.
- [x] Identificar el dataset público de Kaggle, registrar su autor, URL, versión y licencia, y advertir que es sintético.
- [x] Crear y documentar nueve CSV reproducibles para perfiles, sesiones, economía, actividades, vehículos y rendimiento; distinguirlos de telemetría observada.
- [x] Validar referencias entre jugadores, sesiones, transacciones y vehículos, y documentar el análisis descriptivo de la simulación.
- [x] Ejecutar el Notebook con kernel `.venv` sobre las diez tablas disponibles y generar un archivo separado con todas las salidas.
- [ ] Si posteriormente se obtiene acceso a un servidor, añadir exportaciones autorizadas y anonimizadas antes de afirmar resultados reales.
- [x] Documentar dimensiones, tipos, faltantes, duplicados, anomalías sembradas, relaciones y límites en el informe.
- [x] Mantener el Notebook sin salidas guardadas; las muestras visibles redactan las columnas identificadoras.
- [ ] Ejecutar el Notebook en VS Code y revisar visualmente sus tablas antes de la entrega final.
- [ ] Confirmar que Git no incluya datos privados.
- [ ] Publicar el repositorio y entregar su URL en Classroom.
