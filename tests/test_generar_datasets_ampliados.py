import tempfile
import unittest
from pathlib import Path

import pandas as pd

from scripts.generar_datasets_ampliados import generate


class GenerateExpandedDatasetsTests(unittest.TestCase):
    def test_generation_is_deterministic_and_creates_five_tables(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            first_counts = generate(output, seed=42)
            first_content = {
                path.name: path.read_bytes()
                for path in output.glob("*.csv")
            }
            second_counts = generate(output, seed=42)
            second_content = {
                path.name: path.read_bytes()
                for path in output.glob("*.csv")
            }

        self.assertEqual(first_counts, second_counts)
        self.assertEqual(first_content, second_content)
        self.assertEqual(
            first_counts,
            {
                "players.csv": 1515,
                "sessions.csv": 8000,
                "transactions.csv": 12000,
                "vehicles.csv": 2200,
                "server_performance.csv": 2840,
            },
        )

    def test_synthetic_ids_and_seeded_quality_cases_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            generate(output)
            players = pd.read_csv(output / "players.csv", dtype={"discord_id": "string"})
            sessions = pd.read_csv(output / "sessions.csv")
            transactions = pd.read_csv(output / "transactions.csv", dtype={"amount": "string"})
            vehicles = pd.read_csv(output / "vehicles.csv")
            performance = pd.read_csv(output / "server_performance.csv")

        self.assertTrue(players["license"].dropna().str.startswith("SIM_LICENSE:").all())
        self.assertTrue(players["discord_id"].dropna().str.startswith("SIM_DISCORD_").all())
        self.assertEqual(players["player_id"].duplicated().sum(), 15)
        self.assertEqual(sessions["player_id"].gt(1500).sum(), 30)
        self.assertEqual(sessions["duration_min"].eq("unknown").sum(), 10)
        self.assertEqual(transactions["amount"].str.contains(r"[$,]", na=False).sum(), 15)
        self.assertEqual(vehicles["plate"].duplicated().sum(), 20)
        self.assertGreater(performance["players_online"].lt(0).sum(), 0)


if __name__ == "__main__":
    unittest.main()
