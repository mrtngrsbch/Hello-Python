"""
Clase 04 — Higher Order Functions (funciones de orden superior)

Propósito pedagógico:
- Introducir el concepto de funciones de orden superior.
- Practicar su uso con funciones integradas como map, filter y reduce.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Intermediate/04_higher_order_functions.py
"""

from __future__ import annotations
from functools import reduce


def sum_one(value: int) -> int:
    return value + 1


def sum_five(value: int) -> int:
    return value + 5


def sum_two_values_and_add_value(first_value: int, second_value: int, f_sum: callable) -> int:
    return f_sum(first_value + second_value)


def sum_ten(original_value: int) -> callable:
    def add(value: int) -> int:
        return value + 10 + original_value
    return add


def multiply_two(number: int) -> int:
    return number * 2


def filter_greater_than_ten(number: int) -> bool:
    return number > 10


def sum_two_values(first_value: int, second_value: int) -> int:
    return first_value + second_value


if __name__ == "__main__":
    print(sum_two_values_and_add_value(5, 2, sum_one))
    print(sum_two_values_and_add_value(5, 2, sum_five))

    add_closure = sum_ten(1)
    print(add_closure(5))
    print((sum_ten(5))(1))

    numbers = [2, 5, 10, 21, 3, 30]

    print(list(map(multiply_two, numbers)))
    print(list(map(lambda number: number * 2, numbers)))

    print(list(filter(filter_greater_than_ten, numbers)))
    print(list(filter(lambda number: number > 10, numbers)))

    print(reduce(sum_two_values, numbers))
