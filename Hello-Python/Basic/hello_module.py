"""
Módulo simple para Clase 01: funciones reutilizables y ejecutable como script.

- hello(): devuelve un saludo estándar (puro, fácil de testear)
- greet(name): valida la entrada y devuelve un saludo personalizado

Ejecutar como script:
../.venv/bin/python Hello-Python/Basic/hello_module.py [nombre]
"""

import sys


def hello() -> str:
    """Devuelve un saludo básico.

    Uso: pensado para ser llamado desde tests o desde main.
    """
    return "Hola Python"


def greet(name: str) -> str:
    """Devuelve un saludo personalizado validando la entrada.

    - Rechaza valores no str o cadenas vacías/solo espacios
    - Normaliza espacios usando strip()
    - No imprime: devuelve el resultado (más fácil de testear)
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name debe ser un string no vacío")
    return f"Encantado, {name.strip()}!"


if __name__ == "__main__":
    # Permite ejecutar el archivo directamente desde la terminal:
    #   ../.venv/bin/python Hello-Python/Basic/hello_module.py [nombre]
    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        print(hello())