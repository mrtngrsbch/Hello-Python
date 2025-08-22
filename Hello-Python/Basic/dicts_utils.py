"""
Utilidades puras para trabajar con diccionarios (Clase 07 — Dicts).
- Enfoque funcional: NO mutamos los dicts de entrada; devolvemos nuevos dicts.
- Validamos tipos para feedback claro.

Ejemplos rápidos:
>>> create_dict_from_pairs([("a", 1), ("b", 2)])
{'a': 1, 'b': 2}
>>> set_item({"a": 1}, "b", 2)
{'a': 1, 'b': 2}
>>> remove({"a": 1, "b": 2}, "a")
({'b': 2}, 1)
"""
from typing import Any, Dict, Iterable, List, Tuple


def _ensure_dict(d: Any) -> Dict[Any, Any]:
    if not isinstance(d, dict):
        raise ValueError("Se esperaba un dict como primer argumento")
    return d  # type: ignore[return-value]


def create_dict_from_pairs(pairs: Iterable[Tuple[Any, Any]]) -> Dict[Any, Any]:
    """Crea un dict a partir de una secuencia de pares (clave, valor)."""
    try:
        return dict(pairs)
    except Exception as e:  # ValueError por pares inválidos, etc.
        raise ValueError("Se esperaban pares (clave, valor) válidos") from e


def get(d: Any, key: Any, default: Any = None) -> Any:
    """Obtiene d[key] o devuelve default si no existe."""
    base = _ensure_dict(d)
    return base.get(key, default)


def has_key(d: Any, key: Any) -> bool:
    """True si key está en d."""
    base = _ensure_dict(d)
    return key in base


def set_item(d: Any, key: Any, value: Any) -> Dict[Any, Any]:
    """Devuelve un nuevo dict con (key=value) sin mutar d."""
    base = _ensure_dict(d)
    nuevo = dict(base)
    nuevo[key] = value
    return nuevo


def remove(d: Any, key: Any) -> Tuple[Dict[Any, Any], Any]:
    """Elimina key de d y devuelve (nuevo_dict, valor). Lanza KeyError si no existe."""
    base = _ensure_dict(d)
    if key not in base:
        raise KeyError(key)
    nuevo = dict(base)
    val = nuevo.pop(key)
    return nuevo, val


def discard(d: Any, key: Any, default: Any = None) -> Tuple[Dict[Any, Any], Any]:
    """Elimina key si existe; si no, devuelve default. Nunca lanza error."""
    base = _ensure_dict(d)
    nuevo = dict(base)
    if key in nuevo:
        val = nuevo.pop(key)
        return nuevo, val
    return nuevo, default


def keys_list(d: Any) -> List[Any]:
    """Devuelve lista de claves (para comparar en tests usar set o sorted)."""
    base = _ensure_dict(d)
    return list(base.keys())


def values_list(d: Any) -> List[Any]:
    base = _ensure_dict(d)
    return list(base.values())


def items_list(d: Any) -> List[Tuple[Any, Any]]:
    base = _ensure_dict(d)
    return list(base.items())


def update(d: Any, updates: Dict[Any, Any]) -> Dict[Any, Any]:
    """Devuelve un nuevo dict con d actualizado por updates."""
    base = _ensure_dict(d)
    if not isinstance(updates, dict):
        raise ValueError("updates debe ser un dict")
    nuevo = dict(base)
    nuevo.update(updates)
    return nuevo