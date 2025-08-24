"""
Clase 10 — Funciones (definición, parámetros y retorno)

Propósito pedagógico:
- Definir y llamar funciones con parámetros posicionales, por nombre y por defecto.
- Distinguir entre retornar valores y sólo imprimir.
- Usar *args para número variable de argumentos.

Cómo ejecutar:
- python3 Hello-Python/Basic/10_functions.py
"""

from __future__ import annotations

def my_function() -> None:
    print("Esto es una función")


# Función con parámetros de entrada/argumentos

def sum_two_values(first_number: int | float | str, second_number: int | float | str) -> None:
    print(first_number + second_number)


# Función con parámetros y retorno

def sum_two_values_with_return(first_number: int | float, second_number: int | float) -> int | float:
    return first_number + second_number


# Parámetros por clave

def print_name(name: str, surname: str) -> None:
    print(f"{name} {surname}")


# Parámetros por defecto

def print_name_with_default(name: str, surname: str, alias: str = "Sin alias") -> None:
    print(f"{name} {surname} {alias}")


# Parámetros arbitrarios (*args)

def print_upper_texts(*texts: str) -> None:
    for text in texts:
        print(text.upper())


# Demostraciones

def demo_basico_y_parametros() -> None:
    print("\n== Básico y parámetros ==")
    my_function()
    my_function()
    my_function()
    sum_two_values(5, 7)
    sum_two_values(54754, 71231)
    sum_two_values("5", "7")
    sum_two_values(1.4, 5.2)


def demo_retorno_vs_print() -> None:
    print("\n== Retorno vs print ==")
    # Antes se usaba `sum_two_values` (que solo imprime) y devolvía None en my_result
    # Usamos la función que retorna el resultado para poder reutilizarlo
    my_result = sum_two_values_with_return(1.4, 5.2)
    print(my_result)
    my_result = sum_two_values_with_return(10, 5)
    print(my_result)


def demo_keywords_defaults_y_args() -> None:
    print("\n== Keywords, defaults y *args ==")
    print_name(surname="Moure", name="Brais")
    print_name_with_default("Brais", "Moure")
    print_name_with_default("Brais", "Moure", "MoureDev")
    print_upper_texts("Hola", "Python", "MoureDev")
    print_upper_texts("Hola")


if __name__ == "__main__":
    demo_basico_y_parametros()
    demo_retorno_vs_print()
    demo_keywords_defaults_y_args()

    # Práctica guiada (opcional)
    # - Crea una función que reciba **kwargs y muestre claves y valores ordenados alfabéticamente.
    # - Escribe una función pura que reciba una lista de números y devuelva la media (sin prints), y otra que la formatee para imprimir.

    # Checklist mental
    # - ¿Necesito retornar un valor para reutilizarlo más tarde?
    # - ¿Debería usar parámetros por defecto o forzar al usuario a pasarlos?
    # - ¿Voy a aceptar un número variable de argumentos con *args/**kwargs?
