"""
Funciones utilitarias para Clase 03 — Operadores.
Enfoque: funciones puras (sin I/O) y fáciles de testear.

Ejemplos rápidos:
>>> add(2, 3)
5
>>> int_div(7, 2)
3
>>> mod(7, 2)
1
>>> power(2, 3)
8
>>> is_greater(3, 2)
True
>>> logical_and(True, False)
False

Nota: div() lanza ZeroDivisionError si b == 0 (comportamiento estándar de Python).
"""
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Suma a + b."""
    return a + b


def sub(a: Number, b: Number) -> Number:
    """Resta a - b."""
    return a - b


def mul(a: Number, b: Number) -> Number:
    """Multiplicación a * b."""
    return a * b


def div(a: Number, b: Number) -> float:
    """División a / b. Puede lanzar ZeroDivisionError."""
    return a / b


def int_div(a: Number, b: Number) -> int:
    """División entera a // b (floor)."""
    return int(a // b)


def mod(a: Number, b: Number) -> Number:
    """Resto de la división a % b."""
    return a % b


def power(a: Number, b: Number) -> Number:
    """Potencia a ** b."""
    return a ** b


def is_equal(a: Number, b: Number) -> bool:
    """Devuelve True si a == b."""
    return a == b


def is_greater(a: Number, b: Number) -> bool:
    """Devuelve True si a > b."""
    return a > b


def is_less_or_equal(a: Number, b: Number) -> bool:
    """Devuelve True si a <= b."""
    return a <= b


def logical_and(x: bool, y: bool) -> bool:
    """Devuelve x and y."""
    return x and y


def logical_or(x: bool, y: bool) -> bool:
    """Devuelve x or y."""
    return x or y


def logical_not(x: bool) -> bool:
    """Devuelve not x."""
    return not x