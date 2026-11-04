# Informe técnico: diagnóstico inicial de calidad de datos

**Proyecto:** Análisis de rendimiento, retención de jugadores y economía virtual en servidores de roleplay de FiveM GTA V  
**Aprendiz:** David Alejandro Orozco Henao  
**Evidencia:** EV05. La mención a EV06 en el título interno de la guía es un error del profesor, según la aclaración del aprendiz.  
**Fecha de ejecución:** 4 de noviembre de 2026  
**Entorno validado:** Python 3.15.2, Pandas 3.1.1  
**Alcance:** escenario FiveM generado con semilla `20261104` y dataset público de Kaggle. El autor del dataset de Kaggle lo declara sintético. No hay observaciones de un servidor real.

## 1. Propósito y pregunta analítica

El proyecto busca explorar cómo se relacionan la actividad de los jugadores, el rendimiento del servidor y la economía virtual para orientar decisiones sobre los sistemas de juego y la experiencia de la comunidad.

**Pregunta:** ¿Cuáles son las actividades, trabajos y zonas del mapa con mayor concurrencia de jugadores dentro del servidor de FiveM, y cómo influye el balance económico (ingresos vs. gastos virtuales) en la retención y tiempo promedio de juego diario de la comunidad?

## 2. Fuentes seleccionadas y disponibilidad

| Fuente | Contenido y uso | Archivos inspeccionados | Procedencia |
|---|---|---|---|
| Escenario de servidor FiveM | Sesiones, economía virtual, actividades y snapshots de concurrencia/rendimiento, según las variables propuestas en EP 2. | `sesiones_fivem_sinteticas.csv`, `transacciones_economicas_sinteticas.csv`, `actividad_jugadores_sintetica.csv` y `rendimiento_servidor_sintetico.csv`. | Generado para esta evidencia; no se extrajo de un servidor ni representa personas reales. |
| Predict Online Gaming Behavior Dataset | Variables tabulares de juego y engagement como referencia general de análisis de jugadores. | `data/examples/kaggle/online_gaming_behavior_dataset.csv`. | Descarga pública de Kaggle, versión 1. Rabie El Kharoua, CC BY 4.0. El autor indica expresamente que los registros son sintéticos. |

El escenario FiveM se genera mediante `scripts/generar_datos_sinteticos.py`, con 350 identificadores ficticios `SIM_PLAYER_*`, 5.000 sesiones base durante 60 días (más una fila duplicada), transacciones, eventos y snapshots horarios. Se sembraron algunos defectos a propósito para comprobar las operaciones de diagnóstico. Los resultados describen el comportamiento del generador y de la copia local del dataset de Kaggle, no un servidor o población real.

**Referencia Kaggle:** [ficha del dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset), versión 1, licencia CC BY 4.0, última actualización indicada por Kaggle: 21-06-2024. Atribución completa: [data/examples/kaggle/ATRIBUCION.md](../data/examples/kaggle/ATRIBUCION.md). La ficha declara que es sintético y educativo.

## 3. Diagnóstico estructural

Las dimensiones, tipos y conteos siguientes son salida de la ejecución de todas las celdas del Notebook sobre los archivos disponibles. Pandas 3.1.1 representa texto con dtype `str`; en versiones de Pandas 2.x puede mostrarse como `object`. Ambos indican columnas de texto en estos CSV.

| Archivo/DataFrame | Filas | Columnas | Tipos de datos | Observaciones |
|---|---:|---:|---|---|
| Actividades FiveM simuladas | 5.001 | 7 | `str` (7) | Eventos sintéticos vinculados a sesiones; una zona faltante y un duplicado exacto. |
| Rendimiento FiveM simulado | 1.441 | 7 | `str` (3), `int64` (2), `float64` (2) | Snapshots horarios; faltante en FPS, texto no numérico en memoria, CPU fuera del rango porcentual y duplicado. |
| Sesiones FiveM simuladas | 5.001 | 8 | `str` (7), `int64` (1) | Duración inferida como texto por la palabra `noventa`; un valor faltante y un duplicado. |
| Transacciones FiveM simuladas | 12.397 | 8 | `str` (8) | El importe queda como texto por la anomalía `sin_dato`; un importe faltante y un duplicado. |
| Kaggle: comportamiento de juego | 40.034 | 13 | `str` (5), `int64` (7), `float64` (1) | Edad, género, ubicación, género de juego, tiempo, compras, sesiones, nivel, logros y engagement. Sin faltantes ni filas completas duplicadas. |

Las columnas de trabajo, zona, actividad y concurrencia están presentes para practicar análisis posteriores. Este informe se limita al diagnóstico de calidad y no presenta rankings de popularidad como hallazgos sobre una comunidad.

## 4. Hallazgos de calidad basados en evidencia

| Dataset/archivo | Problema identificado | Evidencia encontrada | Posible impacto | Acción propuesta |
|---|---|---|---|---|
| Actividades simuladas | 1 zona faltante y 1 fila duplicada. | `zone`: 5.000 valores no nulos de 5.001; `dataframe.duplicated()` = 1. | Una zona desconocida afecta la clasificación geográfica; una repetición puede sobrecontar actividad. Ambas condiciones fueron sembradas. | Revisar el evento de origen y su clave; no eliminar duplicados sin confirmar que no sean eventos válidos. |
| Rendimiento simulado | 1 FPS faltante, 1 CPU fuera de rango, 1 texto no numérico en memoria y 1 duplicado. | `server_fps`: 1.440/1.441 presentes; `cpu_percent` máximo 145 (regla exploratoria 0–100); `memory_percent="sin_dato"`; 1 fila duplicada. | Impide resumir el intervalo faltante; un porcentaje >100 y una cadena requieren validar definición/unidad; el duplicado puede sesgar estadísticas. | Verificar procedencia/unidad de cada métrica; tratar faltantes, convertir tipos y revisar duplicados solo con regla del dominio. |
| Sesiones simuladas | 1 duración faltante, 1 texto no numérico, 1 duración negativa, 1 fecha inválida y 1 duplicado. | `duration_minutes`: 5.000/5.001 presentes; valor `noventa`; duración `-8`; `disconnected_at="fecha_invalida"`; 1 fila completa duplicada. | Puede distorsionar duración promedio, secuencia temporal y conteo de sesiones. Los defectos fueron sembrados deliberadamente. | Parsear fecha/duración con formato explícito, verificar hora de desconexión y reglas de sesión; documentar el efecto antes de excluir/imputar. |
| Transacciones simuladas | 1 importe faltante, 1 texto no numérico, 1 importe negativo y 1 duplicado. | `amount`: 12.396/12.397 presentes; valor `sin_dato`; importe `-250`; 1 fila duplicada. | Afecta sumas de ingresos/gastos y balance. La simulación usa `transaction_type` para distinguir ingreso/gasto; el valor negativo se sembró deliberadamente como anomalía. | Confirmar convención de signos, corregir/conservar el valor con trazabilidad y revisar duplicados por `transaction_id`. |
| Kaggle público (sintético del autor) | No se observan valores faltantes ni duplicados exactos; revisar la limitación de representatividad y el alcance de `EngagementLevel`. | 40.034 filas; 40.034 `PlayerID` distintos; categorías de engagement: Medium 19.374, High 10.336, Low 10.324. | No representa FiveM; no contiene economía virtual, trabajos ni zonas del servidor. `EngagementLevel` no equivale por sí solo a retención real observada. No debe unirse con tablas FiveM por identificador. | Usar solo como referencia exploratoria separada; atribuir la fuente y describir sus variables sintéticas y límites. |

El Notebook también observa los rangos del archivo Kaggle: edad 15–49, horas de juego 0–24, sesiones por semana 0–19, duración promedio 10–179 minutos, nivel 1–99 y logros 0–49. Son estadísticas de la distribución sintética publicada, no límites universales de calidad.

## 5. Aspectos a validar durante la interpretación

- **Valores faltantes:** se identificaron en zonas, FPS, duración de sesión y monto de transacción dentro del escenario. Se debe valorar su impacto por variable antes de decidir un tratamiento.
- **Tipos:** las columnas con texto inesperado (`noventa`, `sin_dato`) hacen que las columnas completas se carguen como texto. La fecha `fecha_invalida` tampoco puede convertirse a fecha/hora.
- **Posibles inconsistencias:** duración negativa, CPU de 145% y monto negativo activan reglas exploratorias. Se verifican contra el dominio; no se corrigen automáticamente.
- **Duplicados:** el generador incluye una fila duplicada exacta en cada una de las cuatro tablas FiveM. `duplicated()` no demuestra por sí solo que un evento real sea erróneo; comparar la clave y la regla de negocio.
- **Cobertura/comparabilidad:** el Kaggle es de videojuegos generales y no comparte comunidad, periodo, identificadores, trabajos, zonas ni economía con el escenario FiveM. No se pueden relacionar las filas ni inferir causas de retención con esta combinación.
- **Privacidad/licencia:** los identificadores FiveM son ficticios y los identificadores de Kaggle proceden de su dataset sintético. La fuente pública se mantiene con la atribución CC BY 4.0.

## 6. Limpieza y preparación propuestas

No se ejecuta limpieza completa, tal como indica la guía. Para preparar datos de una futura fuente observada, se propone:

1. Comprobar fechas y duraciones contra la exportación y convertir con formato explícito; separar fallos de parseo.
2. Confirmar la convención de signos de transacciones y la unidad de cada monto antes de agregar ingresos y gastos.
3. Investigar valores faltantes y determinar si corresponde recuperarlos, excluirlos o dejarlos sin imputación.
4. Verificar filas duplicadas mediante identificadores y reglas del evento; no borrar solo por coincidencia de todas las columnas.
5. Validar métricas porcentuales y rangos de sesiones con el esquema del servidor y la definición original de cada variable.
6. Mantener el Kaggle como dataset de referencia independiente; no combinarlo con FiveM como si PlayerID representara al mismo jugador.

## 7. Conclusiones

El Notebook carga e inspecciona de manera reproducible cinco DataFrames y detecta las anomalías incluidas en el escenario, mientras confirma que el CSV público de Kaggle no tiene faltantes ni duplicados completos en la copia revisada. Las anomalías de FiveM fueron sembradas; no se deben presentar como incidencias de un servidor. El dataset de Kaggle es una fuente pública y atribuida, pero también sintética según su autor. Ninguna de las dos fuentes permite concluir cómo se comporta una comunidad real ni inferir causalidad entre economía y retención.

La pregunta original menciona zonas, concurrencia, balance económico y retención. El escenario ayuda a probar esas variables, pero Kaggle no tiene los mismos jugadores ni un indicador longitudinal de retención, y los snapshots/eventos simulados no equivalen a telemetría operativa. Para conclusiones reales se requiere permiso/acceso a un servidor o cambiar explícitamente el alcance con el instructor para aceptar un caso simulado.
