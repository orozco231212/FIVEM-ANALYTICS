# Informe de diagnóstico y análisis descriptivo — FiveM Analytics

- **Proyecto:** análisis de actividad, economía virtual, retención y rendimiento en servidores de roleplay FiveM
- **Aprendiz:** David Alejandro Orozco Henao
- **Evidencia:** EV05. La referencia a EV06 en el título de la guía fue indicada como error del profesor.
- **Ejecución documentada:** 4 de noviembre de 2026
- **Entorno:** Python 3.15.2, Pandas 3.1.1, kernel `fivem-analytics`
- **Alcance:** nueve CSV sintéticos para representar tablas FiveM, más un dataset público de Kaggle sintético según su autor. Ninguno es telemetría real.

## 1. Pregunta y alcance de la respuesta

La pregunta del proyecto busca identificar actividades, trabajos y zonas de mayor concurrencia y explorar la relación entre el balance económico, la retención y el tiempo de juego.

Los archivos permiten ensayar esas operaciones y revisar la estructura relacional, pero fueron generados con reglas aleatorias y defectos sembrados. Por ello, los resultados cuantitativos de este informe describen **la simulación**, no una comunidad, un servidor, una economía ni un comportamiento de jugadores reales. La única fuente pública externa es el dataset de Kaggle, que tampoco es telemetría real.

## 2. Fuentes inspeccionadas

| Fuente | Contenido | Procedencia |
|---|---|---|
| Escenario sintético original | Sesiones, actividad, transacciones y snapshots simplificados. | `scripts/generar_datos_sinteticos.py`, semilla `20261104`. |
| Escenario sintético ampliado | Perfiles de jugadores, sesiones, movimientos, vehículos y métricas horarias. | Adaptación reproducible del generador de escenarios compartido, `scripts/generar_datasets_ampliados.py`, semilla `42`. Los identificadores se marcan `SIM_`. |
| Predict Online Gaming Behavior Dataset | Variables genéricas de comportamiento y engagement de videojuegos. | Descarga pública de Kaggle, versión 1, Rabie El Kharoua, CC BY 4.0. El autor declara que es sintético. Ver [atribución](../data/examples/kaggle/ATRIBUCION.md). |

Las fuentes FiveM se cargan desde `data/examples/fivem/` de forma recursiva. El Notebook convierte los campos identificadores a texto para conservar su precisión, los redacta en las muestras y no modifica los DataFrames originales. Las carpetas `data/raw/` no se usan para estos datos.

## 3. Diagnóstico estructural

| Archivo/DataFrame | Filas | Columnas | Hallazgo estructural principal |
|---|---:|---:|---|
| Actividad simplificada | 5.001 | 7 | Texto en las siete columnas; 1 zona vacía y 1 fila repetida. |
| Rendimiento simplificado | 1.441 | 7 | 4 variables numéricas y 3 de texto; faltantes y defectos sembrados. |
| Sesiones simplificadas | 5.001 | 8 | Duración como texto por valores heterogéneos; faltantes y duplicado. |
| Transacciones simplificadas | 12.397 | 8 | Importe como texto por anomalías; faltantes y duplicado. |
| Jugadores ampliados | 1.515 | 11 | 1.500 claves de jugador distintas; 15 registros completos añadidos como duplicados. |
| Rendimiento ampliado | 2.840 | 7 | Muestreo horario entre 2026-06-01 y 2026-09-28; cinco métricas numéricas. |
| Sesiones ampliadas | 8.000 | 10 | Sesiones desde 2026-06-01 hasta 2026-10-29, con actividad, zona y coordenadas. |
| Transacciones ampliadas | 12.000 | 7 | Importe mixto (numérico y texto), fechas y tipos de movimiento. |
| Vehículos ampliados | 2.200 | 9 | 10 modelos; faltantes de garaje/precio y valores fuera de rangos orientativos. |
| Kaggle: comportamiento de juego | 40.034 | 13 | Sin nulos ni duplicados exactos en la copia examinada; `PlayerID` único en las 40.034 filas. |

La salida completa de `shape`, columnas, tipos, `info()`, `describe()`, faltantes, duplicados y hallazgos queda en [salidas_notebook.md](salidas_notebook.md).

## 4. Hallazgos de calidad

Los límites siguientes son reglas exploratorias para comprobar el diagnóstico. Deben validarse con la documentación de un servidor y no son reglas universales de FiveM.

| Tabla | Hallazgos medidos en los CSV sintéticos | Tratamiento recomendado |
|---|---|---|
| `players.csv` | 15 filas completamente duplicadas (15 claves `player_id` repetidas); `discord_id`: 92 faltantes; `job`: 44 faltantes y 25 filas con `POLICE`; `last_seen`: 20 faltantes; 12 valores de `cash` negativos; 8 `bank` por encima de 100 millones; 6 `age_character` fuera de 18–100. | Resolver duplicados por clave/fecha y confirmar reglas del saldo y la edad; uniformar categorías solo sobre una copia de análisis. Tratar Discord ID como texto; no publicar identificadores. |
| `sessions.csv` | `disconnect_time`: 120 faltantes; `zone`: 150 faltantes; `duration_min`: 10 textos `unknown`, 40 negativos y 15 superiores a 720; 30 referencias a jugadores inexistentes. | Confirmar sesiones abiertas, validar duración contra conexión/desconexión y resolver referencias huérfanas antes de unir. No imputar zonas automáticamente. |
| `transactions.csv` | `amount`: 179 faltantes; `account`: 100 faltantes; 30 timestamps inválidos; 15 importes con formato `$1,500`; 50 importes de magnitud 1.000 millones; 40 filas con `type="Salary "` que requieren normalización. | Mantener el valor original, documentar parseos, revisar los importes extremos y confirmar el significado de signo y de `transfer`; usar columnas normalizadas derivadas sin sobrescribir el CSV. |
| `vehicles.csv` | `garage`: 433 faltantes; `price_paid`: 60 faltantes y 200 negativos; 35 valores de combustible mayores que 100; 25 `engine_health=-1`; 20 placas repetidas adicionales. | Confirmar unidades, modelos gratuitos, significado del estado del motor y política de placas duplicadas. El rango 0–100 de combustible es solo una hipótesis porcentual. |
| `server_performance.csv` ampliado | 69 `server_fps` y 69 `cpu_pct` faltantes; 15 FPS en cero; 10 CPUs en 400%; 19 conteos negativos de jugadores; 40 horas faltantes del muestreo esperado. | Validar la tasa de muestreo, instrumentación y unidades. No interpolar huecos ni atribuirlos a caídas reales: fueron sembrados en un generador. |
| Cuatro CSV simplificados | Se encontraron las anomalías controladas: faltantes, texto en duración/importe/memoria, fechas no interpretables, valores fuera de rango y un duplicado exacto por tabla. | Ver [tablas de hallazgos completas](salidas_notebook.md); los ejemplos no son evidencia de incidentes. |
| Kaggle | 40.034 filas, 13 columnas, sin faltantes ni duplicados exactos en la copia examinada. `EngagementLevel`: Medium 19.374, High 10.336, Low 10.324. | Mantener separado de FiveM: no comparte jugadores, identificadores ni definiciones operativas. La etiqueta de engagement no es retención longitudinal observada. |

La lectura de CSV sin tipo explícito puede convertir identificadores numéricos con faltantes en flotantes y perder precisión. El cargador del Notebook ahora impone tipo texto a nombres de columnas identificadoras antes de cargar los registros.

## 5. Resumen descriptivo de la simulación ampliada

Para este resumen se conservaron los CSV fuente sin modificar. Solo en copias temporales se normalizaron espacios/mayúsculas, se parsearon números y se excluyeron los registros señalados a continuación.

- **Sesiones:** 7.970 de 8.000 filas se enlazan con un jugador existente. Tras excluir duraciones no numéricas o fuera de 1–720 minutos, quedan 7.905 sesiones para los conteos de actividad/zona y medidas de duración.
- **Actividad:** entre las sesiones válidas, `police_patrol` aparece 1.024 veces, `drug_dealing` 1.012 y `mining` 1.009; la categoría `none` aparece 947 veces. Estos órdenes proceden de selecciones aleatorias del generador.
- **Zona:** 1.002 sesiones válidas están etiquetadas `Legion Square`; 924, `Sandy Shores`; 149 carecen de zona. Las coordenadas fueron generadas aleatoriamente y no se validaron contra el mapa; no se puede afirmar que una zona tenga más concurrencia real.
- **Repetición a 7 días:** 1.436 de 1.488 jugadores elegibles (96,5%) tuvieron otra sesión al menos siete días después de su primera sesión observada. Es una proxy del periodo sintético; no es una tasa real de retención ni churn.
- **Economía frente al tiempo:** tras retirar 50 valores extremos de 1.000 millones y parsear los importes con símbolo, la correlación descriptiva entre la suma firmada de transacciones y los minutos de sesión válidos por jugador es `-0,019` (1.487 jugadores emparejados). No muestra una asociación lineal apreciable en esta simulación y no permite concluir que la economía afecte la retención.
- **Concurrencia y FPS:** la correlación descriptiva entre jugadores concurrentes y FPS, después de excluir mediciones fuera de los límites orientadores, es `-0,815`. La fórmula del generador reduce FPS al aumentar la concurrencia; esto verifica el comportamiento programado, no mide el rendimiento de un servidor.
- **Rendimiento por recurso:** `heaviest_resource` se asigna aleatoriamente en el generador; sus promedios no identifican un cuello de botella ni permiten atribuir causalidad a un recurso.
- **Vehículos:** las frecuencias y medianas por modelo describen solo los valores aleatorios generados. Los 200 precios negativos y las métricas fuera de rango requieren revisión antes de cualquier total económico.

Kaggle no se unió a las tablas FiveM. Su población sintética es distinta y sus variables no bastan para responder la pregunta de retención de un servidor concreto.

## 6. Conclusiones y trabajo pendiente para resultados reales

El proyecto ya cuenta con un flujo reproducible para cargar, describir, revisar calidad, validar algunas relaciones entre tablas y resumir el escenario simulado. No se realizó limpieza destructiva, entrenamiento predictivo ni inferencia estadística; las fuentes no respaldan conclusiones sobre un servidor real.

Para afirmar resultados empíricos, se necesita una exportación autorizada y anonimizada, con diccionario de datos, unidades, zona horaria, reglas de ingresos/gastos, calendario de muestreo y claves de relación. Las fuentes reales deben mantenerse separadas en `data/raw/`, ejecutar el Notebook con `DATA_MODE="real"` y sustituir las conclusiones de simulación por resultados respaldados por esos archivos. No subir datos personales o privados al repositorio.
