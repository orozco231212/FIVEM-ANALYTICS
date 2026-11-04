"""Generate deterministic, clearly labeled FiveM-style sample datasets."""

from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


SEED = 20261104
START = datetime(2026, 9, 1)
DAYS = 60
PLAYER_COUNT = 350
SESSION_COUNT = 5000

JOBS = ("police", "mechanic", "ambulance", "taxi", "trucker", "unemployed")
ZONES = (
    "Legion Square",
    "Pillbox Hill",
    "Los Santos Customs",
    "Sandy Shores",
    "Vespucci Beach",
    "La Mesa",
)
ZONE_BY_JOB = {
    "police": ("Legion Square", "La Mesa", "Sandy Shores"),
    "mechanic": ("Los Santos Customs", "La Mesa", "Vespucci Beach"),
    "ambulance": ("Pillbox Hill", "Legion Square", "Sandy Shores"),
    "taxi": ("Legion Square", "Vespucci Beach", "Pillbox Hill"),
    "trucker": ("Sandy Shores", "La Mesa", "Vespucci Beach"),
    "unemployed": ZONES,
}


def _write_csv(path: Path, rows: list[dict[str, Any]], columns: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def generate(output_dir: Path, seed: int = SEED) -> dict[str, int]:
    """Create five reproducible CSV files and return their row counts."""
    rng = random.Random(seed)
    players = [f"SIM_PLAYER_{index:04d}" for index in range(1, PLAYER_COUNT + 1)]
    sessions: list[dict[str, Any]] = []
    transactions: list[dict[str, Any]] = []
    activities: list[dict[str, Any]] = []
    for index in range(SESSION_COUNT):
        player = rng.choice(players)
        job = rng.choices(JOBS, weights=(18, 19, 13, 16, 15, 19), k=1)[0]
        zone = rng.choice(ZONE_BY_JOB[job])
        started = START + timedelta(
            days=rng.randrange(DAYS),
            minutes=rng.randrange(24 * 60),
        )
        duration = rng.randint(15, 210)
        ended = started + timedelta(minutes=duration)
        session_id = f"SIM_SESSION_{index + 1:06d}"
        sessions.append({
            "session_id": session_id,
            "player_id": player,
            "connected_at": started.isoformat(sep=" "),
            "disconnected_at": ended.isoformat(sep=" "),
            "duration_minutes": duration,
            "job": job,
            "zone": zone,
            "peak_concurrent_players": rng.randint(8, 64),
        })
        activities.append({
            "event_id": f"SIM_EVENT_{index + 1:06d}",
            "session_id": session_id,
            "player_id": player,
            "event_at": (started + timedelta(minutes=rng.randint(1, duration))).isoformat(sep=" "),
            "activity": rng.choice(("job_shift", "vehicle_use", "store_purchase", "social_event")),
            "job": job,
            "zone": zone,
        })

        for _ in range(rng.randint(1, 4)):
            transaction_type = rng.choice(("income", "expense"))
            category = rng.choice(
                ("salary", "mission", "vehicle", "housing", "repair", "medical")
            )
            transactions.append({
                "transaction_id": f"SIM_TX_{len(transactions) + 1:07d}",
                "player_id": player,
                "transaction_at": (started + timedelta(minutes=rng.randint(0, duration))).isoformat(sep=" "),
                "transaction_type": transaction_type,
                "category": category,
                "amount": round(rng.uniform(100, 25000), 2),
                "job": job,
                "zone": zone,
            })

    performance: list[dict[str, Any]] = []
    for day in range(DAYS):
        for hour in range(24):
            online = rng.randint(5, 64)
            performance.append({
                "snapshot_at": (START + timedelta(days=day, hours=hour)).isoformat(sep=" "),
                "server_name": "FiveM Roleplay (simulado)",
                "online_players": online,
                "max_players": 64,
                "server_fps": round(max(20, 72 - online * 0.48 + rng.uniform(-5, 5)), 2),
                "cpu_percent": round(min(96, 22 + online * 0.9 + rng.uniform(-8, 8)), 2),
                "memory_percent": round(min(94, 38 + online * 0.55 + rng.uniform(-6, 6)), 2),
            })

    # Seeded defects are intentional so the quality checks have evidence to find.
    sessions[4]["duration_minutes"] = ""
    sessions[16]["duration_minutes"] = "noventa"
    sessions[24]["duration_minutes"] = -8
    sessions[54]["zone"] = ""
    sessions[98]["disconnected_at"] = "fecha_invalida"
    sessions.append(sessions[69].copy())

    transactions[12]["amount"] = ""
    transactions[37]["amount"] = "sin_dato"
    transactions[83]["amount"] = -250
    transactions.append(transactions[119].copy())

    activities[31]["zone"] = ""
    activities.append(activities[149].copy())

    performance[20]["server_fps"] = ""
    performance[72]["cpu_percent"] = 145
    performance[101]["memory_percent"] = "sin_dato"
    performance.append(performance[199].copy())

    datasets = {
        "sesiones_fivem_sinteticas.csv": (
            "fivem",
            sessions,
            (
                "session_id", "player_id", "connected_at", "disconnected_at",
                "duration_minutes", "job", "zone", "peak_concurrent_players",
            ),
        ),
        "transacciones_economicas_sinteticas.csv": (
            "fivem",
            transactions,
            (
                "transaction_id", "player_id", "transaction_at", "transaction_type",
                "category", "amount", "job", "zone",
            ),
        ),
        "actividad_jugadores_sintetica.csv": (
            "fivem",
            activities,
            ("event_id", "session_id", "player_id", "event_at", "activity", "job", "zone"),
        ),
        "rendimiento_servidor_sintetico.csv": (
            "fivem",
            performance,
            (
                "snapshot_at", "server_name", "online_players", "max_players",
                "server_fps", "cpu_percent", "memory_percent",
            ),
        ),
    }

    for filename, (source, rows, columns) in datasets.items():
        _write_csv(output_dir / source / filename, rows, columns)
    return {filename: len(rows) for filename, (_, rows, _) in datasets.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "examples",
    )
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    counts = generate(args.output_dir, args.seed)
    print(f"Datos sintéticos creados en: {args.output_dir.resolve()}")
    for filename, count in counts.items():
        print(f"- {filename}: {count:,} filas")


if __name__ == "__main__":
    main()
