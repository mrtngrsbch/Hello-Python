"""
Clase 03 — Lambdas (funciones anónimas)

Propósito pedagógico:
- Introducir el concepto de funciones lambda en Python.
- Practicar su uso en operaciones simples y como retornos de funciones.

Cómo ejecutar:
- python3 Hello-Python/Intermediate/03_lambdas.py
"""

from __future__ import annotations


if __name__ == "__main__":
    sum_two_values = lambda first_value, second_value: first_value + second_value
    print(sum_two_values(2, 4))

    multiply_values = lambda first_value, second_value: first_value * second_value - 3
    print(multiply_values(2, 4))

    def sum_three_values(value: int) -> callable:
        return lambda first_value, second_value: first_value + second_value + value

    print(sum_three_values(5)(2, 4))