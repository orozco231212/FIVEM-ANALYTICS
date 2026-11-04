# Preparación de las fuentes de datos

El Notebook usa por defecto cuatro CSV reproducibles del escenario simulado FiveM y un dataset público de Kaggle. El dataset de Kaggle está publicado bajo CC BY 4.0, pero su autor declara que es sintético. Ninguna de las dos fuentes es telemetría observada de un servidor FiveM real.

El generador `scripts/generar_datos_sinteticos.py` crea estas tablas de escenario:

- Sesiones con fechas, duración, empleo, zona y concurrencia máxima.
- Transacciones simuladas de ingresos y gastos.
- Eventos de actividad vinculados a sesiones.
- Muestreos simulados de jugadores conectados, FPS y consumo de recursos.

El archivo de Kaggle en `data/examples/kaggle/online_gaming_behavior_dataset.csv` aporta variables de engagement generales. Sus variables y población no corresponden a un servidor FiveM concreto. Sus metadatos están en `data/examples/kaggle/ATRIBUCION.md`.

Si en el futuro se obtiene una exportación real autorizada, coloca sus archivos CSV en:

```text
data/raw/
├── fivem/
│   ├── users.csv
│   ├── bank_statements.csv
│   └── ...
└── kaggle/
    └── archivos_del_dataset_seleccionado.csv
```

Los nombres anteriores son ejemplos de tablas, no indican que esos archivos se hayan recibido ni que existan en todos los frameworks. Agrega solo las tablas disponibles y pertinentes a la pregunta. El Notebook examina cada CSV de forma independiente, también dentro de subcarpetas.

## Variables orientadoras del proyecto

De acuerdo con EP 2, identifica qué archivos contienen, cuando estén disponibles:

- Hora de conexión/desconexión o duración de sesión.
- Transacciones con fecha, tipo/categoría y valor; confirma si los signos representan ingresos, gastos o reversos.
- Trabajo, actividad, recurso o evento asociado al jugador.
- Coordenadas X, Y, Z para analizar zonas, si la fuente las registra.
- Métricas de servidor como tickrate, FPS o consumo por recurso, si txAdmin/logs las proveen.
- Para Kaggle: sesiones, tiempo de juego, engagement y definición de retención/abandono.

No presupongas que todos esos campos existen. Registra el esquema real y la procedencia de cada archivo en el informe. La comparación con Kaggle requiere comprobar que las definiciones, unidades, periodos y poblaciones sean compatibles.

## Exportación y privacidad

1. Exporta desde MySQL/MariaDB únicamente las columnas y el periodo necesarios para el análisis. No conectes el Notebook a producción.
2. Sustituye o elimina Steam ID, Discord ID, license, citizen ID, tokens y cualquier dato que permita identificar a una persona. Conserva una clave anónima consistente solo si es indispensable para relacionar tablas.
3. Para Kaggle, registra el nombre exacto, URL, autor, licencia, versión/fecha de descarga y archivos seleccionados en el informe.
4. Comprueba los permisos y las condiciones de uso de ambas fuentes. No subas información privada o restringida a GitHub.
5. Los archivos de `data/raw/` están ignorados por Git. No fuerces su inclusión en commits.

Formato de entrada admitido por el Notebook: `.csv`. Exporta bases de datos a CSV con encabezados o adapta y documenta explícitamente el cargador antes de incorporar otro formato.
