"""Compile and exercise the original two-integer addition CLI."""

import pathlib
import shutil
import subprocess
import tempfile
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "add.cpp"


@unittest.skipUnless(shutil.which("g++"), "g++ is required for C++ tests")
class AddExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.binary = pathlib.Path(cls.temp_dir.name) / "add"
        subprocess.run(
            ["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror", "-pedantic", str(SOURCE), "-o", str(cls.binary)],
            check=True,
            capture_output=True,
            text=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()

    def run_program(self, data):
        return subprocess.run([str(self.binary)], input=data, capture_output=True, text=True)

    def test_positive_integers(self):
        run = self.run_program("2 3\n")
        self.assertEqual(run.returncode, 0)
        self.assertEqual(run.stdout, "the addition result = 5\n")
        self.assertEqual(run.stderr, "")

    def test_negative_and_zero(self):
        run = self.run_program("-6 0\n")
        self.assertEqual((run.returncode, run.stdout), (0, "the addition result = -6\n"))

    def test_valid_int_inputs_with_sum_beyond_int_range(self):
        run = self.run_program("2147483647 2147483647\n")
        self.assertEqual((run.returncode, run.stdout), (0, "the addition result = 4294967294\n"))

    def test_invalid_input(self):
        for data in ("", "2\n", "1 nope\n"):
            with self.subTest(data=data):
                run = self.run_program(data)
                self.assertNotEqual(run.returncode, 0)
                self.assertEqual(run.stdout, "")
                self.assertIn("Expected two integers", run.stderr)


if __name__ == "__main__":
    unittest.main()
