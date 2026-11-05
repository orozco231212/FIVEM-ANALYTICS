"""Generate deterministic, clearly labeled synthetic FiveM datasets."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 42
PLAYER_COUNT = 1_500
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "examples" / "fivem" / "expanded"
JOBS = (
    "police", "ambulance", "mechanic", "miner", "taxi",
    "trucker", "fisherman", "unemployed", "gang_member", "realestate",
)


def generate(output_dir: Path = OUTPUT_DIR, seed: int = SEED) -> dict[str, int]:
    """Create five reproducible CSVs with labeled identifiers and seeded defects."""
    rng = np.random.default_rng(seed)
    output_dir.mkdir(parents=True, exist_ok=True)

    registration = pd.Timestamp("2026-06-01") + pd.to_timedelta(
        rng.integers(0, 140, PLAYER_COUNT), unit="D"
    )
    players = pd.DataFrame({
        "player_id": np.arange(1, PLAYER_COUNT + 1),
        "license": [f"SIM_LICENSE:{rng.bytes(8).hex()}" for _ in range(PLAYER_COUNT)],
        "discord_id": [f"SIM_DISCORD_{value}" for value in rng.integers(10**17, 10**18, PLAYER_COUNT)],
        "username": [f"sim_user_{index}" for index in range(PLAYER_COUNT)],
        "job": rng.choice(JOBS, PLAYER_COUNT, p=[.10, .07, .09, .12, .08, .08, .06, .25, .08, .07]),
        "cash": rng.gamma(2, 2_500, PLAYER_COUNT).round(0),
        "bank": rng.gamma(2, 9_000, PLAYER_COUNT).round(0),
        "age_character": rng.integers(18, 70, PLAYER_COUNT),
        "registered_at": registration.strftime("%Y-%m-%d %H:%M:%S"),
        "last_seen": (registration + pd.to_timedelta(rng.integers(0, 60, PLAYER_COUNT), unit="D")).strftime("%Y-%m-%d"),
        "banned": rng.choice([0, 1], PLAYER_COUNT, p=[.97, .03]),
    })
    players.loc[rng.choice(PLAYER_COUNT, 90, replace=False), "discord_id"] = pd.NA
    players.loc[rng.choice(PLAYER_COUNT, 45, replace=False), "job"] = pd.NA
    players.loc[rng.choice(PLAYER_COUNT, 12, replace=False), "cash"] = -rng.integers(100, 5_000, 12)
    players.loc[rng.choice(PLAYER_COUNT, 6, replace=False), "age_character"] = rng.choice([0, 5, 150, 999], 6)
    players.loc[rng.choice(PLAYER_COUNT, 8, replace=False), "bank"] = 9_999_999_999
    players.loc[rng.choice(PLAYER_COUNT, 25, replace=False), "job"] = "POLICE"
    players.loc[rng.choice(PLAYER_COUNT, 20, replace=False), "last_seen"] = "N/A"
    players = pd.concat([players, players.sample(15, random_state=1)], ignore_index=True)

    session_count = 8_000
    player_ids = rng.choice(np.arange(1, PLAYER_COUNT + 1), session_count)
    connect = pd.Timestamp("2026-06-01") + pd.to_timedelta(
        rng.integers(0, 150 * 86_400, session_count), unit="s"
    )
    duration = np.clip(rng.lognormal(4.7, .8, session_count), 1, 720).round(1)
    sessions = pd.DataFrame({
        "session_id": np.arange(1, session_count + 1),
        "player_id": player_ids,
        "connect_time": connect.strftime("%Y-%m-%d %H:%M:%S"),
        "disconnect_time": (connect + pd.to_timedelta(duration, unit="m")).strftime("%Y-%m-%d %H:%M:%S"),
        "duration_min": duration,
        "main_activity": rng.choice(
            ["mining", "police_patrol", "taxi", "mechanic", "drug_dealing", "fishing", "racing", "none"],
            session_count,
        ),
        "zone": rng.choice(
            ["Legion Square", "Sandy Shores", "Paleto Bay", "Port", "Mirror Park", "Vinewood", "Grapeseed", "Mina"],
            session_count,
        ),
        "pos_x": rng.uniform(-3_500, 4_000, session_count).round(2),
        "pos_y": rng.uniform(-3_300, 7_000, session_count).round(2),
        "pos_z": rng.uniform(0, 800, session_count).round(2),
    })
    sessions.loc[rng.choice(session_count, 120, replace=False), "disconnect_time"] = pd.NA
    sessions.loc[rng.choice(session_count, 40, replace=False), "duration_min"] = -rng.integers(1, 100, 40)
    sessions.loc[rng.choice(session_count, 15, replace=False), "duration_min"] = rng.integers(2_000, 9_000, 15)
    sessions.loc[rng.choice(session_count, 150, replace=False), "zone"] = pd.NA
    sessions.loc[rng.choice(session_count, 60, replace=False), "pos_x"] = 0.0
    sessions.loc[rng.choice(session_count, 30, replace=False), "player_id"] = rng.integers(5_000, 6_000, 30)
    sessions["duration_min"] = sessions["duration_min"].astype(object)
    sessions.loc[rng.choice(session_count, 10, replace=False), "duration_min"] = "unknown"

    transaction_count = 12_000
    transaction_type = rng.choice(
        ["salary", "purchase_vehicle", "purchase_item", "transfer", "fine", "property", "illegal_sale"],
        transaction_count,
        p=[.35, .03, .25, .15, .08, .02, .12],
    )
    amount = np.where(
        transaction_type == "purchase_vehicle",
        rng.integers(15_000, 250_000, transaction_count),
        np.where(
            transaction_type == "property",
            rng.integers(80_000, 600_000, transaction_count),
            rng.integers(50, 8_000, transaction_count),
        ),
    )
    sign = np.where(np.isin(transaction_type, ["salary", "illegal_sale"]), 1, -1)
    transactions = pd.DataFrame({
        "transaction_id": np.arange(1, transaction_count + 1),
        "player_id": rng.integers(1, PLAYER_COUNT + 1, transaction_count),
        "timestamp": (
            pd.Timestamp("2026-06-01")
            + pd.to_timedelta(rng.integers(0, 150 * 86_400, transaction_count), unit="s")
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "amount": amount * sign,
        "account": rng.choice(["cash", "bank", "black_money"], transaction_count, p=[.5, .4, .1]),
        "source_job": rng.choice(JOBS, transaction_count),
    })
    transactions.loc[rng.choice(transaction_count, 180, replace=False), "amount"] = np.nan
    transactions.loc[rng.choice(transaction_count, 50, replace=False), "amount"] = rng.choice([10**9, -(10**9)], 50)
    transactions.loc[rng.choice(transaction_count, 100, replace=False), "account"] = pd.NA
    transactions.loc[rng.choice(transaction_count, 40, replace=False), "type"] = "Salary "
    transactions.loc[rng.choice(transaction_count, 30, replace=False), "timestamp"] = "0000-00-00 00:00:00"
    transactions["amount"] = transactions["amount"].astype(object)
    transactions.loc[rng.choice(transaction_count, 15, replace=False), "amount"] = "$1,500"

    vehicle_count = 2_200
    model_prices = {
        "sultan": 35_000, "adder": 1_000_000, "panto": 8_000, "faggio": 4_500,
        "bison": 28_000, "police3": 0, "ambulance": 0, "buzzard": 900_000,
        "sanchez": 9_000, "t20": 2_200_000,
    }
    models = rng.choice(list(model_prices), vehicle_count)
    vehicles = pd.DataFrame({
        "vehicle_id": np.arange(1, vehicle_count + 1),
        "owner_player_id": rng.integers(1, PLAYER_COUNT + 1, vehicle_count),
        "model": models,
        "plate": [
            f"{rng.integers(10,99)}{chr(rng.integers(65,91))}{chr(rng.integers(65,91))}{rng.integers(100,999)}"
            for _ in range(vehicle_count)
        ],
        "price_paid": [model_prices[model] + int(rng.integers(-500, 500)) for model in models],
        "garage": rng.choice(["legion", "pillbox", "sandy", "paleto", None], vehicle_count),
        "fuel": rng.uniform(0, 100, vehicle_count).round(1),
        "engine_health": rng.uniform(200, 1_000, vehicle_count).round(0),
        "purchase_date": (
            pd.Timestamp("2026-06-01") + pd.to_timedelta(rng.integers(0, 150, vehicle_count), unit="D")
        ).strftime("%Y-%m-%d"),
    })
    vehicles.loc[rng.choice(vehicle_count, 35, replace=False), "fuel"] = 250
    vehicles.loc[rng.choice(vehicle_count, 25, replace=False), "engine_health"] = -1
    vehicles.loc[rng.choice(vehicle_count, 20, replace=False), "plate"] = vehicles["plate"].iloc[0]
    vehicles.loc[rng.choice(vehicle_count, 60, replace=False), "price_paid"] = np.nan

    performance_count = 24 * 30 * 4
    timestamps = pd.date_range("2026-06-01", periods=performance_count, freq="h")
    online = np.clip(
        40 + 45 * np.exp(-((timestamps.hour - 21) ** 2) / 18) + rng.normal(0, 6, performance_count),
        0,
        128,
    ).round(0)
    performance = pd.DataFrame({
        "timestamp": timestamps.strftime("%Y-%m-%d %H:%M:%S"),
        "players_online": online,
        "server_fps": np.clip(60 - online * .25 + rng.normal(0, 3, performance_count), 5, 60).round(1),
        "tickrate": np.clip(40 - online * .08 + rng.normal(0, 1.5, performance_count), 5, 40).round(1),
        "cpu_pct": np.clip(20 + online * .5 + rng.normal(0, 5, performance_count), 1, 100).round(1),
        "ram_mb": np.clip(3_000 + online * 18 + rng.normal(0, 150, performance_count), 1_500, 16_000).round(0),
        "heaviest_resource": rng.choice(
            ["qb-core", "qb-inventory", "qb-phone", "oxmysql", "qb-vehicleshop", "mlo_pack", "qb-policejob"],
            performance_count,
        ),
    })
    performance.loc[rng.choice(performance_count, 70, replace=False), ["server_fps", "cpu_pct"]] = np.nan
    performance.loc[rng.choice(performance_count, 15, replace=False), "server_fps"] = 0
    performance.loc[rng.choice(performance_count, 10, replace=False), "cpu_pct"] = 400
    performance.loc[rng.choice(performance_count, 20, replace=False), "players_online"] = -1
    performance = performance.drop(rng.choice(performance_count, 40, replace=False))

    datasets = {
        "players.csv": players,
        "sessions.csv": sessions,
        "transactions.csv": transactions,
        "vehicles.csv": vehicles,
        "server_performance.csv": performance,
    }
    for filename, dataframe in datasets.items():
        dataframe.to_csv(output_dir / filename, index=False)
    return {filename: len(dataframe) for filename, dataframe in datasets.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    counts = generate(args.output_dir, args.seed)
    print(f"Escenario sintético guardado en {args.output_dir.resolve()}")
    for filename, count in counts.items():
        print(f"- {filename}: {count:,} filas")


if __name__ == "__main__":
    main()
