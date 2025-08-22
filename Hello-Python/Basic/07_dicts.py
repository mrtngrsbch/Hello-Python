"""
Clase 07 — Diccionarios (mapeos clave→valor)

Propósito pedagógico:
- Entender los diccionarios como mapeos de claves hashables a valores.
- Practicar creación, acceso, inserción, actualización y eliminación.
- Usar vistas: .keys(), .values(), .items() y utilidades como .get(), .update(), .fromkeys().
- Evitar errores típicos: KeyError, confundir pertenencia de claves vs. valores, claves no hashables.

Cómo usar este archivo:
- Ejecuta el script para ver pequeñas demostraciones impresas en consola.
- Úsalo como referencia rápida y base para experimentar.
"""

# Pequeñas demostraciones

def demo_basicos() -> None:
    print("\n== Básicos ==")
    d_vacio = dict()
    otro_vacio = {}
    persona = {
        "Nombre": "Brais",
        "Apellido": "Moure",
        "Edad": 35,
        "Lenguajes": {"Python", "Swift", "Kotlin"},
        1: 1.77,
    }
    print(type(d_vacio).__name__, type(otro_vacio).__name__)
    print(len(persona))


def demo_acceso_y_busqueda() -> None:
    print("\n== Acceso y búsqueda ==")
    d = {"Nombre": "Brais", "Apellido": "Moure", 1: 1.77}
    print(d[1], d["Nombre"])  # KeyError si la clave no existe
    print("'Apellido' in d?", "Apellido" in d)  # pertenencia sobre claves
    print("'Moure' in d?", "Moure" in d)        # False: no busca en valores
    print("get('Altura', 'N/D') ->", d.get("Altura", "N/D"))


def demo_insercion_actualizacion() -> None:
    print("\n== Inserción y actualización ==")
    d = {"Nombre": "Brais"}
    d["Calle"] = "Calle MoureDev"  # inserción
    d["Nombre"] = "Pedro"          # actualización
    d.update({"Edad": 35})
    print(d)


def demo_eliminacion() -> None:
    print("\n== Eliminación ==")
    d = {"Nombre": "Brais", "Calle": "X"}
    eliminado = d.pop("Calle", None)  # seguro si no existe
    print("pop ->", eliminado, d)
    # del d["Calle"]  # KeyError si no existe
    d.clear()
    print("len tras clear:", len(d))


def demo_claves_valores_items() -> None:
    print("\n== Claves, valores e items ==")
    d = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35}
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))


def demo_fromkeys_y_copias() -> None:
    print("\n== fromkeys y copias ==")
    llaves = ["Nombre", "Edad", "Pais"]
    d1 = dict.fromkeys(llaves)              # valores por defecto None
    d2 = dict.fromkeys(llaves, "N/D")      # ¡ojo!: mismo objeto si es mutable
    copia = d2.copy()                        # copia superficial
    print(d1, d2, copia)


def demo_casos_avanzados() -> None:
    print("\n== Casos avanzados ==")
    # Evitar claves no hashables (como listas/dicts)
    d = {("Brais", "Moure"): 1}  # tuplas sí son hashables si son inmutables
    print(d)


if __name__ == "__main__":
    demo_basicos()
    demo_acceso_y_busqueda()
    demo_insercion_actualizacion()
    demo_eliminacion()
    demo_claves_valores_items()
    demo_fromkeys_y_copias()
    demo_casos_avanzados()

    # Bloque de práctica guiada (descomentarlo si quieres practicar)
    # Ejercicio: dado un texto, calcula la frecuencia de cada palabra usando un dict.
    # texto = "hola hola que tal hola que"
    # frec = {}
    # for palabra in texto.split():
    #     frec[palabra] = frec.get(palabra, 0) + 1
    # print(frec)  # {'hola': 3, 'que': 2, 'tal': 1}

    # Checklist mental
    # - Pertenencia con 'in' va sobre claves, no sobre valores
    # - Acceso seguro: .get(clave, default)
    # - Mutaciones: asignación directa, .update(), .pop()
    # - Vistas: .keys(), .values(), .items()
    # - Claves deben ser hashables (inmutables)
