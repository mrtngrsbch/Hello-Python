import unittest
from pathlib import Path
import importlib.util

# Resolver ruta a sets_utils.py sin depender de PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "Basic" / "sets_utils.py"

spec = importlib.util.spec_from_file_location("sets_utils", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)  # type: ignore[attr-defined]

new_set_from_iterable = module.new_set_from_iterable  # type: ignore[attr-defined]
add = module.add  # type: ignore[attr-defined]
remove = module.remove  # type: ignore[attr-defined]
discard = module.discard  # type: ignore[attr-defined]
contains = module.contains  # type: ignore[attr-defined]
union = module.union  # type: ignore[attr-defined]
intersection = module.intersection  # type: ignore[attr-defined]
difference = module.difference  # type: ignore[attr-defined]
symmetric_difference = module.symmetric_difference  # type: ignore[attr-defined]


class SetsUtilsTests(unittest.TestCase):
    def test_creation_removes_duplicates(self):
        s = new_set_from_iterable([1, 2, 2, 3, 1])
        self.assertEqual(s, {1, 2, 3})

    def test_add_and_contains_are_pure(self):
        base = {1, 2}
        s1 = add(base, 2)  # añadir existente no cambia el contenido
        s2 = add(base, 3)
        self.assertEqual(base, {1, 2})  # sin mutación
        self.assertEqual(s1, {1, 2})
        self.assertEqual(s2, {1, 2, 3})
        self.assertTrue(contains(s2, 3))
        self.assertFalse(contains(base, 3))

    def test_remove_and_discard(self):
        base = {1, 2}
        s = remove(base, 2)
        self.assertEqual(s, {1})
        with self.assertRaises(KeyError):
            remove(base, 5)
        self.assertEqual(discard(base, 5), {1, 2})  # no error si no existe

    def test_set_operations(self):
        a, b = {1, 2}, {2, 3}
        self.assertEqual(union(a, b), {1, 2, 3})
        self.assertEqual(intersection(a, b), {2})
        self.assertEqual(difference(a, b), {1})
        self.assertEqual(symmetric_difference(a, b), {1, 3})

    def test_type_validation(self):
        with self.assertRaises(ValueError):
            union(123, {1})  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            intersection({1}, "x")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()