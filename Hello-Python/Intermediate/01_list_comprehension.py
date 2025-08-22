"""
Clase 01 — List Comprehension (listas por comprensión)

Propósito pedagógico:
- Crear listas de manera eficiente usando comprensión.
- Practicar transformaciones y operaciones básicas en listas.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Intermediate/01_list_comprehension.py
"""

from __future__ import annotations


def sum_five(number: int) -> int:
    return number + 5


if __name__ == "__main__":
    my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
    print(my_original_list)

    my_range = range(8)
    print(list(my_range))

    my_list = [i + 1 for i in range(8)]
    print(my_list)

    my_list = [i * 2 for i in range(8)]
    print(my_list)

    my_list = [i * i for i in range(8)]
    print(my_list)

    my_list = [sum_five(i) for i in range(8)]
    print(my_list)
