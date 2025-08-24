"""
Clase 07 — Regular Expressions (expresiones regulares)

Propósito pedagógico:
- Introducir el uso de expresiones regulares en Python.
- Practicar la búsqueda y manipulación de patrones en texto.

Cómo ejecutar:
- python3 Hello-Python/Intermediate/07_regular_expressions.py
"""

from __future__ import annotations
import re


def demo_regular_expressions() -> None:
    my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
    my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

    # match
    match = re.match("Esta es la lección", my_string, re.I)
    print(match)
    if match:
        start, end = match.span()
        print(my_string[start:end])

    match = re.match("Esta no es la lección", my_other_string)
    if match is not None:
        print(match)
        start, end = match.span()
        print(my_other_string[start:end])

    print(re.match("Expresiones Regulares", my_string))

    # search
    search = re.search("lección", my_string, re.I)
    print(search)
    if search:
        start, end = search.span()
        print(my_string[start:end])

    # findall
    findall = re.findall("lección", my_string, re.I)
    print(findall)

    # split
    print(re.split(":", my_string))

    # sub
    print(re.sub("[l|L]ección", "LECCIÓN", my_string))
    print(re.sub("Expresiones Regulares", "RegEx", my_string))

    # Regular Expressions Patterns
    pattern = r"[lL]ección"
    print(re.findall(pattern, my_string))

    pattern = r"[lL]ección|Expresiones"
    print(re.findall(pattern, my_string))

    pattern = r"[0-9]"
    print(re.findall(pattern, my_string))
    print(re.search(pattern, my_string))

    pattern = r"\d"
    print(re.findall(pattern, my_string))

    pattern = r"\D"
    print(re.findall(pattern, my_string))

    pattern = r"[l].*"
    print(re.findall(pattern, my_string))

    email = "mouredev@mouredev.com"
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    print(re.match(pattern, email))
    print(re.search(pattern, email))
    print(re.findall(pattern, email))

    email = "mouredev@mouredev.com.mx"
    print(re.findall(pattern, email))


if __name__ == "__main__":
    demo_regular_expressions()
