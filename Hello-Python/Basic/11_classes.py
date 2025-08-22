"""
Clase 11 — Clases y objetos (modelando datos y comportamiento)

Propósito pedagógico:
- Definir clases con `__init__`, atributos públicos y "privados" (name mangling con `__`).
- Crear métodos de instancia y entender `self`.
- Buenas prácticas: `__str__`/`__repr__`, validaciones en constructor, mutabilidad controlada.

Cómo usar este archivo:
- Ejecuta el script para ver demostraciones y reflexionar sobre los prints.
- Úsalo como plantilla para tus propias clases.
"""


# Definiciones
from __future__ import annotations

class MyEmptyPerson:
    """Clase vacía de ejemplo"""
    pass


class Person:
    def __init__(self, name: str, surname: str, alias: str = "Sin alias") -> None:
        self.full_name: str = f"{name} {surname} ({alias})"
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name

    def walk(self) -> None:
        print(f"{self.full_name} está caminando")

    def __str__(self) -> str:
        return self.full_name


# Demostraciones

def demo_clase_vacia() -> None:
    print("\n== Clase vacía ==")
    print(MyEmptyPerson)
    print(MyEmptyPerson())


def demo_persona_basico() -> None:
    print("\n== Persona básico ==")
    p = Person("Brais", "Moure")
    print(p.full_name)
    print(p.get_name())
    p.walk()


def demo_persona_alias_y_mutacion() -> None:
    print("\n== Alias y mutación de atributos ==")
    p = Person("Brais", "Moure", "MoureDev")
    print(p.full_name)
    p.walk()
    # Mutación (válida, pero debe usarse con criterio)
    p.full_name = "Héctor de León (El loco de los perros)"
    print(p.full_name)
    # Advertencia: Python no impide cambiar el tipo
    p.full_name = 666
    print(p.full_name)


if __name__ == "__main__":
    demo_clase_vacia()
    demo_persona_basico()
    demo_persona_alias_y_mutacion()

    # Práctica guiada (opcional)
    # 1) Añade una edad a Person validando que sea >= 0 en __init__
    # 2) Implementa propiedades (@property) para exponer name de solo lectura
    # 3) Implementa __repr__ para depuración clara

    # Checklist mental
    # - ¿Necesito __init__? ¿Qué invariantes valido ahí?
    # - ¿Qué atributos deben ser públicos vs. "privados" (name mangling con __)?
    # - ¿Mi __str__/__repr__ explica bien el estado del objeto?
    # - ¿Estoy mutando atributos conscientemente (posibles efectos colaterales)?
