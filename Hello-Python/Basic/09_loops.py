"""
Clase 09 — Bucles (repetición controlada)

Propósito pedagógico:
- Usar `while` y `for` correctamente.
- Entender `break`, `continue` y la cláusula `else` de los bucles.
- Iterar sobre `list`, `tuple`, `set`, `dict` y sus vistas.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Basic/09_loops.py
"""

from __future__ import annotations


def demo_while_basico() -> None:
    print("\n== while básico ==")
    condicion = 0
    while condicion < 10:
        print(condicion)
        condicion += 2
    else:  # opcional
        print("Mi condición es mayor o igual que 10")


def demo_while_con_break() -> None:
    print("\n== while con break ==")
    condicion = 10
    while condicion < 20:
        condicion += 1
        if condicion == 15:
            print("Se detiene la ejecución")
            break
        print(condicion)


def demo_for_sobre_colecciones() -> None:
    print("\n== for sobre colecciones ==")
    my_list = [35, 24, 62, 52, 30, 30, 17]
    for e in my_list:
        print(e)

    my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
    for e in my_tuple:
        print(e)

    my_set = {"Brais", "Moure", 35}
    for e in my_set:
        print(e)

    my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
    for k in my_dict:
        print(k)
        if k == "Edad":
            break
    else:
        print("El bucle for para el diccionario ha finalizado")


def demo_for_con_continue_y_else() -> None:
    print("\n== for con continue y else ==")
    my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
    for k in my_dict:
        print(k)
        if k == "Edad":
            continue
        print("Se ejecuta")
    else:
        print("El bucle for para diccionario ha finalizado")


if __name__ == "__main__":
    demo_while_basico()
    demo_while_con_break()
    demo_for_sobre_colecciones()
    demo_for_con_continue_y_else()

    # Práctica guiada (opcional)
    # - Imprime los números del 1 al 100, pero salta los múltiplos de 3
    # - Recorre un diccionario de estudiantes y muestra solo los que tengan nota >= 7

    # Checklist mental
    # - ¿El bucle termina? (condición/contador en while)
    # - ¿Necesito `break` o `continue`? ¿Por qué?
    # - `for` sobre dicts itera por claves; usa .items() si necesitas clave y valor
