<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 04**

# Clase 04 — Listas (colecciones ordenadas y mutables)

## Apertura narrativa

Una lista es tu caja de herramientas ordenada: puedes añadir, sacar, reordenar y mirar lo que hay en cada posición. Cuando limpias datos, agrupar resultados o preparar un batch de tareas, las listas te dan control y velocidad.

## Por qué te importa

- Estructuras tus datos en orden, con acceso por índice.
- Puedes crecer y reducir la colección al vuelo.
- Preparas datos para transformaciones posteriores (map, filtros, ordenación).

## Demostración guiada

```python
nums = [35, 24, 62, 52, 30, 30, 17]
print(len(nums))          # medir
print(nums[0], nums[-1])  # acceso
nums.append(99)           # agregar al final
nums.insert(1, 50)        # insertar en posición
nums.remove(30)           # elimina primera aparición
extra = nums.pop()        # quita y devuelve el último
sub = nums[1:4]           # slicing
print(nums, extra, sub)
```

## Micro‑kata (7–10 min)

- Dada una lista con duplicados, crea una nueva lista sin duplicados preservando el orden.
- Ordena la lista resultante en forma descendente y muestra los 3 primeros.
- Pista: usa `in`, `not in`, `append`, `sort(reverse=True)`.

## Cheatsheet de listas

- Crear: `[]`, `list(iterable)`
- Medir: `len(lista)`
- Acceso: `lista[i]`, `lista[-1]`
- Concatenar: `lista1 + lista2`
- Añadir/insertar: `.append(x)`, `.insert(i, x)`, `.extend(iterable)`
- Eliminar: `.remove(x)`, `.pop()`, `.pop(i)`, `del lista[i]`
- Buscar/contar: `.index(x)`, `.count(x)`
- Slicing: `lista[a:b]`, `lista[:b]`, `lista[a:]`, `lista[-n:]`
- Copia vs referencia: `.copy()` crea copia; `asignación` crea alias
- Reversa/orden: `.reverse()`, `.sort(key=..., reverse=...)`
- Pertenencia: `in`, `not in`
- Tip: evita `sort` con tipos mezclados; define `key` cuando sea útil

## Errores frecuentes

- `IndexError` por un índice inválido.
- `ValueError` en `.remove(x)` si `x` no existe.
- Mutación accidental: asignar `lista_b = lista_a` no copia; usa `.copy()`.

## Prueba/ejecución (opcional)

- Ejecuta `Basic/04_lists.py` para ver las demos.
- No hay pruebas automáticas específicas todavía; practica en el REPL.

## Material de apoyo

- Código de referencia: `Basic/04_lists.py`

## Qué te llevas hoy

- Sabes crear, leer, actualizar y borrar elementos en listas.
- Manejas slicing, copia, reversa y ordenación sin sorpresas.

## Siguiente paso

- Clase 05: tuplas (similares a listas, pero `inmutables`).

---

**⬅️ [Anterior: Clase 03 - Operadores](CLASE_03.md) | ⏭️ [Siguiente: Clase 05 - Tuplas](CLASE_05.md) | [🏠 Volver al Índice](../../HelloPython.md)**