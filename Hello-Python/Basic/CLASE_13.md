<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 13**

# Clase 13 — Módulos e Imports (organización y reutilización)

## Apertura narrativa

Dividir en módulos te permite organizar el código por responsabilidad y reutilizarlo. Importar lo correcto en el lugar correcto simplifica tu vida.

## Por qué te importa

- Separas funcionalidades y reduces el acoplamiento.
- Reutilizas utilidades en distintos archivos/proyectos.
- Evitas duplicación y mejoras mantenibilidad.

## Demostración guiada

```python
# Import de módulo propio
import my_module
print(my_module.sumValue(5, 3))
my_module.printValue("Hola")

# Import selectivo y alias
from my_module import sumValue as sumar
print(sumar(2, 2))

# Módulo estándar
import math as m
print(m.sqrt(16))
print(m.pi)

# Buenas prácticas: importar al inicio del archivo.
# if __name__ == "__main__":
#     # código que solo se ejecuta si se llama directamente
#     pass
```

## Micro‑kata (7–10 min)

- Crea `util_texto.py` con `contar_vocales(s)` y úsalo desde otro archivo.
- Usa `random` para simular 100 lanzamientos de moneda y contar caras.

## Cheatsheet de módulos

- Importar: `import modulo`, `from modulo import nombre`, `as` para alias
- Módulos estándar: `math`, `random`, `datetime`, `pathlib`, etc.
- Módulos propios: archivos `.py` en tu proyecto
- Punto de entrada: `if __name__ == "__main__": ...`

## Errores frecuentes

- Importar dentro de funciones sin necesidad (más lento/menos claro).
- Nombres en conflicto (usa alias `as`).
- Rutas relativas complejas; mantén una estructura simple de paquetes.

## Prueba/ejecución (opcional)

- Ejecuta `Basic/13_modules.py` para ver las demos.

## Material de apoyo

- Código de referencia: `Basic/13_modules.py`, `Basic/my_module.py`

## Qué te llevas hoy

- Importas con criterio y organizas tu proyecto en módulos reutilizables.

## Siguiente paso

- Consolidar: escribe utilidades propias y crea tests mínimos para validarlas.

---

**⬅️ [Anterior: Clase 12 - Excepciones](CLASE_12.md) | [🏠 Volver al Índice](../../HelloPython.md)**
