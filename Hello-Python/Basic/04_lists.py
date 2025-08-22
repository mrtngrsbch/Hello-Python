"""
Clase 04 — Listas (colecciones ordenadas y mutables)

Propósito pedagógico:
- Comprender qué es una lista: colección ordenada y mutable.
- Practicar operaciones básicas (crear, leer, actualizar, borrar: CRUD).
- Dominar búsqueda, concatenación, slicing, copia, reversa y ordenación.
- Evitar errores típicos: IndexError, mutabilidad accidental por referencia, sort de tipos mezclados.

Cómo usar este archivo:
- Ejecuta el script para ver pequeñas demostraciones impresas en consola.
- Usa este archivo como referencia rápida y como base para tus propios experimentos.
"""

# Pequeñas demostraciones (cada una es corta y enfocada)

def demo_basicos() -> None:
    print("\n== Básicos ==")
    vacia = list()
    otra_vacia = []
    numeros = [35, 24, 62, 52, 30, 30, 17]
    mixto = [35, 1.77, "Brais", "Moure"]
    print(len(vacia), len(numeros))
    print(type(numeros).__name__, type(mixto).__name__)


def demo_acceso_y_busqueda() -> None:
    print("\n== Acceso y búsqueda ==")
    datos = [35, 1.77, "Brais", "Moure"]
    print(datos[0], datos[1], datos[-1])
    print("index('Brais'):", datos.index("Brais"))
    # Desempaquetado
    edad, altura, nombre, apellido = datos
    print(nombre, edad)


def demo_concatenacion() -> None:
    print("\n== Concatenación ==")
    a = [1, 2, 3]
    b = ["x", "y"]
    print(a + b)


def demo_crud() -> None:
    print("\n== CRUD (crear/leer/actualizar/borrar) ==")
    datos = [35, 1.77, "Brais", "Moure"]
    datos.append("MoureDev")
    datos.insert(1, "Rojo")
    print(datos)
    datos[1] = "Azul"
    print(datos)
    datos.remove("Azul")
    print(datos)
    numeros = [35, 24, 62, 52, 30, 30, 17]
    numeros.remove(30)  # elimina la primera aparición
    print(numeros)
    extraido = numeros.pop()  # último
    print("pop() ->", extraido, numeros)
    extraido = numeros.pop(2)  # por índice
    print("pop(2) ->", extraido, numeros)
    del numeros[2]
    print("del indice 2 ->", numeros)


def demo_operaciones() -> None:
    print("\n== Operaciones comunes ==")
    origen = [35, 24, 62, 52, 30, 30, 17]
    copia = origen.copy()  # copia superficial (shallow copy)
    origen.clear()
    print("origen:", origen, "copia:", copia)
    copia.reverse()
    print("reverse:", copia)
    copia.sort()  # orden ascendente
    print("sort asc:", copia)
    copia.sort(reverse=True)
    print("sort desc:", copia)


def demo_slicing() -> None:
    print("\n== Slicing (sublistas) ==")
    datos = [10, 20, 30, 40, 50]
    print(datos[1:3], datos[:3], datos[2:], datos[-3:])


def demo_cambio_tipo() -> None:
    print("\n== Cambio de tipo ==")
    texto = "Hola Python"
    lista = list(texto)
    print(lista[:5])


if __name__ == "__main__":
    demo_basicos()
    demo_acceso_y_busqueda()
    demo_concatenacion()
    demo_crud()
    demo_operaciones()
    demo_slicing()
    demo_cambio_tipo()

    # Bloque de práctica guiada (descomentarlo si quieres practicar)
    # Ejercicio: dada una lista de números, elimina duplicados manteniendo el orden.
    # pistas: usa un conjunto para ver pertenencia, y construye una nueva lista.
    # nums = [1, 2, 2, 3, 1, 4, 3]
    # vistos = set()
    # sin_dupes = []
    # for n in nums:
    #     if n not in vistos:
    #         vistos.add(n)
    #         sin_dupes.append(n)
    # print(sin_dupes)  # esperado: [1, 2, 3, 4]

    # Checklist mental
    # - CRUD en listas: .append(), .insert(), asignación por índice, .remove(), .pop(), del
    # - Búsqueda/medición: .index(), .count(), len(...)
    # - Slicing: lista[inicio:fin], soporta negativos
    # - Copiar vs referenciar: .copy() crea nueva lista; asignación crea alias
    # - Ordenación y reversa: .sort(key=..., reverse=...), .reverse()
    # - Errores: IndexError si índice inválido; ValueError en .remove() si no existe el elemento
