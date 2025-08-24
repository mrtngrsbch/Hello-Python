"""
Clase 02 — Variables y Strings (base)

Propósito:
- Entender qué es una variable y cómo asignar valores
- Practicar strings y transformaciones básicas (len, upper, replace, strip)
- Mantener el código legible con nombres descriptivos

Cómo ejecutar:
- python3 Hello-Python/Basic/01_variables.py

Nota: Hay un bloque de práctica con input comentado para no bloquear pruebas.
"""

from __future__ import annotations


def demo_variables_basicas() -> None:
    """Variables, asignación y tipos comunes."""
    mensaje: str = "Hola"
    veces: int = 3
    pi_aproximado: float = 3.14
    es_activo: bool = True

    # f-strings: interpolación de variables en cadenas
    print(f"mensaje={mensaje}, veces={veces}, pi≈{pi_aproximado}, activo={es_activo}")

    # Python es de tipado dinámico: puedes reasignar otro tipo
    # (No es recomendable para principiantes; mejor mantener consistencia)
    mensaje = mensaje + " Python"
    print("Después de concatenar:", mensaje)


def demo_strings_basicos() -> None:
    """Operaciones esenciales con strings: len, upper, replace, strip."""
    frase = "  Hola mundo desde Python  "
    print("Original:", repr(frase))

    frase_limpia = frase.strip()              # quita espacios al inicio/fin
    print("strip():", repr(frase_limpia))

    longitud = len(frase_limpia)              # mide longitud
    print("len():", longitud)

    mayus = frase_limpia.upper()              # mayúsculas
    print("upper():", mayus)

    con_guiones = frase_limpia.replace(" ", "_")  # reemplaza espacios
    print("replace(' ', '_'):", con_guiones)

    # Importante: las cadenas son inmutables; cada operación crea una nueva cadena.


# Práctica guiada (comentada)
# 1) Pide al usuario una frase, límpiala con strip() y muestra:
#    - longitud
#    - mayúsculas
#    - la misma frase con guiones bajos en vez de espacios
# 2) Declara variables nombre, edad y activo. Forma un mensaje con f-string.
# 3) Verifica con type() los tipos de tus variables.
# Checklist mental (comentado)
# - ¿Qué es una variable? Un nombre que referencia un valor.
# - Strings son inmutables: cada transformación crea una nueva cadena.
# - ¿Cuándo usar strip(), len(), upper(), replace()?
# - ¿Mis nombres de variables son descriptivos?


if __name__ == "__main__":
    demo_variables_basicas()
    demo_strings_basicos()
