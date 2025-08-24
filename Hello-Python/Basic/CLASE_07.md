<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 07**

# Clase 07 — Diccionarios (pares clave‑valor)

## Apertura narrativa
Un `dict` es como una agenda: buscas por clave y obtienes el valor al instante. Ideal para representar entidades (usuario, producto) y acceder a sus campos de forma directa.

## Por qué te importa
- Acceso por clave rápido y expresivo.
- APIs claras y extensibles para datos estructurados.
- Métodos útiles para inspección: `.keys()`, `.values()`, `.items()`.

## Demostración guiada
```python
user = {"nombre": "Brais", "apellido": "Moure", "edad": 35}
print(user["nombre"])        # acceso por clave

user["edad"] = 36            # actualizar
user["email"] = "b@example.com"  # insertar
print(user)

print("nombre" in user)      # pertenencia por clave
print(user.get("altura"))    # `None` si no existe (no lanza error)
print(user.get("altura", 0)) # valor por defecto

print(list(user.keys()))      # claves
print(list(user.values()))    # valores
print(list(user.items()))     # pares (clave, valor)

# Eliminación
valor = user.pop("email")    # elimina y devuelve
print(valor)

# Copias y fromkeys
vacio = dict.fromkeys(["id", "estado"], None)
print(vacio)
copia = user.copy()           # copia superficial
print(copia)
```

## Micro‑kata (7–10 min)
- Dada una lista de tuplas `(nombre, nota)`, crea un `dict` y muestra solo alumnos con nota `>= 7`.
- A partir de un `dict` de productos, calcula el `precio_total` acumulado.

## Cheatsheet de diccionarios
- Crear: `{clave: valor}`, `dict(pares)`, `dict.fromkeys(claves, valor)`
- Acceso/actualización: `d[clave]`, `d.get(clave, por_defecto)`, `d[clave] = valor`
- Inspección: `.keys()`, `.values()`, `.items()`
- Eliminación: `.pop(clave)`, `del d[clave]`, `.clear()`
- Copias: `.copy()` (superficial)
- Pertenencia: `in` (sobre claves)

## Errores frecuentes
- `KeyError` al acceder con `d[clave]` inexistente; usa `get()` si no estás seguro.
- Mutar mientras iteras sobre `d.items()` puede generar comportamientos inesperados.
- Claves deben ser `hashables` (inmutables típicamente: `str`, `int`, `tuple` de hashables).

## Prueba/ejecución (opcional)
- Ejecuta `Basic/07_dicts.py` para ver las demos.

## Material de apoyo
- Código de referencia: `Basic/07_dicts.py`

## Qué te llevas hoy
- Modelas entidades con claridad, iteras por claves/valores y evitas errores comunes.

## Siguiente paso
- Clase 08: condicionales (`if`/`elif`/`else`) para tomar decisiones.

---

**⬅️ [Anterior: Clase 06 - Sets](CLASE_06.md) | ⏭️ [Siguiente: Clase 08 - Condicionales](CLASE_08.md) | [🏠 Volver al Índice](../../HelloPython.md)**