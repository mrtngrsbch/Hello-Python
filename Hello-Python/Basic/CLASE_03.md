# Clase 03 — Operadores (Aritméticos, Comparación y Lógicos)

## Apertura narrativa
Los operadores son el lenguaje de las decisiones y los cálculos. Con ellos sumas un total, decides si una condición se cumple, o combinas reglas. Hoy verás cómo pensar y expresar operaciones de manera clara y segura.

## Por qué te importa
- Aritmética fiable para cálculos (precios, promedios, porcentajes).
- Comparación para validar entradas y ordenar decisiones.
- Lógica para combinar reglas (`and`/`or`/`not`) con precedencia clara.

## Demostración guiada
```python
# Aritmética
subtotal = 120
iva = 0.21
impuesto = subtotal * iva
precio_final = subtotal + impuesto
print("Precio final:", precio_final)

# Comparación
mayor_de_edad = 18
edad = 20
print("¿Es mayor de edad?", edad >= mayor_de_edad)

# Lógica
es_estudiante = True
aplica_descuento = (edad < 26) or es_estudiante
print("¿Descuento aplica?", aplica_descuento)
```
## Puntos clave
- Usa paréntesis cuando dudes de la precedencia.
- Evita expresiones densas: crea variables intermedias.

## Micro‑kata (10–12 min)
1) Calculadora mínima (solo `+`, `-`, `*`, `/`): pide dos números y la operación, y muestra el resultado (maneja división por cero).
2) Comparador: pide dos números y muestra si el primero es `>`, `<` o `==` que el segundo.
3) Paridad: pide un entero y dice si es par o impar usando `%`.

## Cheatsheet completo
- Aritméticos: `+`, `-`, `*`, `/` (float), `//` (entera), `%` (módulo), `**` (potencia)
- Comparación: `==`, `!=`, `>`, `>=`, `<`, `<=`
- Lógicos: `and`, `or`, `not`
- Strings: `+` concatena, `*` repite (solo int)
- Orden y paréntesis: `**` `>` `*`, `/`, `//`, `%` `>` `+`, `-`; luego comparaciones; luego lógicos (`and` antes que `or`). Usa paréntesis si tienes dudas.

## Errores frecuentes
- División por cero: ZeroDivisionError.
- Comparar strings por longitud sin querer: usa `len(...)` explícitamente si eso buscas.
- Precedencia confusa: añade paréntesis para hacer la intención explícita.

## Prueba automática
- Desde Hello-Python: `../.venv/bin/python -m unittest -v`
- Deben pasar los tests de `tests/test_operators_utils.py`.

## Material de apoyo
- Utilidades de operadores: `Basic/operators_utils.py`
- Pruebas: `tests/test_operators_utils.py`

## Qué te llevas hoy
- Sabes combinar operadores aritméticos, de comparación y lógicos con claridad.
- Puedes validar entradas y calcular resultados evitando trampas comunes.

## Siguiente paso
- Condicionales: usarás operadores para tomar decisiones (`if`/`elif`/`else`) de manera estructurada.