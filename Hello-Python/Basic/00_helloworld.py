"""
Clase 01 — Hello World e I/O básico (input/print)

Propósito:
- Imprimir mensajes en consola con print()
- Diferenciar comentarios de una línea y docstrings/bloques multilínea
- Reconocer tipos básicos con type()
- Practicar un pequeño bloque de entrada/salida (opcional)

Cómo ejecutar:
- python3 Hello-Python/Basic/00_helloworld.py

Nota: hay un bloque de práctica con input comentado para no bloquear pruebas. Lee el flujo y luego descoméntalo si quieres interactuar.
"""

from __future__ import annotations


def demo_hello_world() -> None:
    """Demostración mínima de impresión en consola."""
    print("Hola Python")
    print('Hola Python')  # Comillas simples o dobles, ambas funcionan


def demo_comments_and_docstrings() -> None:
    """Muestra diferentes tipos de comentarios.

    - El texto entre triple comillas al inicio del archivo es un docstring de módulo.
    - Este docstring pertenece a la función.
    - Las líneas que empiezan con # son comentarios de una sola línea.
    """
    # Esto es un comentario de una línea (no se ejecuta)

    """
    Este es un bloque de texto multilínea que, si no se asigna a una variable,
    suele usarse como comentario de varias líneas. Técnicamente Python lo 
    interpreta como un literal de cadena no usado.
    """


def demo_basic_types() -> None:
    """Repaso de tipos básicos y la función type()."""
    print(type("Soy un dato str"))   # str (cadena de texto)
    print(type(5))                    # int (entero)
    print(type(1.5))                  # float (coma flotante)
    print(type(3 + 1j))               # complex (número complejo)
    print(type(True))                 # bool (booleano)
    print(type(print("Mi cadena de texto")))  # NoneType (print no devuelve nada)


# Bloque de práctica (comentado para no interrumpir ejecuciones automatizadas)
# 1) Descomenta y ejecuta el archivo. Escribe tu nombre cuando te lo pida.
# 2) Observa la salida.
# 3) Prueba a cambiar el mensaje.
#
# name = input("¿Cuál es tu nombre? ")
# print(f"Encantado, {name}!")
# Checklist mental (comentado)
# - print(): ¿entiendo que imprime y no devuelve valor (None)?
# - type(): ¿puedo reconocer str, int, float, bool, complex?
# - Comentarios: # para una línea, triple comillas para docstrings/bloques.

if __name__ == "__main__":
    demo_hello_world()
    demo_comments_and_docstrings()
    demo_basic_types()