# Datos sintéticos de demostración

Los archivos de `fivem/` se generan para representar un escenario de servidor FiveM y practicar el diagnóstico:

- `fivem/sesiones_fivem_sinteticas.csv`: sesiones sintéticas de jugadores anonimizados ficticios.
- `fivem/transacciones_economicas_sinteticas.csv`: ingresos/gastos simulados asociados a jugadores y trabajos.
- `fivem/actividad_jugadores_sintetica.csv`: eventos simulados vinculados a sesiones.
- `fivem/rendimiento_servidor_sintetico.csv`: snapshots simulados de concurrencia, FPS, CPU y memoria.
- `kaggle/online_gaming_behavior_dataset.csv`: dataset descargado de Kaggle; es público, pero el autor advierte que fue generado sintéticamente.

Los cuatro archivos de FiveM no son exportaciones de servidor ni representan usuarios reales. Su generación es reproducible con `python scripts/generar_datos_sinteticos.py` (semilla por defecto `20261104`). Se sembraron algunos valores faltantes, incompatibilidades de tipo, valores que requieren validación y filas duplicadas para que el diagnóstico tenga evidencia que identificar. No uses esos ejemplos para hacer afirmaciones empíricas sobre una comunidad.

El CSV de Kaggle fue creado por Rabie El Kharoua y se distribuye bajo licencia CC BY 4.0: [ficha del dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset). Cita al autor al reutilizarlo; sus metadatos están en [`kaggle/ATRIBUCION.md`](./kaggle/ATRIBUCION.md). La ficha declara que también es un dataset sintético educativo; su presencia en Kaggle no lo convierte en registros reales de jugadores.

Si posteriormente se obtienen exportaciones autorizadas de un servidor:

1. Colócalas en `data/raw/fivem/` y elimina/anonimiza identificadores personales.
2. Deja el CSV público de Kaggle en `data/examples/kaggle/` o agrega otros datos permitidos en `data/raw/kaggle/`.
3. En el Notebook cambia `DATA_MODE` de `"synthetic"` a `"real"` y ejecuta todas las celdas.
4. Sustituye el diagnóstico simulado del informe por los hallazgos correspondientes a las fuentes realmente utilizadas.
