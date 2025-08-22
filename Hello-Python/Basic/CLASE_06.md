# Clase 06 — Sets (colecciones sin duplicados)

## Apertura narrativa
Un `set` es como una bolsa mágica donde cada cosa aparece solo una vez. Cuando limpias datos, buscas pertenencia rápida o quieres operaciones de teoría de conjuntos, `set` es tu mejor aliado.

## Por qué te importa
- Elimina duplicados de forma simple.
- Búsqueda de pertenencia `in`/`not in` muy eficiente.
- Operaciones potentes: unión `|`, intersección `&`, diferencia `-`, diferencia simétrica `^`.

## Demostración guiada
```python
nums = {1, 2, 3, 3, 2}
print(nums)                # {1, 2, 3} sin duplicados

nums.add(4)                # añadir
nums.add(2)                # no añade duplicado
print(nums)

nums.remove(3)             # elimina existente (lanza `KeyError` si no está)
nums.discard(99)           # elimina si existe (no lanza error)
print(nums)

# Operaciones de conjuntos
pares = {2, 4, 6}
impares = {1, 3, 5}
print(nums | pares)        # unión
print(nums & pares)        # intersección
print(nums - {1, 4})       # diferencia
print(pares ^ impares)     # diferencia simétrica

# Conversión
lista = [1, 2, 2, 3, 3, 4]
unicos = set(lista)        # quitar duplicados
print(unicos)
print(2 in unicos)         # pertenencia
```

## Micro‑kata (7–10 min)
- Dada una lista de emails con duplicados y mayúsculas/minúsculas mezcladas, normaliza (`lower()`), elimina duplicados y cuenta cuántos únicos quedan.
- Muestra la intersección entre dos grupos de emails.

## Cheatsheet de sets
- Crear: `{}`, `set(iterable)` (ojo: `{}` crea `dict`, para set vacío usa `set()`)
- Añadir/eliminar: `.add(x)`, `.remove(x)`, `.discard(x)`, `.pop()`
- Limpieza: `.clear()`
- Operaciones: `a | b` (unión), `a & b` (intersección), `a - b` (diferencia), `a ^ b` (diferencia simétrica)
- Pertenencia: `in`, `not in`
- Conversión: `list(set(lista))` para quitar duplicados preservando luego con cuidado el orden si lo reconstruyes

## Errores frecuentes
- Usar `{}` esperando un set vacío: crea un `dict`; usa `set()`.
- `.remove(x)` sobre elemento inexistente lanza `KeyError`; si no estás seguro, usa `.discard(x)`.
- Conjuntos no mantienen orden; no los uses cuando el orden sea importante.

## Prueba/ejecución (opcional)
- Ejecuta `Basic/06_sets.py` para ver las demos.

## Material de apoyo
- Código de referencia: `Basic/06_sets.py`

## Qué te llevas hoy
- Limpias duplicados, pruebas pertenencia y combinas conjuntos con claridad y seguridad.

## Siguiente paso
- Clase 07: diccionarios (`dict`), pares clave-valor muy versátiles.