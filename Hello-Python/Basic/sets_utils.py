"""
Utilidades puras para trabajar con conjuntos (Clase 06 — Sets).
- Enfoque funcional: NO mutamos los sets de entrada; devolvemos nuevos sets.
- Validamos tipos para dar feedback claro al alumno.

Ejemplos rápidos:
>>> new_set_from_iterable([1, 2, 2, 3])
{1, 2, 3}
>>> add({1, 2}, 3)
{1, 2, 3}
>>> discard({1, 2}, 5)
{1, 2}
>>> union({1, 2}, {2, 3})
{1, 2, 3}
"""
from typing import Any, Iterable, Set


def _ensure_set(s: Any) -> Set[Any]:
    if not isinstance(s, set):
        raise ValueError("Se esperaba un set como primer argumento")
    return s  # type: ignore[return-value]


def new_set_from_iterable(it: Iterable[Any]) -> Set[Any]:
    """Crea un set a partir de un iterable, eliminando duplicados."""
    try:
        return set(it)
    except TypeError as e:
        # Elementos no hashables, por ejemplo listas dentro de it
        raise ValueError("Los elementos deben ser hashables para formar un set") from e


def add(s: Any, item: Any) -> Set[Any]:
    """Devuelve un nuevo set con item añadido (sin mutar s)."""
    base = _ensure_set(s)
    nuevo = set(base)
    nuevo.add(item)
    return nuevo


def remove(s: Any, item: Any) -> Set[Any]:
    """Devuelve un nuevo set sin item. Lanza KeyError si no existe (comportamiento estricto)."""
    base = _ensure_set(s)
    if item not in base:
        raise KeyError(item)
    nuevo = set(base)
    nuevo.remove(item)
    return nuevo


def discard(s: Any, item: Any) -> Set[Any]:
    """Devuelve un nuevo set sin item. Si no existe, no lanza error (modo seguro)."""
    base = _ensure_set(s)
    nuevo = set(base)
    if item in nuevo:
        nuevo.remove(item)
    return nuevo


def contains(s: Any, item: Any) -> bool:
    """True si item pertenece al set s."""
    base = _ensure_set(s)
    return item in base


def union(a: Any, b: Any) -> Set[Any]:
    """Unión de dos sets (a ∪ b)."""
    sa = _ensure_set(a)
    sb = _ensure_set(b)
    return sa.union(sb)


def intersection(a: Any, b: Any) -> Set[Any]:
    """Intersección de dos sets (a ∩ b)."""
    sa = _ensure_set(a)
    sb = _ensure_set(b)
    return sa.intersection(sb)


def difference(a: Any, b: Any) -> Set[Any]:
    """Diferencia de sets (a − b)."""
    sa = _ensure_set(a)
    sb = _ensure_set(b)
    return sa.difference(sb)


def symmetric_difference(a: Any, b: Any) -> Set[Any]:
    """Diferencia simétrica (elementos en uno u otro, pero no en ambos)."""
    sa = _ensure_set(a)
    sb = _ensure_set(b)
    return sa.symmetric_difference(sb)