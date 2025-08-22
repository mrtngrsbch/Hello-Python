import unittest
from pathlib import Path
import importlib.util

# Resolver ruta a operators_utils.py sin depender de PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # .../_LearnPyhton/Hello-Python
MODULE_PATH = PROJECT_ROOT / "Basic" / "operators_utils.py"

spec = importlib.util.spec_from_file_location("operators_utils", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)  # type: ignore[attr-defined]

add = module.add  # type: ignore[attr-defined]
sub = module.sub  # type: ignore[attr-defined]
mul = module.mul  # type: ignore[attr-defined]
div = module.div  # type: ignore[attr-defined]
int_div = module.int_div  # type: ignore[attr-defined]
mod = module.mod  # type: ignore[attr-defined]
power = module.power  # type: ignore[attr-defined]
is_equal = module.is_equal  # type: ignore[attr-defined]
is_greater = module.is_greater  # type: ignore[attr-defined]
is_less_or_equal = module.is_less_or_equal  # type: ignore[attr-defined]
logical_and = module.logical_and  # type: ignore[attr-defined]
logical_or = module.logical_or  # type: ignore[attr-defined]
logical_not = module.logical_not  # type: ignore[attr-defined]


class OperatorsUtilsTests(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(div(8, 4), 2.0)
        self.assertEqual(int_div(7, 2), 3)
        self.assertEqual(mod(7, 2), 1)
        self.assertEqual(power(2, 3), 8)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)
        with self.assertRaises(ZeroDivisionError):
            int_div(1, 0)
        with self.assertRaises(ZeroDivisionError):
            mod(1, 0)

    def test_comparisons(self):
        self.assertTrue(is_equal(5, 5))
        self.assertTrue(is_greater(3, 2))
        self.assertTrue(is_less_or_equal(2, 2))
        self.assertTrue(is_less_or_equal(1, 2))

    def test_logical(self):
        self.assertFalse(logical_and(True, False))
        self.assertTrue(logical_or(False, True))
        self.assertTrue(logical_not(False))


if __name__ == "__main__":
    unittest.main()