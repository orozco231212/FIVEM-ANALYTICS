# Preparación y calidad de datos — EV07

## Alcance y procedencia

La preparación se ejecutó sobre las cinco tablas de `data/examples/fivem/expanded/`, generadas de forma determinista con semilla `42`. Son datos sintéticos con anomalías sembradas; no son exportaciones observadas de FiveM. `data/raw/` permanece sin modificaciones y no contiene una fuente real para esta actividad. El diagnóstico previo se conserva en [informe_diagnostico.md](./informe_diagnostico.md).

## Comparación antes y después

La comparación de celdas vacías se calcula sobre las columnas de cada tabla antes de exportar. Los aumentos se deben a fechas o valores numéricos ilegibles y valores fuera de los límites exploratorios, que se convierten en faltantes en vez de imputarse. No se eliminan filas por esas conversiones.

| Dataset | Filas antes | Filas después | Columnas | Celdas vacías antes | Celdas vacías después | Duplicados exactos retirados |
|---|---:|---:|---:|---:|---:|---:|
| `players` | 1.515 | 1.500 | 11 | 156 | 160 | 15 |
| `sessions` | 8.000 | 8.000 | 10 | 270 | 280 | 0 |
| `transactions` | 12.000 | 12.000 | 7 | 279 | 309 | 0 |
| `vehicles` | 2.200 | 2.200 | 9 | 493 | 753 | 0 |
| `server_performance` | 2.840 | 2.840 | 7 | 138 | 182 | 0 |

Se eliminaron únicamente las 15 filas de perfil completamente idénticas. Los valores ausentes se mantienen como tales; no se imputaron trabajos, zonas, fechas, importes ni mediciones. Las columnas simuladas `license`, `discord_id` y `username` se omiten del CSV de perfiles procesados. La clave ficticia `player_id` se conserva para poder relacionar tablas.

Las reglas de elegibilidad para cada análisis se limitan a ese cálculo: duración de sesión de 1–720 minutos, fecha de conexión interpretable y jugador presente; importes interpretables con magnitud inferior a 100 millones y fecha válida; y métricas de rendimiento dentro de rangos orientativos. Los extremos de transacciones y los límites no son reglas contables ni operativas de un servidor real. Se detectaron 30 referencias a jugadores inexistentes en sesiones; se excluyeron de las métricas que requieren perfil.

## Indicadores descriptivos de la simulación

De 8.000 sesiones fuente, 7.905 cumplen las condiciones usadas para los resúmenes. La actividad con más sesiones es `police_patrol` (1.024), seguida de `drug_dealing` (1.012) y `mining` (1.009). El trabajo con más sesiones asociadas es `unemployed` (1.686); la zona observada más frecuente es `Legion Square` (1.002). Cada indicador cuenta registros sintéticos del generador, no concurrencia observada simultáneamente ni comportamiento de una comunidad.

La tabla de jugadores contiene 1.500 perfiles únicos y agrega sesiones y transacciones mediante uniones con validación de cardinalidad. La proxy de repetición a 7 días es 96,5% entre 1.488 jugadores con una ventana mínima de observación de siete días. La ventana y el generador sintético limitan su interpretación: no equivale a retención real.

La economía se resume como ingresos y gastos según el signo asignado por el generador; el neto firmado se contrasta descriptivamente con minutos de juego mediante correlación de Spearman (`-0,004` en esta ejecución). No se interpreta como efecto causal. La pregunta de influencia económica sobre retención requiere datos longitudinales reales, definiciones validadas de ingresos/gastos y control de otros factores.

## Estructuración y archivos generados

`notebooks/data_preparation.ipynb` contiene el pipeline reutilizable con `pipe()`, filtros, agregaciones, validaciones y exportación. Se mantienen por separado vehículos y rendimiento: no hay una clave temporal de evento que permita unir el rendimiento con sesiones sin fabricar una relación.

Los diez CSV generados en `data/processed/` son:

- `players_clean.csv`, `sessions_clean.csv`, `transactions_clean.csv`, `vehicles_clean.csv` y `server_performance_clean.csv`.
- `sessions_by_activity.csv`, `sessions_by_job.csv` y `sessions_by_zone.csv`.
- `player_analysis.csv`, una fila por `player_id` con indicadores de perfil, sesiones, economía y proxy de recurrencia.
- `quality_comparison.csv`, con las dimensiones, faltantes y duplicados antes/después.

El Notebook comprueba claves únicas, rangos usados en filtros, cardinalidades de las uniones, conservación de perfiles y cantidades exportadas. Los datos procesados siguen describiendo exclusivamente la simulación. Para conclusiones sobre un servidor se requieren exportaciones autorizadas y anonimizadas con diccionario de datos, unidades, periodo y reglas de negocio documentadas.
