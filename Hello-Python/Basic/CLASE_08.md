<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 08**

# Clase 08 — Condicionales (tomar decisiones)

## Apertura narrativa
Los condicionales son tus semáforos lógicos: te permiten decidir qué camino tomar según los datos. Desde validar formularios hasta activar descuentos, `if`/`elif`/`else` son el corazón del control de flujo.

## Por qué te importa
- Activar o desactivar bloques de código según condiciones.
- Expresar reglas de negocio de forma clara y legible.
- Evitar errores típicos al comparar, combinar condiciones y tratar valores vacíos.

## Demostración guiada
```python
x = 15
if x > 10 and x < 20:
    print("Rango medio")
elif x == 20:
    print("En el límite superior")
else:
    print("Fuera de rango")

# Truthiness: valores "falsy" (", 0, None, colecciones vacías)
s = ""
if not s:
    print("Cadena vacía")

# Comparación exacta
if s == "Hola":
    print("Coincide")
```

## Micro‑kata (7–10 min)
- Pide una `edad` y clasifícala: `< 18` = "menor", `18–64` = "adulto", `>= 65` = "senior".
- Valida una contraseña: longitud `>= 8`, contiene dígito y letra; imprime mensajes claros.

## Cheatsheet de condicionales
- Estructura: `if`, `elif`, `else` (en orden mutuamente excluyente)
- Comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Lógicos: `and`, `or`, `not` (usa paréntesis si hay duda de precedencia)
- Pertenencia/identidad (avanzado): `in`, `not in`, `is`, `is not` (cuidado, `is` no es igual que `==`)
- Truthiness: vacío/`0`/`None`/colección vacía evalúan a `False`

## Errores frecuentes
- Escribir `=` en lugar de `==` al comparar.
- Ramas inalcanzables por orden incorrecto de condiciones.
- Olvidar paréntesis cuando mezclas `and` y `or` y cambia la intención.

## Prueba/ejecución (opcional)
- Ejecuta `Basic/08_conditionals.py` para ver las demos.

## Material de apoyo
- Código de referencia: `Basic/08_conditionals.py`

## Qué te llevas hoy
- Tomas decisiones claras con `if`/`elif`/`else` y dominas comparaciones y truthiness.

## Siguiente paso
- Clase 09: bucles (`while`, `for`, `break`, `continue`, `else`).

---

**⬅️ [Anterior: Clase 07 - Diccionarios](CLASE_07.md) | ⏭️ [Siguiente: Clase 09 - Bucles](CLASE_09.md) | [🏠 Volver al Índice](../../HelloPython.md)**