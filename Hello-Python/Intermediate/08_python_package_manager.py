"""
Clase 08 — Python Package Manager (gestor de paquetes)

Propósito pedagógico:
- Aprender a gestionar paquetes externos con pip.
- Practicar la importación y uso de paquetes populares.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Intermediate/08_python_package_manager.py
"""

from __future__ import annotations
import pandas
from mypackage import arithmetics
import requests
import numpy


def demo_package_manager() -> None:
    print(numpy.version.version)

    numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
    print(type(numpy_array))
    print(numpy_array * 2)

    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    print(response)
    print(response.status_code)
    print(response.json())

    print(arithmetics.sum_two_values(1, 4))


if __name__ == "__main__":
    demo_package_manager()
