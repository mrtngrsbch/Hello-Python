import unittest
from pathlib import Path
import importlib.util

# Resolver ruta a dicts_utils.py sin depender de PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "Basic" / "dicts_utils.py"

spec = importlib.util.spec_from_file_location("dicts_utils", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)  # type: ignore[attr-defined]

create_dict_from_pairs = module.create_dict_from_pairs  # type: ignore[attr-defined]
get_value = module.get  # type: ignore[attr-defined]
has_key = module.has_key  # type: ignore[attr-defined]
set_item = module.set_item  # type: ignore[attr-defined]
remove = module.remove  # type: ignore[attr-defined]
discard = module.discard  # type: ignore[attr-defined]
keys_list = module.keys_list  # type: ignore[attr-defined]
values_list = module.values_list  # type: ignore[attr-defined]
items_list = module.items_list  # type: ignore[attr-defined]
update_dict = module.update  # type: ignore[attr-defined]


class DictsUtilsTests(unittest.TestCase):
    def test_create_and_set_item_are_pure(self):
        d = create_dict_from_pairs([("a", 1), ("b", 2)])
        self.assertEqual(d, {"a": 1, "b": 2})
        base = {"x": 10}
        d2 = set_item(base, "y", 20)
        self.assertEqual(base, {"x": 10})  # sin mutación
        self.assertEqual(d2, {"x": 10, "y": 20})

    def test_get_and_has_key(self):
        d = {"a": 1}
        self.assertEqual(get_value(d, "a"), 1)
        self.assertIsNone(get_value(d, "b"))
        self.assertEqual(get_value(d, "b", 0), 0)
        self.assertTrue(has_key(d, "a"))
        self.assertFalse(has_key(d, "z"))

    def test_remove_and_discard(self):
        d = {"a": 1, "b": 2}
        d2, val = remove(d, "a")
        self.assertEqual(val, 1)
        self.assertEqual(d2, {"b": 2})
        with self.assertRaises(KeyError):
            remove(d, "missing")
        d3, val2 = discard(d, "missing", default=-1)
        self.assertEqual(val2, -1)
        self.assertEqual(d3, d)

    def test_lists_views_and_update(self):
        d = {"a": 1, "b": 2}
        self.assertEqual(set(keys_list(d)), {"a", "b"})
        self.assertEqual(set(values_list(d)), {1, 2})
        self.assertEqual(set(items_list(d)), {("a", 1), ("b", 2)})
        d2 = update_dict(d, {"b": 20, "c": 3})
        self.assertEqual(d2, {"a": 1, "b": 20, "c": 3})
        self.assertEqual(d, {"a": 1, "b": 2})  # sin mutación

    def test_type_validation(self):
        with self.assertRaises(ValueError):
            get_value(123, "a")  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            set_item("not a dict", "k", 1)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            update_dict({"a": 1}, [1, 2])  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            create_dict_from_pairs([("a", 1, 2)])  # type: ignore[list-item]


if __name__ == "__main__":
    unittest.main()