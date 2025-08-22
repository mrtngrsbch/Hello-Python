# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ###

"""
Clase 13 — Módulos e importación (organizando el código)

Propósito pedagógico:
- Importar módulos de distintas formas: `import`, `from ... import`, alias con `as`.
- Entender espacios de nombres y cuándo usar cada estilo.
- Practicar con un módulo propio (`my_module`) y con la librería estándar (`math`).

Cómo ejecutar:
- ../.venv/bin/python Hello-Python/Basic/13_modules.py
- Abre `Basic/my_module.py` para ver las funciones importadas.
"""

from __future__ import annotations

import math
from math import pi as PI_VALUE
import my_module
from my_module import sumValue, printValue


def demo_imports_y_uso() -> None:
    print("\n== Importaciones y uso ==")
    # Usando el espacio de nombres del módulo
    my_module.sumValue(5, 3, 1)
    my_module.printValue("Hola Python!")

    # Importando símbolos directamente
    sumValue(5, 3, 1)
    printValue("Hola python")

    # Librería estándar
    print(math.pi)
    print(math.pow(2, 8))

    # Alias desde un módulo
    print(PI_VALUE)


if __name__ == "__main__":
    demo_imports_y_uso()

    # Práctica guiada (opcional)
    # - Crea una función en my_module que multiplique 3 números e impórtala aquí.
    # - Prueba alias distintos: from math import pow as power.

    # Checklist mental
    # - `import modulo` vs `from modulo import símbolo`: ¿qué me conviene por legibilidad?
    # - ¿Hay colisión de nombres? Usa alias con `as`.
    # - Mantén importaciones al inicio del archivo.
