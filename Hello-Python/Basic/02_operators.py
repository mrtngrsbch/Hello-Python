"""
Clase 03 — Operadores (aritméticos, comparación y lógicos)

Propósito:
- Practicar operadores aritméticos: +, -, *, /, //, %, **
- Comparaciones: ==, !=, >, >=, <, <= (incluye strings)
- Lógicos: and, or, not (usa paréntesis si hay duda de precedencia)
- Casos mixtos con strings (concatenación y repetición)

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Basic/02_operators.py

Notas:
- La división por cero lanza ZeroDivisionError.
- Con strings: "+" concatena, "*" repite (solo con enteros).
"""


def demo_aritmeticos() -> None:
    """Demostración de operadores aritméticos y precedencia básica."""
    print("-- Aritméticos --")
    print(3 + 4)        # suma -> 7
    print(3 - 4)        # resta -> -1
    print(3 * 4)        # multiplicación -> 12
    print(3 / 4)        # división (float) -> 0.75
    print(10 % 3)       # módulo (resto) -> 1
    print(10 // 3)      # división entera (floor) -> 3
    print(2 ** 3)       # potencia -> 8
    print(2 ** 3 + 3 - 7 / 1 // 4)  # precedencia mixta


def demo_strings_operadores() -> None:
    """Uso de operadores con strings: concatenación y repetición."""
    print("-- Strings y Operadores --")
    print("Hola " + "Python " + "¿Qué tal?")
    print("Hola " + str(5))
    print("Hola " * 5)
    print("Hola " * (2 ** 3))
    my_float = 2.5 * 2
    print("Hola " * int(my_float))  # convertir a int para repetir


def demo_comparacion() -> None:
    """Comparaciones con números y cadenas (lexicográficas)."""
    print("-- Comparación --")
    print(3 > 4)
    print(3 < 4)
    print(3 >= 4)
    print(4 <= 4)
    print(3 == 4)
    print(3 != 4)

    # Comparaciones de strings: orden lexicográfico (Unicode)
    print("Hola" > "Python")
    print("Hola" < "Python")
    print("aaaa" >= "abaa")  # compara carácter a carácter
    print(len("aaaa") >= len("abaa"))  # alternativa: compara por longitud
    print("Hola" <= "Python")
    print("Hola" == "Hola")
    print("Hola" != "Python")


def demo_logicos() -> None:
    """Operadores lógicos: and, or, not (con ejemplos de precedencia)."""
    print("-- Lógicos --")
    # Álgebra de Boole: and, or, not
    print(3 > 4 and "Hola" > "Python")
    print(3 > 4 or "Hola" > "Python")
    print(3 < 4 and "Hola" < "Python")
    print(3 < 4 or "Hola" > "Python")
    print(3 < 4 or ("Hola" > "Python" and 4 == 4))
    print(not (3 > 4))


# Práctica guiada (comentada para no interrumpir pruebas automáticas)
# 1) Calcula el precio final de un producto:
#    - precio_base = 100, descuento = 15% (aplica primero), IVA = 21% (después)
#    - Muestra el total final (usa paréntesis para claridad)
# 2) Dadas dos cadenas s1, s2, muestra cuál es lexicográficamente mayor y
#    cuál es más larga (usa > y len()).
# 3) Con tres booleanos a, b, c, evalúa: (a and b) or (not c) y explica el resultado.
# Checklist mental (comentado)
# - Aritméticos: +, -, *, /, //, %, ** (cuidado división por cero)
# - Comparación: ==, !=, >, >=, <, <=
# - Lógicos: and, or, not + paréntesis para precedencia
# - Strings: + concatena, * repite (solo enteros)
# - ¿Expresiones densas? Separa en variables intermedias para legibilidad


if __name__ == "__main__":
    demo_aritmeticos()
    demo_strings_operadores()
    demo_comparacion()
    demo_logicos()
