import unittest
from pathlib import Path
import importlib.util

# Resolver ruta a strings_utils.py sin depender de PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # .../_LearnPyhton/Hello-Python
MODULE_PATH = PROJECT_ROOT / "Basic" / "strings_utils.py"

spec = importlib.util.spec_from_file_location("strings_utils", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)  # type: ignore[attr-defined]

normalize = module.normalize  # type: ignore[attr-defined]
length = module.length  # type: ignore[attr-defined]
to_upper = module.to_upper  # type: ignore[attr-defined]
replace_spaces_with_underscores = module.replace_spaces_with_underscores  # type: ignore[attr-defined]
count_vowels = module.count_vowels  # type: ignore[attr-defined]


class StringsUtilsTests(unittest.TestCase):
    def test_length_basic(self):
        self.assertEqual(length("Hola"), 4)

    def test_to_upper_basic(self):
        self.assertEqual(to_upper("Hola Python"), "HOLA PYTHON")

    def test_replace_spaces_basic(self):
        self.assertEqual(replace_spaces_with_underscores("hola mundo"), "hola_mundo")

    def test_normalize_trims_whitespace(self):
        self.assertEqual(normalize("  texto  "), "texto")

    def test_count_vowels_case_insensitive(self):
        self.assertEqual(count_vowels("AeiOu XYZ"), 5)

    def test_raises_on_non_string(self):
        with self.assertRaises(ValueError):
            to_upper(123)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            length(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()