"""
Funciones utilitarias para trabajar con strings (Clase 02).
Enfoque: funciones puras, sin I/O, fáciles de probar con unittest.

Ejemplos rápidos:
>>> normalize("  hola  ")
'hola'
>>> length("Python")
6
>>> to_upper("hola")
'HOLA'
>>> replace_spaces_with_underscores("hola mundo")
'hola_mundo'
>>> count_vowels("Python")
1

Recuerda: los strings son inmutables; cada transformación devuelve una nueva cadena.
Si pasas un valor que no es str, levantamos ValueError para guiar al alumno.
"""
from typing import Any

VOWELS = set("aeiou")


def _ensure_str(value: Any) -> str:
    """Valida que value sea str y devuelve el mismo valor.

    Separa la validación en una función pequeña para reutilizarla.
    """
    if not isinstance(value, str):
        raise ValueError("Se esperaba un str")
    return value


def normalize(text: Any) -> str:
    """Devuelve el texto sin espacios al inicio/fin usando strip()."""
    s = _ensure_str(text)
    return s.strip()


def length(text: Any) -> int:
    """Longitud del texto (len)."""
    s = _ensure_str(text)
    return len(s)


def to_upper(text: Any) -> str:
    """Convierte texto a mayúsculas (upper)."""
    s = _ensure_str(text)
    return s.upper()


def replace_spaces_with_underscores(text: Any) -> str:
    """Reemplaza espacios por guiones bajos usando replace."""
    s = _ensure_str(text)
    return s.replace(" ", "_")


def count_vowels(text: Any) -> int:
    """Cuenta vocales (a, e, i, o, u) sin diferenciar mayúsculas/minúsculas."""
    s = _ensure_str(text).lower()
    return sum(1 for ch in s if ch in VOWELS)