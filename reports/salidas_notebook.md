# Salidas completas del Notebook de diagnóstico

**Notebook:** [`notebooks/diagnostico_calidad.ipynb`](../notebooks/diagnostico_calidad.ipynb)
**Generadas:** al ejecutar el Notebook con los archivos del repositorio
**Kernel:** `.venv` (`Python (fivem-analytics .venv)`)
**Modo:** `synthetic`; se inspeccionan nueve CSV FiveM sintéticos y un CSV público de Kaggle que su autor también declara sintético.

> Salidas de texto y tablas de las celdas ejecutadas. No son resultados de un servidor real. Las vistas de muestras respetan la redacción de identificadores del Notebook.

---

# Diagnóstico inicial de calidad de datos — FiveM Analytics

### Salida de celda de código 1

```text
AVISO: FiveM es un escenario sintético; el dataset público de Kaggle también se declara sintético por su autor.
Raíz del proyecto: D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics
FiveM sintético (demostración): D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics\data\examples\fivem
Kaggle (dataset público sintético): D:\TRABAJOS SENA\CIENCIAS DE DATOS\fivem-analytics\data\examples\kaggle
```

### Salida de celda de código 2

```text
Archivos cargados correctamente: 10
- FiveM sintético (demostración) / actividad_jugadores_sintetica: 5001 filas × 7 columnas
- FiveM sintético (demostración) / expanded/players: 1515 filas × 11 columnas
- FiveM sintético (demostración) / expanded/server_performance: 2840 filas × 7 columnas
- FiveM sintético (demostración) / expanded/sessions: 8000 filas × 10 columnas
- FiveM sintético (demostración) / expanded/transactions: 12000 filas × 7 columnas
- FiveM sintético (demostración) / expanded/vehicles: 2200 filas × 9 columnas
- FiveM sintético (demostración) / rendimiento_servidor_sintetico: 1441 filas × 7 columnas
- FiveM sintético (demostración) / sesiones_fivem_sinteticas: 5001 filas × 8 columnas
- FiveM sintético (demostración) / transacciones_economicas_sinteticas: 12397 filas × 8 columnas
- Kaggle (dataset público sintético) / online_gaming_behavior_dataset: 40034 filas × 13 columnas
```

---

## Inspección estructural

### Salida de celda de código 3

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
 0   event_id    5001 non-null   string
 1   session_id  5001 non-null   string
 2   player_id   5001 non-null   string
 3   event_at    5001 non-null   str
 4   activity    5001 non-null   str
 5   job         5001 non-null   str
 6   zone        5000 non-null   str
dtypes: str(4), string(3)
memory usage: 273.6 KB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / expanded/players
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (1515, 11)
columns: ['player_id', 'license', 'discord_id', 'username', 'job', 'cash', 'bank', 'age_character', 'registered_at', 'last_seen', 'banned']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 1515 entries, 0 to 1514
Data columns (total 11 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   player_id      1515 non-null   string
 1   license        1515 non-null   string
 2   discord_id     1423 non-null   string
 3   username       1515 non-null   string
 4   job            1471 non-null   str
 5   cash           1515 non-null   float64
 6   bank           1515 non-null   float64
 7   age_character  1515 non-null   int64
 8   registered_at  1515 non-null   str
 9   last_seen      1495 non-null   str
 10  banned         1515 non-null   int64
dtypes: float64(2), int64(2), str(3), string(4)
memory usage: 130.3 KB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / expanded/server_performance
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (2840, 7)
columns: ['timestamp', 'players_online', 'server_fps', 'tickrate', 'cpu_pct', 'ram_mb', 'heaviest_resource']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 2840 entries, 0 to 2839
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   timestamp          2840 non-null   str
 1   players_online     2840 non-null   float64
 2   server_fps         2771 non-null   float64
 3   tickrate           2840 non-null   float64
 4   cpu_pct            2771 non-null   float64
 5   ram_mb             2840 non-null   float64
 6   heaviest_resource  2840 non-null   str
dtypes: float64(5), str(2)
memory usage: 155.4 KB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / expanded/sessions
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (8000, 10)
columns: ['session_id', 'player_id', 'connect_time', 'disconnect_time', 'duration_min', 'main_activity', 'zone', 'pos_x', 'pos_y', 'pos_z']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 8000 entries, 0 to 7999
Data columns (total 10 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   session_id       8000 non-null   string
 1   player_id        8000 non-null   string
 2   connect_time     8000 non-null   str
 3   disconnect_time  7880 non-null   str
 4   duration_min     8000 non-null   str
 5   main_activity    8000 non-null   str
 6   zone             7850 non-null   str
 7   pos_x            8000 non-null   float64
 8   pos_y            8000 non-null   float64
 9   pos_z            8000 non-null   float64
dtypes: float64(3), str(5), string(2)
memory usage: 625.1 KB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / expanded/transactions
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (12000, 7)
columns: ['transaction_id', 'player_id', 'timestamp', 'type', 'amount', 'account', 'source_job']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 12000 entries, 0 to 11999
Data columns (total 7 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   transaction_id  12000 non-null  string
 1   player_id       12000 non-null  string
 2   timestamp       12000 non-null  str
 3   type            12000 non-null  str
 4   amount          11821 non-null  str
 5   account         11900 non-null  str
 6   source_job      12000 non-null  str
dtypes: str(5), string(2)
memory usage: 656.4 KB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):

## FiveM sintético (demostración) / expanded/vehicles
head() — primeros registros (vista redactada):
tail() — últimos registros (vista redactada):
shape: (2200, 9)
columns: ['vehicle_id', 'owner_player_id', 'model', 'plate', 'price_paid', 'garage', 'fuel', 'engine_health', 'purchase_date']
dtypes:
info():
<class 'pandas.DataFrame'>
RangeIndex: 2200 entries, 0 to 2199
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   vehicle_id       2200 non-null   string
 1   owner_player_id  2200 non-null   string
 2   model            2200 non-null   str
 3   plate            2200 non-null   string
 4   price_paid       2140 non-null   float64
 5   garage           1767 non-null   str
 6   fuel             2200 non-null   float64
 7   engine_health    2200 non-null   float64
 8   purchase_date    2200 non-null   str
dtypes: float64(3), str(3), string(3)
memory usage: 154.8 KB
describe() — variables numéricas no identificadoras:
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
describe() — variables numéricas no identificadoras:
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
 0   session_id               5001 non-null   string
 1   player_id                5001 non-null   string
 2   connected_at             5001 non-null   str
 3   disconnected_at          5001 non-null   str
 4   duration_minutes         5000 non-null   str
 5   job                      5001 non-null   str
 6   zone                     5000 non-null   str
 7   peak_concurrent_players  5001 non-null   int64
dtypes: int64(1), str(5), string(2)
memory usage: 312.7 KB
describe() — variables numéricas no identificadoras:
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
 0   transaction_id    12397 non-null  string
 1   player_id         12397 non-null  string
 2   transaction_at    12397 non-null  str
 3   transaction_type  12397 non-null  str
 4   category          12397 non-null  str
 5   amount            12396 non-null  str
 6   job               12397 non-null  str
 7   zone              12397 non-null  str
dtypes: str(6), string(2)
memory usage: 774.9 KB
describe() — variables numéricas no identificadoras:
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
 0   PlayerID                   40034 non-null  string
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
dtypes: float64(1), int64(6), str(5), string(1)
memory usage: 4.0 MB
describe() — variables numéricas no identificadoras:
describe() — variables de texto (vista redactada):
Valores faltantes por dataset y columna:
```

```text
      event_id   session_id    player_id             event_at        activity         job          zone
0  [redactado]  [redactado]  [redactado]  2026-10-02 20:24:00       job_shift    mechanic       La Mesa
1  [redactado]  [redactado]  [redactado]  2026-10-01 08:29:00  store_purchase      police  Sandy Shores
2  [redactado]  [redactado]  [redactado]  2026-10-18 14:52:00     vehicle_use  unemployed  Pillbox Hill
3  [redactado]  [redactado]  [redactado]  2026-09-28 07:44:00       job_shift    mechanic       La Mesa
4  [redactado]  [redactado]  [redactado]  2026-10-27 13:25:00     vehicle_use      police  Sandy Shores
```
```text
         event_id   session_id    player_id             event_at     activity         job                zone
4996  [redactado]  [redactado]  [redactado]  2026-10-05 23:54:00    job_shift    mechanic  Los Santos Customs
4997  [redactado]  [redactado]  [redactado]  2026-10-03 15:25:00    job_shift     trucker             La Mesa
4998  [redactado]  [redactado]  [redactado]  2026-09-11 07:44:00    job_shift  unemployed             La Mesa
4999  [redactado]  [redactado]  [redactado]  2026-10-26 04:24:00    job_shift  unemployed        Sandy Shores
5000  [redactado]  [redactado]  [redactado]  2026-09-06 16:01:00  vehicle_use     trucker             La Mesa
```
```text
             dtype
event_id    string
session_id  string
player_id   string
event_at       str
activity       str
job            str
zone           str
```
```text
Empty DataFrame
Columns: []
Index: []
```
```text
           event_id   session_id    player_id             event_at      activity       job     zone
count          5001         5001         5001                 5001          5001      5001     5000
unique            1            1            1                 4856             4         6        6
top     [redactado]  [redactado]  [redactado]  2026-09-16 03:28:00  social_event  mechanic  La Mesa
freq           5001         5001         5001                    3          1270       981     1024
```
```text
     player_id      license   discord_id     username          job     cash     bank  age_character        registered_at   last_seen  banned
0  [redactado]  [redactado]  [redactado]  [redactado]      trucker    983.0  22518.0             58  2026-06-13 00:00:00  2026-07-21       0
1  [redactado]  [redactado]  [redactado]  [redactado]  gang_member   4764.0  31869.0             61  2026-09-17 00:00:00  2026-10-23       0
2  [redactado]  [redactado]  [redactado]  [redactado]   realestate   2294.0  16982.0             46  2026-08-31 00:00:00  2026-09-08       0
3  [redactado]  [redactado]  [redactado]  [redactado]    ambulance   1530.0   5913.0             50  2026-08-01 00:00:00  2026-08-31       0
4  [redactado]  [redactado]  [redactado]  [redactado]        miner  16318.0  19696.0             42  2026-07-31 00:00:00  2026-09-11       0
```
```text
        player_id      license   discord_id     username       job     cash     bank  age_character        registered_at   last_seen  banned
1510  [redactado]  [redactado]  [redactado]  [redactado]  mechanic   1414.0  40983.0             34  2026-09-21 00:00:00  2026-11-14       0
1511  [redactado]  [redactado]  [redactado]  [redactado]    police   6762.0  11723.0             48  2026-06-22 00:00:00  2026-08-12       0
1512  [redactado]  [redactado]  [redactado]  [redactado]    police  10356.0  26874.0             54  2026-08-30 00:00:00  2026-09-13       0
1513  [redactado]  [redactado]  [redactado]  [redactado]    police   3206.0   5161.0             49  2026-06-28 00:00:00  2026-08-06       0
1514  [redactado]  [redactado]  [redactado]  [redactado]   trucker   3387.0   8200.0             54  2026-10-09 00:00:00  2026-11-04       0
```
```text
                 dtype
player_id       string
license         string
discord_id      string
username        string
job                str
cash           float64
bank           float64
age_character    int64
registered_at      str
last_seen          str
banned           int64
```
```text
               cash          bank  age_character       banned
count   1515.000000  1.515000e+03    1515.000000  1515.000000
mean    5012.749175  5.282305e+07      45.611881     0.028383
std     3541.109794  7.249893e+08      45.128847     0.166119
min    -4894.000000  1.270000e+02       0.000000     0.000000
25%     2495.000000  8.733500e+03      31.000000     0.000000
50%     4162.000000  1.508700e+04      44.000000     0.000000
75%     6764.500000  2.424500e+04      56.000000     0.000000
max    23247.000000  1.000000e+10     999.000000     1.000000
```
```text
          player_id      license   discord_id     username         job        registered_at   last_seen
count          1515         1515         1515         1515        1471                 1515        1495
unique            1            1            1            1          11                  140         183
top     [redactado]  [redactado]  [redactado]  [redactado]  unemployed  2026-10-13 00:00:00  2026-11-04
freq           1515         1515         1515         1515         322                   22          18
```
```text
             timestamp  players_online  server_fps  tickrate  cpu_pct  ram_mb heaviest_resource
0  2026-06-01 00:00:00            30.0        47.1      35.3     46.1  3552.0           oxmysql
1  2026-06-01 01:00:00            48.0        44.4      35.7     49.0  3758.0      qb-policejob
2  2026-06-01 02:00:00            39.0        51.3      35.9     35.2  3940.0      qb-policejob
3  2026-06-01 03:00:00            35.0        50.8      37.4     36.0  3491.0    qb-vehicleshop
4  2026-06-01 04:00:00            36.0        51.7      37.9     38.5  3347.0           oxmysql
```
```text
                timestamp  players_online  server_fps  tickrate  cpu_pct  ram_mb heaviest_resource
2835  2026-09-28 19:00:00            68.0        41.6      33.6     59.3  4111.0    qb-vehicleshop
2836  2026-09-28 20:00:00            87.0        41.5      30.9     62.5  4340.0      qb-inventory
2837  2026-09-28 21:00:00            81.0        37.1      31.0     50.5  4689.0    qb-vehicleshop
2838  2026-09-28 22:00:00            77.0        41.7      35.8     54.8  4577.0          qb-phone
2839  2026-09-28 23:00:00            89.0        39.3      29.1     65.3  4946.0      qb-inventory
```
```text
                     dtype
timestamp              str
players_online     float64
server_fps         float64
tickrate           float64
cpu_pct            float64
ram_mb             float64
heaviest_resource      str
```
```text
       players_online   server_fps     tickrate      cpu_pct       ram_mb
count     2840.000000  2771.000000  2840.000000  2771.000000  2840.000000
mean        50.823592    46.985673    35.863134    46.952905  3918.196127
std         17.991492     6.263621     2.097219    23.481238   351.339484
min         -1.000000     0.000000    28.600000    19.800000  3133.000000
25%         39.000000    43.800000    34.500000    38.400000  3669.000000
50%         44.000000    47.900000    36.000000    43.800000  3840.500000
75%         63.000000    51.200000    37.400000    52.200000  4140.250000
max         98.000000    60.000000    40.000000   400.000000  4972.000000
```
```text
                  timestamp heaviest_resource
count                  2840              2840
unique                 2840                 7
top     2026-06-01 00:00:00          qb-phone
freq                      1               443
```
```text
    session_id    player_id         connect_time      disconnect_time duration_min main_activity          zone    pos_x    pos_y   pos_z
0  [redactado]  [redactado]  2026-07-12 23:41:41  2026-07-13 01:21:53        100.2       fishing      Vinewood  2393.34  1368.73  106.28
1  [redactado]  [redactado]  2026-09-04 21:33:33  2026-09-05 01:02:33        209.0          taxi    Paleto Bay  3640.14   370.78  649.63
2  [redactado]  [redactado]  2026-07-20 00:17:42                  NaN         90.9        mining     Grapeseed  -497.98  3255.15  309.88
3  [redactado]  [redactado]  2026-07-03 04:21:44  2026-07-03 05:30:20         68.6          none  Sandy Shores  2177.35  2173.22  486.70
4  [redactado]  [redactado]  2026-09-09 04:18:04  2026-09-09 05:44:40         86.6        mining          Mina  1383.59 -2109.79  295.21
```
```text
       session_id    player_id         connect_time      disconnect_time duration_min  main_activity           zone    pos_x    pos_y   pos_z
7995  [redactado]  [redactado]  2026-06-26 14:07:36                  NaN        224.3  police_patrol           Mina  2800.98  2094.95   83.10
7996  [redactado]  [redactado]  2026-09-08 10:17:09  2026-09-08 12:17:33        120.4        fishing     Paleto Bay    35.83  3821.52  270.73
7997  [redactado]  [redactado]  2026-08-06 10:18:47  2026-08-06 12:00:41        101.9   drug_dealing  Legion Square -1695.76  2757.32  777.86
7998  [redactado]  [redactado]  2026-06-04 08:18:35  2026-06-04 10:35:17        136.7       mechanic  Legion Square -3168.66  3582.74  454.07
7999  [redactado]  [redactado]  2026-06-30 15:34:31  2026-06-30 16:34:13         59.7           taxi     Paleto Bay     4.68  1154.09  317.52
```
```text
                   dtype
session_id        string
player_id         string
connect_time         str
disconnect_time      str
duration_min         str
main_activity        str
zone                 str
pos_x            float64
pos_y            float64
pos_z            float64
```
```text
             pos_x        pos_y        pos_z
count  8000.000000  8000.000000  8000.000000
mean    273.612341  1828.832691   401.465664
std    2152.895118  2964.522643   231.149569
min   -3496.310000 -3299.410000     0.010000
25%   -1571.647500  -750.765000   204.655000
50%     268.140000  1824.455000   402.010000
75%    2138.635000  4363.510000   602.895000
max    3999.950000  6998.880000   799.730000
```
```text
         session_id    player_id         connect_time      disconnect_time duration_min  main_activity           zone
count          8000         8000                 8000                 7880         8000           8000           7850
unique            1            1                 7996                 7874         3117              8              8
top     [redactado]  [redactado]  2026-06-30 21:42:35  2026-09-01 17:42:22        720.0  police_patrol  Legion Square
freq           8000         8000                    2                    2          100           1036           1010
```
```text
  transaction_id    player_id            timestamp           type   amount account  source_job
0    [redactado]  [redactado]  2026-09-18 21:00:10       transfer  -1805.0    cash    mechanic
1    [redactado]  [redactado]  2026-08-01 07:25:13           fine  -1359.0    bank  realestate
2    [redactado]  [redactado]  2026-06-04 07:00:36  purchase_item  -7610.0    cash       miner
3    [redactado]  [redactado]  2026-09-02 12:27:17  purchase_item  -2644.0    cash   fisherman
4    [redactado]  [redactado]  2026-06-18 20:39:09         salary    271.0    bank   ambulance
```
```text
      transaction_id    player_id            timestamp          type   amount      account  source_job
11995    [redactado]  [redactado]  2026-09-09 22:59:45      transfer  -1659.0         bank   ambulance
11996    [redactado]  [redactado]  2026-09-15 12:27:45        salary   5999.0  black_money      police
11997    [redactado]  [redactado]  2026-10-21 08:30:56      transfer  -2980.0         bank  unemployed
11998    [redactado]  [redactado]  2026-06-22 18:14:15  illegal_sale   5087.0         cash    mechanic
11999    [redactado]  [redactado]  2026-06-12 23:14:59        salary   4081.0         bank  unemployed
```
```text
                 dtype
transaction_id  string
player_id       string
timestamp          str
type               str
amount             str
account            str
source_job         str
```
```text
Empty DataFrame
Columns: []
Index: []
```
```text
       transaction_id    player_id            timestamp    type         amount account  source_job
count           12000        12000                12000   12000          11821   11900       12000
unique              1            1                11965       8           8596       3          10
top       [redactado]  [redactado]  0000-00-00 00:00:00  salary  -1000000000.0    cash  unemployed
freq            12000        12000                   30    4114             26    5989        1256
```
```text
    vehicle_id owner_player_id      model        plate  price_paid   garage  fuel  engine_health purchase_date
0  [redactado]     [redactado]  ambulance  [redactado]      -365.0   paleto  15.7          293.0    2026-07-25
1  [redactado]     [redactado]      panto  [redactado]      7820.0    sandy  85.7          406.0    2026-10-08
2  [redactado]     [redactado]      adder  [redactado]   1000443.0  pillbox  89.3          460.0    2026-09-28
3  [redactado]     [redactado]        t20  [redactado]   2200270.0   paleto  33.8          689.0    2026-08-09
4  [redactado]     [redactado]    police3  [redactado]       147.0   paleto  90.2          445.0    2026-09-24
```
```text
       vehicle_id owner_player_id   model        plate  price_paid  garage  fuel  engine_health purchase_date
2195  [redactado]     [redactado]   panto  [redactado]      8278.0  paleto  53.4          534.0    2026-07-20
2196  [redactado]     [redactado]   adder  [redactado]    999872.0     NaN  92.6          511.0    2026-08-30
2197  [redactado]     [redactado]   bison  [redactado]     28055.0  legion   8.0          258.0    2026-07-16
2198  [redactado]     [redactado]   bison  [redactado]     28298.0  legion  42.0          447.0    2026-10-12
2199  [redactado]     [redactado]  faggio  [redactado]      4818.0  legion  50.1          810.0    2026-07-17
```
```text
                   dtype
vehicle_id        string
owner_player_id   string
model                str
plate             string
price_paid       float64
garage               str
fuel             float64
engine_health    float64
purchase_date        str
```
```text
         price_paid         fuel  engine_health
count  2.140000e+03  2200.000000    2200.000000
mean   4.326947e+05    53.105955     588.195909
std    7.045013e+05    37.919610     235.610730
min   -4.980000e+02     0.000000      -1.000000
25%    4.687250e+03    25.775000     390.000000
50%    2.782400e+04    49.850000     588.000000
75%    9.000512e+05    76.650000     787.250000
max    2.200499e+06   250.000000     999.000000
```
```text
         vehicle_id owner_player_id   model        plate garage purchase_date
count          2200            2200    2200         2200   1767          2200
unique            1               1      10            1      4           150
top     [redactado]     [redactado]  sultan  [redactado]  sandy    2026-08-17
freq           2200            2200     251         2200    452            27
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
0  [redactado]  [redactado]  2026-10-02 20:11:00  2026-10-02 20:31:00               20    mechanic       La Mesa                       22
1  [redactado]  [redactado]  2026-10-01 08:10:00  2026-10-01 08:54:00               44      police  Sandy Shores                       57
2  [redactado]  [redactado]  2026-10-18 14:12:00  2026-10-18 17:38:00              206  unemployed  Pillbox Hill                       21
3  [redactado]  [redactado]  2026-09-28 06:37:00  2026-09-28 07:55:00               78    mechanic       La Mesa                       60
4  [redactado]  [redactado]  2026-10-27 12:32:00  2026-10-27 14:06:00              NaN      police  Sandy Shores                       48
```
```text
       session_id    player_id         connected_at      disconnected_at duration_minutes         job                zone  peak_concurrent_players
4996  [redactado]  [redactado]  2026-10-05 23:36:00  2026-10-06 01:13:00               97    mechanic  Los Santos Customs                       60
4997  [redactado]  [redactado]  2026-10-03 15:18:00  2026-10-03 15:54:00               36     trucker             La Mesa                       37
4998  [redactado]  [redactado]  2026-09-11 06:56:00  2026-09-11 07:45:00               49  unemployed             La Mesa                       10
4999  [redactado]  [redactado]  2026-10-26 03:47:00  2026-10-26 04:35:00               48  unemployed        Sandy Shores                       26
5000  [redactado]  [redactado]  2026-09-16 16:04:00  2026-09-16 17:04:00               60    mechanic      Vespucci Beach                       28
```
```text
                          dtype
session_id               string
player_id                string
connected_at                str
disconnected_at             str
duration_minutes            str
job                         str
zone                        str
peak_concurrent_players   int64
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
count          5001         5001                 5001                 5001             5000      5001     5000
unique            1            1                 4858                 4853              198         6        6
top     [redactado]  [redactado]  2026-09-06 11:35:00  2026-09-27 19:49:00               48  mechanic  La Mesa
freq           5001         5001                    4                    3               40       982     1023
```
```text
  transaction_id    player_id       transaction_at transaction_type category    amount         job          zone
0    [redactado]  [redactado]  2026-10-02 20:11:00          expense  housing  11261.88    mechanic       La Mesa
1    [redactado]  [redactado]  2026-10-01 08:30:00           income  medical  13805.45      police  Sandy Shores
2    [redactado]  [redactado]  2026-10-01 08:41:00          expense   repair   9701.61      police  Sandy Shores
3    [redactado]  [redactado]  2026-10-18 16:18:00          expense  medical  12980.74  unemployed  Pillbox Hill
4    [redactado]  [redactado]  2026-09-28 07:16:00           income   repair  19155.66    mechanic       La Mesa
```
```text
      transaction_id    player_id       transaction_at transaction_type category    amount         job           zone
12392    [redactado]  [redactado]  2026-09-11 07:22:00           income  vehicle  15062.69  unemployed        La Mesa
12393    [redactado]  [redactado]  2026-10-26 04:14:00           income  vehicle   7297.57  unemployed   Sandy Shores
12394    [redactado]  [redactado]  2026-10-26 03:49:00          expense  vehicle   7521.27  unemployed   Sandy Shores
12395    [redactado]  [redactado]  2026-10-26 04:28:00          expense  housing  21869.07  unemployed   Sandy Shores
12396    [redactado]  [redactado]  2026-10-06 16:40:00           income  medical   4821.91        taxi  Legion Square
```
```text
                   dtype
transaction_id    string
player_id         string
transaction_at       str
transaction_type     str
category             str
amount               str
job                  str
zone                 str
```
```text
Empty DataFrame
Columns: []
Index: []
```
```text
       transaction_id    player_id       transaction_at transaction_type category   amount       job     zone
count           12397        12397                12397            12397    12397    12396     12397    12397
unique              1            1                11425                2        6    12360         6        6
top       [redactado]  [redactado]  2026-10-23 00:51:00           income  vehicle  4177.62  mechanic  La Mesa
freq            12397        12397                    4             6260     2108        2      2425     2567
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
PlayerID                    string
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
                Age  PlayTimeHours  InGamePurchases  SessionsPerWeek  AvgSessionDurationMinutes   PlayerLevel  AchievementsUnlocked
count  40034.000000   40034.000000     40034.000000     40034.000000               40034.000000  40034.000000          40034.000000
mean      31.992531      12.024365         0.200854         9.471774                  94.792252     49.655568             24.526477
std       10.043227       6.914638         0.400644         5.763667                  49.011375     28.588379             14.430726
min       15.000000       0.000115         0.000000         0.000000                  10.000000      1.000000              0.000000
25%       23.000000       6.067501         0.000000         4.000000                  52.000000     25.000000             12.000000
50%       32.000000      12.008002         0.000000         9.000000                  95.000000     49.000000             25.000000
75%       41.000000      17.963831         0.000000        14.000000                 137.000000     74.000000             37.000000
max       49.000000      23.999592         1.000000        19.000000                 179.000000     99.000000             49.000000
```
```text
           PlayerID Gender Location GameGenre GameDifficulty EngagementLevel
count         40034  40034    40034     40034          40034           40034
unique            1      2        4         5              3               3
top     [redactado]   Male      USA    Sports           Easy          Medium
freq          40034  23959    16000      8048          20015           19374
```
```text
                                                                Dataset  Filas  Columnas               Tipos de datos
0        FiveM sintético (demostración) / actividad_jugadores_sintetica   5001         7                  str, string
1                     FiveM sintético (demostración) / expanded/players   1515        11  float64, int64, str, string
2          FiveM sintético (demostración) / expanded/server_performance   2840         7                 float64, str
3                    FiveM sintético (demostración) / expanded/sessions   8000        10         float64, str, string
4                FiveM sintético (demostración) / expanded/transactions  12000         7                  str, string
5                    FiveM sintético (demostración) / expanded/vehicles   2200         9         float64, str, string
6       FiveM sintético (demostración) / rendimiento_servidor_sintetico   1441         7          float64, int64, str
7            FiveM sintético (demostración) / sesiones_fivem_sinteticas   5001         8           int64, str, string
8  FiveM sintético (demostración) / transacciones_economicas_sinteticas  12397         8                  str, string
9   Kaggle (dataset público sintético) / online_gaming_behavior_dataset  40034        13  float64, int64, str, string
```
```text
                                                                 Dataset           Columna  Valores faltantes  Porcentaje
0         FiveM sintético (demostración) / actividad_jugadores_sintetica              zone                  1        0.02
1                      FiveM sintético (demostración) / expanded/players        discord_id                 92        6.07
2                      FiveM sintético (demostración) / expanded/players               job                 44        2.90
3                      FiveM sintético (demostración) / expanded/players         last_seen                 20        1.32
4           FiveM sintético (demostración) / expanded/server_performance        server_fps                 69        2.43
5           FiveM sintético (demostración) / expanded/server_performance           cpu_pct                 69        2.43
6                     FiveM sintético (demostración) / expanded/sessions   disconnect_time                120        1.50
7                     FiveM sintético (demostración) / expanded/sessions              zone                150        1.88
8                 FiveM sintético (demostración) / expanded/transactions            amount                179        1.49
9                 FiveM sintético (demostración) / expanded/transactions           account                100        0.83
10                    FiveM sintético (demostración) / expanded/vehicles        price_paid                 60        2.73
11                    FiveM sintético (demostración) / expanded/vehicles            garage                433       19.68
12       FiveM sintético (demostración) / rendimiento_servidor_sintetico        server_fps                  1        0.07
13            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes                  1        0.02
14            FiveM sintético (demostración) / sesiones_fivem_sinteticas              zone                  1        0.02
15  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount                  1        0.01
```

---

## Indicadores iniciales y lectura crítica

### Salida de celda de código 4

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
1                     FiveM sintético (demostración) / expanded/players                        15                       3                   4               7
2          FiveM sintético (demostración) / expanded/server_performance                         0                       2                   5               2
3                    FiveM sintético (demostración) / expanded/sessions                         0                       2                   3               7
4                FiveM sintético (demostración) / expanded/transactions                         0                       2                   0               7
5                    FiveM sintético (demostración) / expanded/vehicles                         0                       2                   3               6
6       FiveM sintético (demostración) / rendimiento_servidor_sintetico                         1                       1                   4               3
7            FiveM sintético (demostración) / sesiones_fivem_sinteticas                         1                       2                   1               7
8  FiveM sintético (demostración) / transacciones_economicas_sinteticas                         1                       1                   0               8
9   Kaggle (dataset público sintético) / online_gaming_behavior_dataset                         0                       0                   7               6
```
```text
                                                                 Dataset          Variable                                Problema  Registros                            Evidencia/regla
0         FiveM sintético (demostración) / actividad_jugadores_sintetica     Fila completa                        Duplicado exacto          1                     dataframe.duplicated()
1         FiveM sintético (demostración) / actividad_jugadores_sintetica              zone                          Valor faltante          1                                     isna()
2                      FiveM sintético (demostración) / expanded/players     Fila completa                        Duplicado exacto         15                     dataframe.duplicated()
3                      FiveM sintético (demostración) / expanded/players        discord_id                          Valor faltante         92                                     isna()
4                      FiveM sintético (demostración) / expanded/players               job                          Valor faltante         44                                     isna()
5                      FiveM sintético (demostración) / expanded/players               job      Variantes de mayúsculas/minúsculas         25  valores distintos tras strip().casefold()
6                      FiveM sintético (demostración) / expanded/players              cash              Fuera del rango orientador         12                      mínimo=0; máximo=None
7                      FiveM sintético (demostración) / expanded/players              bank              Fuera del rango orientador          8                 mínimo=0; máximo=100000000
8                      FiveM sintético (demostración) / expanded/players     age_character              Fuera del rango orientador          6                      mínimo=18; máximo=100
9                      FiveM sintético (demostración) / expanded/players         last_seen                          Valor faltante         20                                     isna()
10          FiveM sintético (demostración) / expanded/server_performance    players_online              Fuera del rango orientador         19                       mínimo=0; máximo=128
11          FiveM sintético (demostración) / expanded/server_performance        server_fps                          Valor faltante         69                                     isna()
12          FiveM sintético (demostración) / expanded/server_performance        server_fps              Fuera del rango orientador         15                       mínimo=1; máximo=100
13          FiveM sintético (demostración) / expanded/server_performance           cpu_pct                          Valor faltante         69                                     isna()
14          FiveM sintético (demostración) / expanded/server_performance           cpu_pct              Fuera del rango orientador         10                       mínimo=0; máximo=100
15                    FiveM sintético (demostración) / expanded/sessions   disconnect_time                          Valor faltante        120                                     isna()
16                    FiveM sintético (demostración) / expanded/sessions      duration_min                  Tipo/valor no numérico         10                to_numeric(errors='coerce')
17                    FiveM sintético (demostración) / expanded/sessions      duration_min              Fuera del rango orientador         55                       mínimo=1; máximo=720
18                    FiveM sintético (demostración) / expanded/sessions              zone                          Valor faltante        150                                     isna()
19                FiveM sintético (demostración) / expanded/transactions         timestamp             Fecha/hora no interpretable         30               to_datetime(errors='coerce')
20                FiveM sintético (demostración) / expanded/transactions              type                Espacios al inicio/final         40                valor distinto tras strip()
21                FiveM sintético (demostración) / expanded/transactions              type      Variantes de mayúsculas/minúsculas         40  valores distintos tras strip().casefold()
22                FiveM sintético (demostración) / expanded/transactions            amount                          Valor faltante        179                                     isna()
23                FiveM sintético (demostración) / expanded/transactions            amount                  Tipo/valor no numérico         15                to_numeric(errors='coerce')
24                FiveM sintético (demostración) / expanded/transactions            amount              Fuera del rango orientador         50            mínimo=-1000000; máximo=1000000
25                FiveM sintético (demostración) / expanded/transactions           account                          Valor faltante        100                                     isna()
26                    FiveM sintético (demostración) / expanded/vehicles        price_paid                          Valor faltante         60                                     isna()
27                    FiveM sintético (demostración) / expanded/vehicles        price_paid              Fuera del rango orientador        200                      mínimo=0; máximo=None
28                    FiveM sintético (demostración) / expanded/vehicles            garage                          Valor faltante        433                                     isna()
29                    FiveM sintético (demostración) / expanded/vehicles              fuel              Fuera del rango orientador         35                       mínimo=0; máximo=100
30       FiveM sintético (demostración) / rendimiento_servidor_sintetico     Fila completa                        Duplicado exacto          1                     dataframe.duplicated()
31       FiveM sintético (demostración) / rendimiento_servidor_sintetico        server_fps                          Valor faltante          1                                     isna()
32       FiveM sintético (demostración) / rendimiento_servidor_sintetico       cpu_percent              Fuera del rango orientador          1                       mínimo=0; máximo=100
33       FiveM sintético (demostración) / rendimiento_servidor_sintetico    memory_percent                  Tipo/valor no numérico          1                to_numeric(errors='coerce')
34            FiveM sintético (demostración) / sesiones_fivem_sinteticas     Fila completa                        Duplicado exacto          1                     dataframe.duplicated()
35            FiveM sintético (demostración) / sesiones_fivem_sinteticas   disconnected_at             Fecha/hora no interpretable          1               to_datetime(errors='coerce')
36            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes                          Valor faltante          1                                     isna()
37            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes                  Tipo/valor no numérico          1                to_numeric(errors='coerce')
38            FiveM sintético (demostración) / sesiones_fivem_sinteticas  duration_minutes              Fuera del rango orientador          1                      mínimo=1; máximo=None
39            FiveM sintético (demostración) / sesiones_fivem_sinteticas              zone                          Valor faltante          1                                     isna()
40  FiveM sintético (demostración) / transacciones_economicas_sinteticas     Fila completa                        Duplicado exacto          1                     dataframe.duplicated()
41  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount                          Valor faltante          1                                     isna()
42  FiveM sintético (demostración) / transacciones_economicas_sinteticas            amount                  Tipo/valor no numérico          1                to_numeric(errors='coerce')
43                     FiveM sintético (demostración) / expanded/players         player_id                Clave primaria duplicada         15                     player_id.duplicated()
44                    FiveM sintético (demostración) / expanded/sessions         player_id  Referencia sin jugador correspondiente         30         clave ausente en players.player_id
45          FiveM sintético (demostración) / expanded/server_performance         timestamp     Huecos en muestreo horario esperado         40    horas esperadas menos marcas observadas
```

---

## Resumen analítico del escenario ampliado

### Salida de celda de código 5

```text
Jugadores únicos para el análisis: 1,500
Sesiones enlazadas a jugadores: 7,970 de 8,000
Sesiones con duración entre 1 y 720 minutos y fecha válida: 7,905
Sesiones por actividad (duración mediana solo con dato numérico):
Sesiones por zona (la ubicación sintética no representa un mapa observado):
Proxy de repetición a 7 días: 1,436/1,488 jugadores elegibles (96.5%); no equivale a retención real.
Transacciones por tipo tras normalizar espacios/mayúsculas y excluir importes > 1,000,000 (regla exploratoria):
Importes no interpretables o fuera de ese umbral: 50 de 12,000.
Correlación descriptiva entre minutos válidos y suma firmada de transacciones (jugadores emparejados n=1,487): -0.019. No demuestra causalidad y depende de los límites exploratorios usados.
Vehículos por modelo (descripción del escenario):
Correlación descriptiva jugadores concurrentes/FPS en rangos orientadores (n=2,729): -0.815. No es una medición real.
Métricas agrupadas por etiqueta de recurso simulada; no atribuye causalidad:
```

```text
               sesiones  duracion_mediana_min
main_activity
police_patrol      1024                 108.4
drug_dealing       1012                 112.8
mining             1009                 109.5
fishing             984                 113.2
mechanic            982                 110.6
racing              976                 115.2
taxi                971                 114.9
none                947                 112.4
```
```text
               sesiones  duracion_mediana_min
zone
Legion Square      1002                 110.6
Paleto Bay          988                 112.6
Grapeseed           982                 112.4
Vinewood            982                 111.2
Mirror Park         972                 116.1
Mina                960                 112.4
Port                946                 115.5
Sandy Shores        924                 110.3
NaN                 149                  93.8
```
```text
                  transacciones  importe_mediano  suma_firmada
type_normalized
salary                     4084           4011.0    16247867.0
purchase_item              3019          -4053.0   -12167110.0
transfer                   1775          -4088.0    -7212664.0
illegal_sale               1432           4094.0     5860835.0
fine                        885          -3730.0    -3432149.0
purchase_vehicle            348        -134954.5   -46515754.0
property                    228        -341059.0   -78133747.0
```
```text
           vehiculos  precio_mediano  combustible_mediano
model
sultan           251         35087.5                 52.8
buzzard          235        899992.5                 48.4
adder            230        999987.5                 50.0
bison            224         27976.0                 50.8
t20              223       2199957.5                 49.4
police3          220           -57.5                 50.4
panto            216          7985.5                 48.3
faggio           203          4536.0                 46.8
ambulance        201           116.0                 46.4
sanchez          197          8984.0                 55.1
```
```text
                   muestras  fps_promedio  cpu_promedio
heaviest_resource
qb-phone                443         46.90         47.22
mlo_pack                421         46.90         46.60
qb-inventory            416         47.02         46.84
qb-vehicleshop          408         46.60         46.54
qb-policejob            396         47.16         47.20
qb-core                 391         47.06         46.88
oxmysql                 365         47.30         47.43
```

---

## Cierre

---

**Fin de salidas.** Todos los resultados corresponden al escenario simulado; revisar `reports/informe_diagnostico.md` para límites y lectura crítica.
