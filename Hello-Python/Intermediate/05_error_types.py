"""
Clase 05 — Error Types (tipos de errores)

Propósito pedagógico:
- Identificar y comprender los errores comunes en Python.
- Practicar la depuración y manejo de errores.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Intermediate/05_error_types.py
"""

from __future__ import annotations
from math import pi
import math


if __name__ == "__main__":
    # SyntaxError
    # print "¡Hola comunidad!" # Descomentar para Error
    print("¡Hola comunidad!")

    # NameError
    language = "Spanish"  # Comentar para Error
    print(language)

    # IndexError
    my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
    print(my_list[0])
    print(my_list[4])
    print(my_list[-1])
    # print(my_list[5]) # Descomentar para Error

    # ModuleNotFoundError
    # import maths # Descomentar para Error

    # AttributeError
    # print(math.PI) # Descomentar para Error
    print(math.pi)

    # KeyError
    my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
    print(my_dict["Edad"])
    # print(my_dict["Apelido"]) # Descomentar para Error
    print(my_dict["Apellido"])

    # TypeError
    # print(my_list["0"]) # Descomentar para Error
    print(my_list[0])
    print(my_list[False])

    # ImportError
    # from math import PI # Descomentar para Error
    print(pi)

    # ValueError
    # my_int = int("10 Años") # Descomentar para Error
    my_int = int("10")
    print(type(my_int))

    # ZeroDivisionError
    # print(4/0) # Descomentar para Error
    print(4/2)
