"""
Clase 05 — Tuplas (colecciones ordenadas e inmutables)

Propósito pedagógico:
- Entender que una tupla es ordenada pero inmutable.
- Practicar acceso, búsqueda, concatenación y slicing.
- Ver cómo “modificar” una tupla convirtiéndola temporalmente en lista.
- Evitar errores típicos: TypeError al intentar asignar/borrar elementos.

Cómo usar este archivo:
- Ejecuta el script para ver pequeñas demostraciones imprimibles.
- Úsalo como referencia rápida y base para experimentar.
"""

# Pequeñas demostraciones

from __future__ import annotations

def demo_basicos() -> None:
    print("\n== Básicos ==")
    vacia = tuple()
    otra_vacia = ()
    t = (35, 1.77, "Brais", "Moure", "Brais")
    t2 = (35, 60, 30)
    print(t)
    print(type(t).__name__)


def demo_acceso_y_busqueda() -> None:
    print("\n== Acceso y búsqueda ==")
    t = (35, 1.77, "Brais", "Moure", "Brais")
    print(t[0], t[-1])
    print("count('Brais'):", t.count("Brais"))
    print("index('Moure'):", t.index("Moure"))


def demo_concatenacion() -> None:
    print("\n== Concatenación ==")
    t = (1, 2, 3)
    u = ("x", "y")
    print(t + u)


def demo_subtuplas() -> None:
    print("\n== Subtuplas (slicing) ==")
    t = (10, 20, 30, 40, 50, 60)
    print(t[2:5], t[:3], t[3:], t[-3:])


def demo_mutabilidad_via_lista() -> None:
    print("\n== Tupla “mutable” vía lista ==")
    t = (35, 1.77, "Brais", "Moure", "Brais")
    l = list(t)
    l[4] = "MoureDev"
    l.insert(1, "Azul")
    t = tuple(l)
    print(t)


def demo_eliminacion() -> None:
    print("\n== Eliminación y errores típicos ==")
    t = (1, 2, 3)
    # del t[1]  # TypeError: no se puede borrar por índice en tupla
    del t  # borra la referencia completa
    # print(t)  # NameError si se intenta acceder después


if __name__ == "__main__":
    demo_basicos()
    demo_acceso_y_busqueda()
    demo_concatenacion()
    demo_subtuplas()
    demo_mutabilidad_via_lista()
    demo_eliminacion()

    # Bloque de práctica guiada (descomentarlo si quieres practicar)
    # Ejercicio: dada una tupla de enteros, obtén una nueva tupla con los elementos desde el índice 1 al 3.
    # t = (5, 10, 15, 20, 25)
    # sub = t[1:4]
    # print(sub)  # esperado: (10, 15, 20)

    # Checklist mental
    # - Inmutabilidad: no se puede asignar ni borrar elementos de una tupla
    # - Acceso/slicing: t[i], t[a:b]
    # - Búsqueda: .count(), .index()
    # - Concatenación: t + u crea una nueva tupla
    # - Para “modificar”: convertir a list, operar, y volver a tuple
