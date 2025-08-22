"""
Clase 06 — Sets (conjuntos no ordenados, sin duplicados)

Propósito pedagógico:
- Entender qué es un set: colección no ordenada de elementos únicos.
- Practicar inserción, pertenencia, eliminación y operaciones entre conjuntos.
- Dominar transformaciones set<->list y precauciones con tipos no hashables.
- Evitar errores típicos: confundir {} (dict), depender del orden, usar elementos mutables.

Cómo usar este archivo:
- Ejecuta el script para ver pequeñas demostraciones impresas en consola.
- Úsalo como referencia rápida y base para tus propios experimentos.
"""

# Pequeñas demostraciones

def demo_basicos() -> None:
    print("\n== Básicos ==")
    vacio = set()
    posible_dict = {}
    print(type(vacio).__name__, type(posible_dict).__name__)  # {} crea dict
    s = {"Brais", "Moure", 35}
    print(s, "len:", len(s))  # sin orden garantizado y sin duplicados


def demo_insercion_y_busqueda() -> None:
    print("\n== Inserción y pertenencia ==")
    s = {"Python", "Swift"}
    s.add("Kotlin")
    s.add("Kotlin")  # ignorado (ya existe)
    print(s)
    print("'Python' in s?", "Python" in s)
    print("'Java' in s?", "Java" in s)


def demo_eliminacion() -> None:
    print("\n== Eliminación ==")
    s = {"Python", "Swift", "Kotlin"}
    s.remove("Swift")  # KeyError si no existe; .discard() no lo lanza
    print(s)
    s.clear()
    print("len tras clear:", len(s))


def demo_operaciones() -> None:
    print("\n== Operaciones entre conjuntos ==")
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("union:", a.union(b))              # {1,2,3,4,5}
    print("intersección:", a.intersection(b)) # {3}
    print("diferencia:", a.difference(b))     # {1,2}
    print("simétrica:", a.symmetric_difference(b))  # {1,2,4,5}
    print("subset:", {1,2}.issubset(a), "superset:", a.issuperset({1,2}))


def demo_transformacion_y_tipos() -> None:
    print("\n== Transformaciones y tipos ==")
    s = {"Brais", "Moure", 35}
    l = list(s)  # orden no garantizado al convertir
    print(l)
    # Nota: elementos de un set deben ser hashables (inmutables). Por ejemplo, no puedes añadir listas o dicts.
    # s.add([1,2])  # TypeError: unhashable type: 'list'


if __name__ == "__main__":
    demo_basicos()
    demo_insercion_y_busqueda()
    demo_eliminacion()
    demo_operaciones()
    demo_transformacion_y_tipos()

    # Bloque de práctica guiada (descomentarlo si quieres practicar)
    # Ejercicio: dados dos sets a y b, imprime su intersección y si a es subconjunto de b.
    # a = {1, 2, 3, 4}
    # b = {3, 4, 5}
    # print(a.intersection(b))  # esperado: {3, 4}
    # print(a.issubset(b))      # esperado: False

    # Checklist mental
    # - {} crea dict, no set; usa set() para set vacío
    # - No hay orden; no dependas de posiciones
    # - No hay duplicados; .add() de repetidos no cambia el set
    # - Pertenencia rápida: x in s
    # - Operaciones: union, intersection, difference, symmetric_difference
    # - Elementos deben ser hashables (no listas/dicts)
