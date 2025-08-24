"""
Clase 03 — Strings

Propósito:
- Concatenación, longitud y caracteres especiales (salto de línea, tabulaciones, escapes)
- Formateo de strings: format, %, concatenación y f-strings
- Desempaquetado de caracteres y slicing (incluye reversa)
- Métodos útiles: capitalize, upper, count, isnumeric, lower, startswith

Cómo ejecutar:
- python3 Hello-Python/Basic/03_strings.py

Nota: hay un bloque de práctica con input comentado para no bloquear pruebas.
"""

from __future__ import annotations

def demo_basicos() -> None:
    print("\n[Demostración] Básicos de strings")
    my_string = "Mi String"
    my_other_string = 'Mi otro String'

    # len mide la cantidad de caracteres
    print(len(my_string))
    print(len(my_other_string))

    # Concatenación simple con espacio
    print(my_string + " " + my_other_string)

    # Caracteres especiales y escapes
    print("Este es un String\ncon salto de línea")
    print("\tEste es un String con tabulación")
    print("\\tEste es un String \\n escapado")


def demo_formateo() -> None:
    print("\n[Demostración] Formateo de strings")
    name, surname, age = "Brais", "Moure", 35

    # 4 formas habituales de formatear
    print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
    print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
    print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
    print(f"Mi nombre es {name} {surname} y mi edad es {age}")


def demo_desempaquetado_y_slicing() -> None:
    print("\n[Demostración] Desempaquetado y slicing")
    language = "python"

    # Desempaquetado (requiere igual número de variables que caracteres)
    a, b, c, d, e, f = language
    print(a)  # p
    print(e)  # o

    # Slices (subcadenas): [inicio:fin:paso]
    print(language[1:3])   # yt (desde índice 1 hasta 3 sin incluir)
    print(language[1:])    # ython (desde 1 hasta el final)
    print(language[-2])    # o (índices negativos desde el final)
    print(language[0:6:2]) # pto (salto de 2 en 2)

    # Reversa rápida
    print(language[::-1])  # nohtyp


def demo_metodos() -> None:
    print("\n[Demostración] Métodos útiles")
    language = "python"
    print(language.capitalize())
    print(language.upper())
    print(language.count("t"))
    print(language.isnumeric())
    print("1".isnumeric())
    print(language.lower())
    print(language.lower().isupper())  # False, porque lower() produce minúsculas
    print(language.startswith("Py"))   # False: comienza con "py" en minúsculas
    print("Py" == "py")               # False: comparación sensible a mayúsculas


if __name__ == "__main__":
    demo_basicos()
    demo_formateo()
    demo_desempaquetado_y_slicing()
    demo_metodos()

    # ----------------------------------------------
    # Práctica guiada (opcional)
    # 1) Pide al usuario una frase y:
    #    - Muestra su longitud con len(...)
    #    - Imprime su versión en mayúsculas con .upper()
    #    - Reemplaza espacios por guiones bajos con .replace(" ", "_")
    # 2) Extrae y muestra los 3 primeros caracteres y los 3 últimos con slicing.
    # 3) Comprueba si la frase comienza por "Py" (startswith) y si contiene "py" (in).
    #
    # Descomenta y prueba:
    # frase = input("Escribe una frase: ")
    # print("Longitud:", len(frase))
    # print("MAYÚSCULAS:", frase.upper())
    # print("Con guiones bajos:", frase.replace(" ", "_"))
    # print("Primeros 3:", frase[:3], "| Últimos 3:", frase[-3:])
    # print("¿Empieza por 'Py'?:", frase.startswith("Py"))
    # print("¿Contiene 'py'?:", "py" in frase)

    # Checklist mental
    # - Las cadenas son inmutables: cada transformación devuelve un string nuevo.
    # - Slicing no incluye el índice final (semiabierto: [inicio:fin)).
    # - f-strings son la forma más legible de formatear en Python moderno.
    # - startswith/endswith y el operador in son aliados para búsquedas.
