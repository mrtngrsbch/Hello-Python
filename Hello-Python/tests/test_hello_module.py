import unittest
from pathlib import Path
import importlib.util

# Resolver ruta a hello_module.py sin depender de PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # .../_LearnPyhton/Hello-Python
MODULE_PATH = PROJECT_ROOT / "Basic" / "hello_module.py"

spec = importlib.util.spec_from_file_location("hello_module", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)  # type: ignore[attr-defined]

hello = module.hello  # type: ignore[attr-defined]
greet = module.greet  # type: ignore[attr-defined]


class HelloModuleTests(unittest.TestCase):
    def test_hello_returns_expected_message(self):
        self.assertEqual(hello(), "Hola Python")

    def test_greet_with_valid_name(self):
        self.assertEqual(greet("Brais"), "Encantado, Brais!")

    def test_greet_strips_whitespace(self):
        self.assertEqual(greet("  Ana  "), "Encantado, Ana!")

    def test_greet_raises_on_empty(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_greet_raises_on_non_string(self):
        with self.assertRaises(ValueError):
            greet(123)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()