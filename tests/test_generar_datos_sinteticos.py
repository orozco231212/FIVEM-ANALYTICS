import csv
import tempfile
import unittest
from pathlib import Path

from scripts.generar_datos_sinteticos import generate


class GenerateSyntheticDataTests(unittest.TestCase):
    def test_generation_is_deterministic_and_contains_expected_datasets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            first_counts = generate(output, seed=123)
            first_content = {
                path.relative_to(output).as_posix(): path.read_bytes()
                for path in output.rglob("*.csv")
            }
            second_counts = generate(output, seed=123)
            second_content = {
                path.relative_to(output).as_posix(): path.read_bytes()
                for path in output.rglob("*.csv")
            }

        self.assertEqual(first_counts, second_counts)
        self.assertEqual(first_content, second_content)
        self.assertEqual(
            set(first_counts),
            {
                "sesiones_fivem_sinteticas.csv",
                "transacciones_economicas_sinteticas.csv",
                "actividad_jugadores_sintetica.csv",
                "rendimiento_servidor_sintetico.csv",
            },
        )

    def test_deliberate_data_quality_cases_are_present(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory)
            generate(output)
            with (output / "fivem" / "sesiones_fivem_sinteticas.csv").open(
                encoding="utf-8-sig", newline=""
            ) as file:
                sessions = list(csv.DictReader(file))
            with (output / "fivem" / "transacciones_economicas_sinteticas.csv").open(
                encoding="utf-8-sig", newline=""
            ) as file:
                transactions = list(csv.DictReader(file))
            with (output / "fivem" / "actividad_jugadores_sintetica.csv").open(
                encoding="utf-8-sig", newline=""
            ) as file:
                activities = list(csv.DictReader(file))
            with (output / "fivem" / "rendimiento_servidor_sintetico.csv").open(
                encoding="utf-8-sig", newline=""
            ) as file:
                performance = list(csv.DictReader(file))

        self.assertEqual(len(sessions), 5001)
        self.assertEqual(sessions[4]["duration_minutes"], "")
        self.assertEqual(sessions[16]["duration_minutes"], "noventa")
        self.assertEqual(sessions[24]["duration_minutes"], "-8")
        self.assertEqual(sessions[-1], sessions[69])
        self.assertEqual(sessions[54]["zone"], "")
        self.assertEqual(sessions[98]["disconnected_at"], "fecha_invalida")
        self.assertEqual(transactions[12]["amount"], "")
        self.assertEqual(transactions[37]["amount"], "sin_dato")
        self.assertEqual(transactions[83]["amount"], "-250")
        self.assertEqual(transactions[-1], transactions[119])
        self.assertEqual(len(activities), 5001)
        self.assertEqual(activities[31]["zone"], "")
        self.assertEqual(activities[-1], activities[149])
        self.assertEqual(len(performance), 1441)
        self.assertEqual(performance[20]["server_fps"], "")
        self.assertEqual(performance[72]["cpu_percent"], "145")
        self.assertEqual(performance[101]["memory_percent"], "sin_dato")
        self.assertEqual(performance[-1], performance[199])


if __name__ == "__main__":
    unittest.main()
