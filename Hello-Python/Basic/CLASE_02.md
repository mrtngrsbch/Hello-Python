# Clase 02 — Variables y Strings (Transformaciones de texto)

## Apertura narrativa
Una variable es una etiqueta para hablar con tus datos por su nombre. Hoy usamos texto (strings) y lo transformamos sin “romper” el original, porque las cadenas en Python son inmutables: cada transformación crea una nueva versión. ¿Para qué sirve? Desde limpiar formularios hasta generar nombres de archivos o URLs legibles.

## Por qué te importa
- Puedes dar nombre a los datos y reutilizarlos en varios pasos.
- Aprendes a medir (len), normalizar (strip), estandarizar (upper) y reemplazar (replace).
- Sientas las bases para búsquedas, comparaciones y validaciones de texto.

## Demostración guiada
```python
frase = input("Escribe una frase: ")
frase_limpia = frase.strip()         # quita espacios al inicio/fin
longitud = len(frase_limpia)         # mide
mayus = frase_limpia.upper()         # estandariza
con_guiones = frase_limpia.replace(" ", "_")  # normaliza

print("Longitud:", longitud)
print("Mayúsculas:", mayus)
print("Con guiones bajos:", con_guiones)
```
## Puntos clave
- Inmutabilidad: cada método devuelve una nueva cadena; si no la asignas, se pierde.
- Asignación clara: usa nombres intermedios para que el flujo sea legible.

## Micro‑kata (7–10 min)
- Pide una frase y muestra:
  1) Longitud con `len(...)`.
  2) Versión en mayúsculas con `.upper()`.
  3) Versión con espacios reemplazados por guiones bajos con `.replace(" ", "_")`.
- Opcional: aplica `.strip()` antes; si la entrada está vacía, vuelve a pedir.

## Cheatsheet (variables y strings)
- `+` (concatenación): "Py" + "thon" → "Python"
- `*` (repetición): "ha" * 3 → "hahaha"
- `in` / `not in` (pertenencia): "py" in "python" → `True`
- `==` / `!=` (comparación): "hola" == "hola" → `True`
- `+=` (asignación compuesta): `s = "hi"; s += "!"` → "hi!" (nota: crea nueva cadena)
- Slicing: `s[0:3]` (sintaxis clave para extraer partes)

## Errores frecuentes
- Transformar sin asignar: el resultado se pierde si no lo guardas.
- Espacios “invisibles” alteran resultados: normaliza con `strip()`.
- Confundir pertenencia con igualdad: "py" in "python" no es igual que "py" == "python".

## Prueba automática (opcional)
- Desde Hello-Python: `../.venv/bin/python -m unittest -v`
- Deben pasar los tests de `tests/test_strings_utils.py`.

## Material de apoyo
- Utilidades de strings: `Basic/strings_utils.py`
- Pruebas: `tests/test_strings_utils.py`

## Qué te llevas hoy
- Sabes nombrar datos, medirlos y transformarlos de forma segura.
- Tienes herramientas para preparar texto antes de validarlo o compararlo.

## Siguiente paso
- Clase 03: operadores (aritméticos, comparación, lógicos). Allí verás el cheatsheet completo con ejemplos y trampas comunes.