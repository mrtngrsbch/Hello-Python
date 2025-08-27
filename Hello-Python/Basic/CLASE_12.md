<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 12**

# Clase 12 — Excepciones (hacer tu código robusto)

## Apertura narrativa

Los errores ocurren. El manejo de excepciones permite anticiparlos, capturarlos y decidir cómo reaccionar sin que tu programa se derrumbe.

## Por qué te importa

- Evitas caídas inesperadas y mejoras la experiencia de usuario.
- Diferencias entre errores recuperables y críticos.
- Depuras mejor al capturar información del error.

## Demostración guiada

```python
# try/except/else/finally
try:
    x = int("42")
except ValueError as e:
    print("Conversión inválida", e)
else:
    print("Todo salió bien:", x)
finally:
    print("Se ejecuta siempre")

# Capturar por tipo específico
try:
    with open("no_existe.txt") as f:
        datos = f.read()
except FileNotFoundError:
    print("Archivo no encontrado")

# Levantar (raise) con mensaje

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("b no puede ser 0")
    return a / b

# Obtener información de la excepción
try:
    dividir(4, 0)
except Exception as e:
    print(type(e).__name__, str(e))
```

## Micro‑kata (7–10 min)

- Implementa `leer_entero(prompt)` que repita hasta obtener un entero válido.
- Escribe `validar_email(email)` que lance `ValueError` con mensajes claros.

## Cheatsheet de excepciones

- Bloques: `try`/`except`/`else`/`finally`
- Tipos comunes: `ValueError`, `TypeError`, `FileNotFoundError`, `ZeroDivisionError`
- `raise` para lanzar una excepción intencionalmente
- Captura selectiva por tipo para respuestas adecuadas

## Errores frecuentes

- Capturar `Exception` demasiado pronto oculta problemas.
- Silenciar errores sin log o mensaje dificulta depuración.
- No cerrar recursos (usa `with` o `finally`).

## Prueba/ejecución (opcional)

- Ejecuta `Basic/12_exceptions.py` para ver las demos.

## Material de apoyo

- Código de referencia: `Basic/12_exceptions.py`

## Qué te llevas hoy

- Manejas errores con criterio y escribes código más resistente.

## Siguiente paso

- Clase 13: módulos e imports (organizar tu proyecto y reutilizar código).

---

**⬅️ [Anterior: Clase 11 - Clases](CLASE_11.md) | ⏭️ [Siguiente: Clase 13 - Módulos](CLASE_13.md) | [🏠 Volver al Índice](../../HelloPython.md)**
