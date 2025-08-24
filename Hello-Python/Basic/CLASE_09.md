<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 09**

# Clase 09 — Bucles (repetición controlada)

## Apertura narrativa
Los bucles son tus robots: repiten tareas sin cansarse. Ya sea procesar listas, buscar un elemento o esperar un evento, `while` y `for` te dan el control del tiempo y la cantidad.

## Por qué te importa
- Automatizas tareas repetitivas de forma legible.
- Recorres colecciones (`list`, `tuple`, `set`, `dict`) con facilidad.
- Controlas el flujo interno con `break`, `continue` y `else` de bucle.

## Demostración guiada
```python
# while básico
n = 0
while n < 5:
    print(n)
    n += 1
else:
    print("Fin del while")

# for sobre colecciones
nums = [1, 2, 3]
for x in nums:
    print(x)

persona = {"nombre": "Brais", "edad": 35}
for k in persona:
    print(k)          # itera por claves

for k, v in persona.items():
    print(k, v)       # par clave-valor

# break y continue
for x in range(1, 8):
    if x == 5:
        break         # sale del bucle
    if x % 2 == 0:
        continue      # salta a la siguiente iteración
    print("impar", x)
else:
    print("Terminó el for sin break")
```

## Micro‑kata (7–10 min)
- Imprime del 1 al 100, pero salta múltiplos de 3 y detente al llegar a `73`.
- Recorre una lista de dicts de estudiantes y muestra solo los de nota `>= 7`.

## Cheatsheet de bucles
- `while condicion:` … `else:` (opcional)
- `for elemento in iterable:` … `else:` (opcional)
- Control: `break` (sale del bucle), `continue` (salta a la siguiente iteración)
- Diccionarios: iterar por claves; usa `.items()` para `(clave, valor)`

## Errores frecuentes
- Bucles infinitos por no actualizar la condición en `while`.
- Modificar una colección mientras la iteras puede causar sorpresas.
- Off‑by‑one: mal cálculo del límite superior.

## Prueba/ejecución (opcional)
- Ejecuta `Basic/09_loops.py` para ver las demos.

## Material de apoyo
- Código de referencia: `Basic/09_loops.py`

## Qué te llevas hoy
- Dominas `while`/`for` y controlas el flujo con `break`/`continue`/`else`.

## Siguiente paso
- Clase 10: funciones (organizar y reutilizar lógica).

---

**⬅️ [Anterior: Clase 08 - Condicionales](CLASE_08.md) | ⏭️ [Siguiente: Clase 10 - Funciones](CLASE_10.md) | [🏠 Volver al Índice](../../HelloPython.md)**