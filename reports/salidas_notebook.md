# Salidas completas del Notebook de diagnostico

**Notebook fuente:** [`notebooks/diagnostico_calidad.ipynb`](../notebooks/diagnostico_calidad.ipynb)  
**Generado:** 2026-11-04T13:54:54-05:00  
**Modo ejecutado:** `synthetic` (cuatro CSV FiveM generados y un CSV publico de Kaggle sintetico, segun su autor).

> Este archivo reune las salidas de todas las celdas de codigo del Notebook al ejecutarse contra los datos presentes. No son resultados de un servidor real. Las muestras que el Notebook redacta antes de mostrarlas siguen redactadas aqui.


---

# Diagnóstico inicial de calidad de datos — FiveM Analytics

### Salida de celda de codigo 1

```text
AVISO: FiveM es un escenario sintético; el dataset público de Kaggle también se declara sintético por su autor.
Raíz del proyecto: D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics
FiveM sintético (demostración): D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics\data\examples\fivem
Kaggle (dataset público sintético): D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics\data\examples\kaggle
```

### Salida de celda de codigo 2

```text
Archivos cargados correctamente: 5
- FiveM sintético (demostración) / actividad_jugadores_sintetica: 5001 filas × 7 columnas
- FiveM sintético (demostración) / rendimiento_servidor_sintetico: 1441 filas × 7 columnas
- FiveM sintético (demostración) / sesiones_fivem_sinteticas: 5001 filas × 8 columnas
- FiveM sintético (demostración) / transacciones_economicas_sinteticas: 12397 filas × 8 columnas
- Kaggle (dataset público sintético) / online_gaming_behavior_dataset: 40034 filas × 13 columnas
```


---

## Inspección estructural

### Salida de celda de codigo 3

```text

## FiveM sintético (demostración) / actividad_jugadores_sintetica
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (5001, 7)
columns: ['event_id', 'session_id', 'player_id', 'event_at', 'activity', 'job', 'zone']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 5001 entries, 0 to 5000
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   event_id    5001 non-null   str  
 1   session_id  5001 non-null   str  
 2   player_id   5001 non-null   str  
 3   event_at    5001 non-null   str  
 4   activity    5001 non-null   str  
 5   job         5001 non-null   str  
 6   zone        5000 non-null   str  
dtypes: str(7)
memory usage: 273.6 KB
describe() — variables numéricas:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / rendimiento_servidor_sintetico
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (1441, 7)
columns: ['snapshot_at', 'server_name', 'online_players', 'max_players', 'server_fps', 'cpu_percent', 'memory_percent']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 1441 entries, 0 to 1440
Data columns (total 7 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   snapshot_at     1441 non-null   str    
 1   server_name     1441 non-null   str    
 2   online_players  1441 non-null   int64  
 3   max_players     1441 non-null   int64  
 4   server_fps      1440 non-null   float64
 5   cpu_percent     1441 non-null   float64
 6   memory_percent  1441 non-null   str    
dtypes: float64(2), int64(2), str(3)
memory usage: 78.9 KB
describe() — variables numéricas:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / sesiones_fivem_sinteticas
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (5001, 8)
columns: ['session_id', 'player_id', 'connected_at', 'disconnected_at', 'duration_minutes', 'job', 'zone', 'peak_concurrent_players']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 5001 entries, 0 to 5000
Data columns (total 8 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   session_id               5001 non-null   str  
 1   player_id                5001 non-null   str  
 2   connected_at             5001 non-null   str  
 3   disconnected_at          5001 non-null   str  
 4   duration_minutes         5000 non-null   str  
 5   job                      5001 non-null   str  
 6   zone                     5000 non-null   str  
 7   peak_concurrent_players  5001 non-null   int64
dtypes: int64(1), str(7)
memory usage: 312.7 KB
describe() — variables numéricas:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / transacciones_economicas_sinteticas
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (12397, 8)
columns: ['transaction_id', 'player_id', 'transaction_at', 'transaction_type', 'category', 'amount', 'job', 'zone']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 12397 entries, 0 to 12396
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   transaction_id    12397 non-null  str  
 1   player_id         12397 non-null  str  
 2   transaction_at    12397 non-null  str  
 3   transaction_type  12397 non-null  str  
 4   category          12397 non-null  str  
 5   amount            12396 non-null  str  
 6   job               12397 non-null  str  
 7   zone              12397 non-null  str  
dtypes: str(8)
memory usage: 774.9 KB
describe() — variables numéricas:
describe() — variables de texto (vista redactada):

## Kaggle (dataset público sintético) / online_gaming_behavior_dataset
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (40034, 13)
columns: ['PlayerID', 'Age', 'Gender', 'Location', 'GameGenre', 'PlayTimeHours', 'InGamePurchases', 'GameDifficulty', 'SessionsPerWeek', 'AvgSessionDurationMinutes', 'PlayerLevel', 'AchievementsUnlocked', 'EngagementLevel']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 40034 entries, 0 to 40033
Data columns (total 13 columns):
 #   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   PlayerID                   40034 non-null  int64  
 1   Age                        40034 non-null  int64  
 2   Gender                     40034 non-null  str    
 3   Location                   40034 non-null  str    
 4   GameGenre                  40034 non-null  str    
 5   PlayTimeHours              40034 non-null  float64
 6   InGamePurchases            40034 non-null  int64  
 7   GameDifficulty             40034 non-null  str    
 8   SessionsPerWeek            40034 non-null  int64  
 9   AvgSessionDurationMinutes  40034 non-null  int64  
 10  PlayerLevel                40034 non-null  int64  
 11  AchievementsUnlocked       40034 non-null  int64  
 12  EngagementLevel            40034 non-null  str    
dtypes: float64(1), int64(7), str(5)
memory usage: 4.0 MB
describe() — variables numéricas:
describe() — variables de texto (vista redactada):
Valores faltantes por dataset y columna:
```

```text
           event_id          session_id    player_id             event_at        activity         job          zone
0  SIM_EVENT_000001  SIM_SESSION_000001  [redactado]  2026-10-02 20:24:00       job_shift    mechanic       La Mesa
1  SIM_EVENT_000002  SIM_SESSION_000002  [redactado]  2026-10-01 08:29:00  store_purchase      police  Sandy Shores
2  SIM_EVENT_000003  SIM_SESSION_000003  [redactado]  2026-10-18 14:52:00     vehicle_use  unemployed  Pillbox Hill
3  SIM_EVENT_000004  SIM_SESSION_000004  [redactado]  2026-09-28 07:44:00       job_shift    mechanic       La Mesa
4  SIM_EVENT_000005  SIM_SESSION_000005  [redactado]  2026-10-27 13:25:00     vehicle_use      police  Sandy Shores
```
```text
              event_id          session_id    player_id             event_at     activity         job                zone
4996  SIM_EVENT_004997  SIM_SESSION_004997  [redactado]  2026-10-05 23:54:00    job_shift    mechanic  Los Santos Customs
4997  SIM_EVENT_004998  SIM_SESSION_004998  [redactado]  2026-10-03 15:25:00    job_shift     trucker             La Mesa
4998  SIM_EVENT_004999  SIM_SESSION_004999  [redactado]  2026-09-11 07:44:00    job_shift  unemployed             La Mesa
4999  SIM_EVENT_005000  SIM_SESSION_005000  [redactado]  2026-10-26 04:24:00    job_shift  unemployed        Sandy Shores
5000  SIM_EVENT_000150  SIM_SESSION_000150  [redactado]  2026-09-06 16:01:00  vehicle_use     trucker             La Mesa
```
```text
           dtype
event_id     str
session_id   str
player_id    str
event_at     str
activity     str
job          str
zone         str
```
```text
                event_id          session_id        player_id             event_at      activity       job     zone
count               5001                5001             5001                 5001          5001      5001     5000
unique              5000                5000              350                 4856             4         6        6
top     SIM_EVENT_000150  SIM_SESSION_000150  SIM_PLAYER_0296  2026-09-16 03:28:00  social_event  mechanic  La Mesa
freq                   2                   2               25                    3          1270       981     1024
```
```text
                event_id          session_id    player_id             event_at      activity       job     zone
count               5001                5001         5001                 5001          5001      5001     5000
unique              5000                5000            1                 4856             4         6        6
top     SIM_EVENT_000150  SIM_SESSION_000150  [redactado]  2026-09-16 03:28:00  social_event  mechanic  La Mesa
freq                   2                   2         5001                    3          1270       981     1024
```
```text
           snapshot_at                server_name  online_players  max_players  server_fps  cpu_percent memory_percent
0  2026-09-01 00:00:00  FiveM Roleplay (simulado)              63           64       39.86        79.31          68.99
1  2026-09-01 01:00:00  FiveM Roleplay (simulado)              49           64       45.61        67.38          67.26
2  2026-09-01 02:00:00  FiveM Roleplay (simulado)               9           64       71.84        26.22          38.17
3  2026-09-01 03:00:00  FiveM Roleplay (simulado)              13           64       61.82        32.39          49.84
4  2026-09-01 04:00:00  FiveM Roleplay (simulado)              11           64       66.95        27.54          47.01
```
```text
              snapshot_at                server_name  online_players  max_players  server_fps  cpu_percent memory_percent
1436  2026-10-30 20:00:00  FiveM Roleplay (simulado)              11           64       67.11        33.09          44.89
1437  2026-10-30 21:00:00  FiveM Roleplay (simulado)              53           64       48.37        75.61           67.2
1438  2026-10-30 22:00:00  FiveM Roleplay (simulado)              23           64       59.97        40.30          56.45
1439  2026-10-30 23:00:00  FiveM Roleplay (simulado)               6           64       71.57        31.30          39.76
1440  2026-09-09 07:00:00  FiveM Roleplay (simulado)              59           64       38.88        79.26          69.76
```
```text
                  dtype
snapshot_at         str
server_name         str
online_players    int64
max_players       int64
server_fps      float64
cpu_percent     float64
memory_percent      str
```
```text
       online_players  max_players   server_fps  cpu_percent
count     1441.000000       1441.0  1440.000000  1441.000000
mean        35.238723         64.0    55.054778    53.773380
std         17.056847          0.0     8.777395    16.229476
min          5.000000         64.0    36.350000    19.080000
25%         21.000000         64.0    47.980000    40.530000
50%         36.000000         64.0    54.815000    54.610000
75%         49.000000         64.0    61.920000    66.520000
max         64.000000         64.0    74.030000   145.000000
```
```text
                snapshot_at                server_name memory_percent
count                  1441                       1441           1441
unique                 1440                          1           1181
top     2026-09-09 07:00:00  FiveM Roleplay (simulado)          61.82
freq                      2                       1441              3
```
```text
           session_id    player_id         connected_at      disconnected_at duration_minutes         job          zone  peak_concurrent_players
0  SIM_SESSION_000001  [redactado]  2026-10-02 20:11:00  2026-10-02 20:31:00               20    mechanic       La Mesa                       22
1  SIM_SESSION_000002  [redactado]  2026-10-01 08:10:00  2026-10-01 08:54:00               44      police  Sandy Shores                       57
2  SIM_SESSION_000003  [redactado]  2026-10-18 14:12:00  2026-10-18 17:38:00              206  unemployed  Pillbox Hill                       21
3  SIM_SESSION_000004  [redactado]  2026-09-28 06:37:00  2026-09-28 07:55:00               78    mechanic       La Mesa                       60
4  SIM_SESSION_000005  [redactado]  2026-10-27 12:32:00  2026-10-27 14:06:00              NaN      police  Sandy Shores                       48
```
```text
              session_id    player_id         connected_at      disconnected_at duration_minutes         job                zone  peak_concurrent_players
4996  SIM_SESSION_004997  [redactado]  2026-10-05 23:36:00  2026-10-06 01:13:00               97    mechanic  Los Santos Customs                       60
4997  SIM_SESSION_004998  [redactado]  2026-10-03 15:18:00  2026-10-03 15:54:00               36     trucker             La Mesa                       37
4998  SIM_SESSION_004999  [redactado]  2026-09-11 06:56:00  2026-09-11 07:45:00               49  unemployed             La Mesa                       10
4999  SIM_SESSION_005000  [redactado]  2026-10-26 03:47:00  2026-10-26 04:35:00               48  unemployed        Sandy Shores                       26
5000  SIM_SESSION_000070  [redactado]  2026-09-16 16:04:00  2026-09-16 17:04:00               60    mechanic      Vespucci Beach                       28
```
```text
                         dtype
session_id                 str
player_id                  str
connected_at               str
disconnected_at            str
duration_minutes           str
job                        str
zone                       str
peak_concurrent_players  int64
```
```text
       peak_concurrent_players
count              5001.000000
mean                 36.025395
std                  16.261278
min                   8.000000
25%                  22.000000
50%                  36.000000
75%                  50.000000
max                  64.000000
```
```text
                session_id    player_id         connected_at      disconnected_at duration_minutes       job     zone
count                 5001         5001                 5001                 5001             5000      5001     5000
unique                5000            1                 4858                 4853              198         6        6
top     SIM_SESSION_000070  [redactado]  2026-09-06 11:35:00  2026-09-27 19:49:00               48  mechanic  La Mesa
freq                     2         5001                    4                    3               40       982     1023
```
```text
   transaction_id    player_id       transaction_at transaction_type category    amount         job          zone
0  SIM_TX_0000001  [redactado]  2026-10-02 20:11:00          expense  housing  11261.88    mechanic       La Mesa
1  SIM_TX_0000002  [redactado]  2026-10-01 08:30:00           income  medical  13805.45      police  Sandy Shores
2  SIM_TX_0000003  [redactado]  2026-10-01 08:41:00          expense   repair   9701.61      police  Sandy Shores
3  SIM_TX_0000004  [redactado]  2026-10-18 16:18:00          expense  medical  12980.74  unemployed  Pillbox Hill
4  SIM_TX_0000005  [redactado]  2026-09-28 07:16:00           income   repair  19155.66    mechanic       La Mesa
```
```text
       transaction_id    player_id       transaction_at transaction_type category    amount         job           zone
12392  SIM_TX_0012393  [redactado]  2026-09-11 07:22:00           income  vehicle  15062.69  unemployed        La Mesa
12393  SIM_TX_0012394  [redactado]  2026-10-26 04:14:00           income  vehicle   7297.57  unemployed   Sandy Shores
12394  SIM_TX_0012395  [redactado]  2026-10-26 03:49:00          expense  vehicle   7521.27  unemployed   Sandy Shores
12395  SIM_TX_0012396  [redactado]  2026-10-26 04:28:00          expense  housing  21869.07  unemployed   Sandy Shores
12396  SIM_TX_0000120  [redactado]  2026-10-06 16:40:00           income  medical   4821.91        taxi  Legion Square
```
```text
                 dtype
transaction_id     str
player_id          str
transaction_at     str
transaction_type   str
category           str
amount             str
job                str
zone               str
```
```text
        transaction_id        player_id       transaction_at transaction_type category   amount       job     zone
count            12397            12397                12397            12397    12397    12396     12397    12397
unique           12396              350                11425                2        6    12360         6        6
top     SIM_TX_0000120  SIM_PLAYER_0296  2026-10-23 00:51:00           income  vehicle  4177.62  mechanic  La Mesa
freq                 2               60                    4             6260     2108        2      2425     2567
```
```text
        transaction_id    player_id       transaction_at transaction_type category   amount       job     zone
count            12397        12397                12397            12397    12397    12396     12397    12397
unique           12396            1                11425                2        6    12360         6        6
top     SIM_TX_0000120  [redactado]  2026-10-23 00:51:00           income  vehicle  4177.62  mechanic  La Mesa
freq                 2        12397                    4             6260     2108        2      2425     2567
```
```text
      PlayerID  Age  Gender Location GameGenre  PlayTimeHours  InGamePurchases GameDifficulty  SessionsPerWeek  AvgSessionDurationMinutes  PlayerLevel  AchievementsUnlocked EngagementLevel
0  [redactado]   43    Male    Other  Strategy      16.271119                0         Medium                6                        108           79                    25          Medium
1  [redactado]   29  Female      USA  Strategy       5.525961                0         Medium                5                        144           11                    10          Medium
2  [redactado]   22  Female      USA    Sports       8.223755                0           Easy               16                        142           35                    41            High
3  [redactado]   35    Male      USA    Action       5.265351                1           Easy                9                         85           57                    47          Medium
4  [redactado]   33    Male   Europe    Action      15.531945                0         Medium                2                        131           95                    37          Medium
```
```text
          PlayerID  Age  Gender Location   GameGenre  PlayTimeHours  InGamePurchases GameDifficulty  SessionsPerWeek  AvgSessionDurationMinutes  PlayerLevel  AchievementsUnlocked EngagementLevel
40029  [redactado]   32    Male      USA    Strategy      20.619662                0           Easy                4                         75           85                    14          Medium
40030  [redactado]   44  Female    Other  Simulation      13.539280                0           Hard               19                        114           71                    27            High
40031  [redactado]   15  Female      USA         RPG       0.240057                1           Easy               10                        176           29                     1            High
40032  [redactado]   34    Male      USA      Sports      14.017818                1         Medium                3                        128           70                    10          Medium
40033  [redactado]   19    Male      USA      Sports      10.083804                0           Easy               13                         84           72                    39          Medium
```
```text
                             dtype
PlayerID                     int64
Age                          int64
Gender                         str
Location                       str
GameGenre                      str
PlayTimeHours              float64
InGamePurchases              int64
GameDifficulty                 str
SessionsPerWeek              int64
AvgSessionDurationMinutes    int64
PlayerLevel                  int64
AchievementsUnlocked         int64
EngagementLevel                str
```
```text
           PlayerID           Age  PlayTimeHours  InGamePurchases  SessionsPerWeek  AvgSessionDurationMinutes   PlayerLevel  AchievementsUnlocked
count  40034.000000  40034.000000   40034.000000     40034.000000     40034.000000               40034.000000  40034.000000          40034.000000
mean   29016.500000     31.992531      12.024365         0.200854         9.471774                  94.792252     49.655568             24.526477
std    11556.964675     10.043227       6.914638         0.400644         5.763667                  49.011375     28.588379             14.430726
min     9000.000000     15.000000       0.000115         0.000000         0.000000                  10.000000      1.000000              0.000000
25%    19008.250000     23.000000       6.067501         0.000000         4.000000                  52.000000     25.000000             12.000000
50%    29016.500000     32.000000      12.008002         0.000000         9.000000                  95.000000     49.000000             25.000000
75%    39024.750000     41.000000      17.963831         0.000000        14.000000                 137.000000     74.000000             37.000000
max    49033.000000     49.000000      23.999592         1.000000        19.000000                 179.000000     99.000000             49.000000
```
```text
       Gender Location GameGenre GameDifficulty EngagementLevel
count   40034    40034     40034          40034           40034
unique      2        4         5              3               3
top      Male      USA    Sports           Easy          Medium
freq    23959    16000      8048          20015           19374
```
```text
                                                                Dataset  Filas  Columnas       Tipos de datos
0        FiveM sintético (demostración) / actividad_jugadores_sintetica   5001         7                  str
1       FiveM sintético (demostración) / rendimiento_servidor_sintetico   1441         7  float64, int64, str
2            FiveM sintético (demostración) / sesiones_fivem_sinteticas   5001         8           int64, str
3  FiveM sintético (demostración) / transacciones_economicas_sinteticas  12397         8                  str
4   Kaggle (dataset público sintético) / online_gaming_behavior_dataset  40034        13  float64, int64, str
```
```text
                                                                Dataset           Columna  Valores faltantes  Porcentaje
0        FiveM sintético (demostración) / actividad_jugadores_sintetica              zone                  1        0.02
1       FiveM sintético (demostración) / rendimiento_servidor_sintetico        server_fps                  1        0.07
2            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes                  1        0.02
3            FiveM sintético (demostración) / sesiones_fivem_sinteticas              zone                  1        0.02
4  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount                  1        0.01
```


---

## Indicadores iniciales y lectura crítica

### Salida de celda de codigo 4

```text
Hallazgos automáticos para revisión; los rangos son reglas orientadoras, no reglas universales del dominio:

Interpretación requerida antes de preparar los datos:
1. Contrastar fechas, unidades y definiciones de variables con la documentación de cada fuente.
2. Validar las reglas de rango orientadoras contra el esquema y el significado de cada fuente.
3. Distinguir faltantes legítimos de errores de captura y justificar el tratamiento por variable.
4. Confirmar periodo, población y licencia del dataset de Kaggle antes de compararlo con FiveM.
5. Registrar en reports/informe_diagnostico.md la evidencia, impacto y acción propuesta por hallazgo.
```

```text
                                                                Dataset  Filas duplicadas exactas  Columnas con faltantes  Columnas numéricas  Columnas texto
0        FiveM sintético (demostración) / actividad_jugadores_sintetica                         1                       1                   0               7
1       FiveM sintético (demostración) / rendimiento_servidor_sintetico                         1                       1                   4               3
2            FiveM sintético (demostración) / sesiones_fivem_sinteticas                         1                       2                   1               7
3  FiveM sintético (demostración) / transacciones_economicas_sinteticas                         1                       1                   0               8
4   Kaggle (dataset público sintético) / online_gaming_behavior_dataset                         0                       0                   8               5
```
```text
                                                                 Dataset          Variable                     Problema  Registros               Evidencia/regla
0         FiveM sintético (demostración) / actividad_jugadores_sintetica     Fila completa             Duplicado exacto          1        dataframe.duplicated()
1         FiveM sintético (demostración) / actividad_jugadores_sintetica              zone               Valor faltante          1                        isna()
2        FiveM sintético (demostración) / rendimiento_servidor_sintetico     Fila completa             Duplicado exacto          1        dataframe.duplicated()
3        FiveM sintético (demostración) / rendimiento_servidor_sintetico        server_fps               Valor faltante          1                        isna()
4        FiveM sintético (demostración) / rendimiento_servidor_sintetico       cpu_percent   Fuera del rango orientador          1          mínimo=0; máximo=100
5        FiveM sintético (demostración) / rendimiento_servidor_sintetico    memory_percent       Tipo/valor no numérico          1   to_numeric(errors='coerce')
6             FiveM sintético (demostración) / sesiones_fivem_sinteticas     Fila completa             Duplicado exacto          1        dataframe.duplicated()
7             FiveM sintético (demostración) / sesiones_fivem_sinteticas   disconnected_at  Fecha/hora no interpretable          1  to_datetime(errors='coerce')
8             FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes               Valor faltante          1                        isna()
9             FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes       Tipo/valor no numérico          1   to_numeric(errors='coerce')
10            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes   Fuera del rango orientador          1         mínimo=1; máximo=None
11            FiveM sintético (demostración) / sesiones_fivem_sinteticas              zone               Valor faltante          1                        isna()
12  FiveM sintético (demostración) / transacciones_economicas_sinteticas     Fila completa             Duplicado exacto          1        dataframe.duplicated()
13  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount               Valor faltante          1                        isna()
14  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount       Tipo/valor no numérico          1   to_numeric(errors='coerce')
15  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount   Fuera del rango orientador          1         mínimo=0; máximo=None
```


---

## Cierre

---

**Fin de salidas.** El Notebook realiza diagnostico inicial; no limpia los datos ni permite inferencias sobre una comunidad real con estas fuentes.
