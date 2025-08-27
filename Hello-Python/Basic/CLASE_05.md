<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 05**

# Clase 05 — Tuplas (colecciones ordenadas e inmutables)

## Apertura narrativa

Una tupla es como una foto: captura un conjunto de valores en un momento y no cambia. Cuando necesitas garantizar que “esto no se toca”, las tuplas te dan seguridad y claridad.

## Por qué te importa

- Estructuras datos ordenados que no deben cambiar (configuraciones, coordenadas, fechas).
- Te permite usar elementos como claves en diccionarios si son hashables.
- Evitas mutaciones accidentales que luego son difíciles de rastrear.

## Demostración guiada

```python
person = ("Brais", "Moure", 35)
print(len(person))         # medir
print(person[0], person[-1])  # acceso por índice

# Concatenación y conteo
more = ("Brais",)
merged = person + more     # `+` crea una nueva tupla
print(merged.count("Brais"))
print(merged.index("Moure"))

# Subtuplas (slicing)
sub = merged[1:3]          # `tupla[a:b]`
print(sub)

# Inmutabilidad: no puedes reasignar un índice
# merged[0] = "Hector"   # TypeError

# Empaquetado y desempaquetado
name, surname, age, extra = merged  # cuidado con la cantidad de elementos
print(name, surname, age, extra)

# Convertir para mutar y volver a tupla
as_list = list(person)
as_list[2] = 36
person2 = tuple(as_list)
print(person2)
```

## Micro‑kata (7–10 min)

- Dada una tupla con nombres, crea otra tupla con nombres únicos preservando el orden.
- Muestra la subtupla de los 2 últimos nombres usando `tupla[-2:]`.
- Pista: usa `in`, `not in` y concatenación con `+`.

## Cheatsheet de tuplas

- Crear: `()`, `(elemento,)` para una tupla de 1 elemento, `tuple(iterable)`
- Medir: `len(tupla)`
- Acceso: `tupla[i]`, `tupla[-1]`
- Concatenar: `tupla1 + tupla2` (crea NUEVA tupla)
- Buscar/contar: `.index(x)`, `.count(x)`
- Slicing: `tupla[a:b]`, `tupla[:b]`, `tupla[a:]`, `tupla[-n:]`
- Empaquetar/desempaquetar: `a, b = (1, 2)` (coincidir cantidades)
- Cambio de tipo: `list(tupla)` para mutar; `tuple(lista)` para volver a tupla
- Pertenencia: `in`, `not in`

## Errores frecuentes

- `TypeError` al intentar asignar `tupla[i] = valor` (inmutables).
- `ValueError` en `.index(x)` si `x` no existe.
- Desempaquetado con cantidades diferentes de variables y elementos.

## Prueba/ejecución (opcional)

- Ejecuta `Basic/05_tuples.py` para ver las demos.
- Practica convirtiendo entre `list` y `tuple` para mutar con control.

## Material de apoyo

- Código de referencia: `Basic/05_tuples.py`

## Qué te llevas hoy

- Sabes cuándo elegir `tuple` frente a `list` y cómo trabajar con slicing, conteo e inmutabilidad.

## Siguiente paso

- Clase 06: `set` (colecciones desordenadas, sin duplicados).

---

**⬅️ [Anterior: Clase 04 - Listas](CLASE_04.md) | ⏭️ [Siguiente: Clase 06 - Sets](CLASE_06.md) | [🏠 Volver al Índice](../../HelloPython.md)**
