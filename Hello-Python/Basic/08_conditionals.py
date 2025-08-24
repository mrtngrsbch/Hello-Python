"""
Clase 08 — Condicionales (tomar decisiones en el código)

Propósito pedagógico:
- Entender cómo usar `if`, `elif`, `else` y `not` para controlar el flujo.
- Practicar comparaciones y combinaciones lógicas (`and`, `or`).
- Evitar errores típicos: ramas inalcanzables, comparaciones mal planteadas, truthiness.

Cómo ejecutar:
- python3 Hello-Python/Basic/08_conditionals.py
"""

from __future__ import annotations


def demo_basicos() -> None:
    print("\n== Básicos ==")
    condicion = False
    if condicion:  # igual que: if condicion == True
        print("Se ejecuta la condición del if")

    valor = 5 * 5
    if valor == 10:
        print("valor == 10")
    elif valor == 25:
        print("valor == 25")
    else:
        print("valor distinto de 10 y 25")


def demo_rangos_y_logica() -> None:
    print("\n== Rangos y lógica ==")
    x = 15
    if x > 10 and x < 20:
        print("Es mayor que 10 y menor que 20")
    elif x == 20 or x == 10:
        print("Es límite del rango")
    else:
        print("Fuera de rango")


def demo_truthiness() -> None:
    print("\n== Truthiness y cadenas vacías ==")
    s = ""
    if not s:
        print("Cadena vacía")
    if s == "Mi cadena de textoooooo":
        print("Coincide exactamente")


if __name__ == "__main__":
    demo_basicos()
    demo_rangos_y_logica()
    demo_truthiness()

    # Bloque de práctica guiada (descomentarlo si quieres practicar)
    # Ejercicio: pide una edad y clasifícala en: menor (<18), adulto (18–64), senior (>=65).
    # edad = int(input("Edad: "))
    # if edad < 18:
    #     print("menor")
    # elif edad < 65:
    #     print("adulto")
    # else:
    #     print("senior")

    # Checklist mental
    # - Orden de condiciones: coloca primero las más restrictivas
    # - Combina con `and`/`or` conscientemente
    # - Usa `not` para negar truthiness ("", 0, None son falsy)
    # - Compara valores explícitamente cuando la intención sea igualdad
