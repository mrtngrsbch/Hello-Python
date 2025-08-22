"""
Clase 12 — Manejo de excepciones (código robusto)

Propósito pedagógico:
- Entender `try`/`except` y el flujo completo con `else`/`finally`.
- Capturar excepciones por tipo y leer su información.
- Distinguir errores previstos vs. errores de programación.

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Basic/12_exceptions.py
"""

from __future__ import annotations


def demo_try_except_base() -> None:
    print("\n== Excepción base: try/except ==")
    numberOne = 5
    numberTwo = "1"
    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except:
        # Se ejecuta si se produce una excepción
        print("Se ha producido un error")


def demo_flujo_completo() -> None:
    print("\n== Flujo completo: try/except/else/finally ==")
    numberOne = 5
    numberTwo = "1"
    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except:
        print("Se ha producido un error")
    else:  # Opcional
        # Se ejecuta si no se produce una excepción
        print("La ejecución continúa correctamente")
    finally:  # Opcional
        # Se ejecuta siempre
        print("La ejecución continúa")


def demo_excepciones_por_tipo() -> None:
    print("\n== Excepciones por tipo ==")
    numberOne = 5
    numberTwo = "1"
    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except ValueError:
        print("Se ha producido un ValueError")
    except TypeError:
        print("Se ha producido un TypeError")


def demo_captura_informacion() -> None:
    print("\n== Captura de información de la excepción ==")
    numberOne = 5
    numberTwo = "1"
    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except ValueError as error:
        print(error)
    except Exception as my_random_error_name:
        print(my_random_error_name)


if __name__ == "__main__":
    demo_try_except_base()
    demo_flujo_completo()
    demo_excepciones_por_tipo()
    demo_captura_informacion()

    # Práctica guiada (opcional)
    # - Crea una función que convierta texto a int; si falla, devuelve 0 y loguea el error.
    # - Escribe un bloque try/except que capture ZeroDivisionError y muestre un mensaje claro.

    # Checklist mental
    # - ¿Estoy capturando solo las excepciones que espero? (evita except sin tipo en producción)
    # - ¿Necesito finally para liberar recursos (archivos, conexiones)?
    # - ¿Qué información de la excepción necesito (mensaje, tipo, stack)?
