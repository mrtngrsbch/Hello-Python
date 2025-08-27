<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 10**

# Clase 10 — Funciones (organizar y reutilizar lógica)

## Apertura narrativa

Las funciones son bloques de construcción: encapsulan una tarea con nombre y te permiten reutilizarla sin repetir código. Son la base para escalar desde scripts simples hasta proyectos serios.

## Por qué te importa

- Reutilizas lógica y reduces duplicación.
- Haces tu código más legible y testeable.
- Controlas entradas (parámetros) y salidas (`return`).

## Demostración guiada

```python
# Definición básica y parámetros

def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Brais"))  # Hola, Brais!

# Return vs print

def suma(a, b):
    return a + b  # devolver valores permite componer funciones

resultado = suma(2, 3)
print(resultado)

# Parámetros por palabra clave y valores por defecto

def enviar_email(dest, asunto, cuerpo="(vacío)"):
    print(f"Para: {dest} — {asunto} — {cuerpo}")

enviar_email(dest="a@b.com", asunto="Hola")

# *args y **kwargs

def total(*nums, **opciones):
    t = sum(nums)
    if opciones.get("iva"):
        t *= 1.21
    return t

print(total(10, 20, 30, iva=True))

# Documentación (docstring)

def dividir(a: float, b: float) -> float:
    """Divide a entre b.
    Lanza ValueError si b es 0.
    """
    if b == 0:
        raise ValueError("b no puede ser 0")
    return a / b
```

## Micro‑kata (7–10 min)

- Escribe `es_palindromo(texto)` que ignore espacios y mayúsculas.
- Implementa `aplicar_descuento(precio, porcentaje=10)` con validaciones.

## Cheatsheet de funciones

- Definición: `def nombre(params): ... return valor`
- Parámetros: posicionales, palabra clave, por defecto, `*args`, `**kwargs`
- Docstrings: explican propósito, parámetros y retornos
- Tipado opcional: `def f(x: int) -> int:` (ayuda a herramientas)
- `return` vs `print`: devuelve datos para componer; `print` solo muestra

## Errores frecuentes

- Olvidar `return` (la función devuelve `None`).
- Usar `print` en vez de devolver valores dificulta tests.
- Mutar argumentos mutables por defecto (usa `None` y crea dentro).

## Prueba/ejecución (opcional)

- Ejecuta `Basic/10_functions.py` para ver las demos.

## Material de apoyo

- Código de referencia: `Basic/10_functions.py`

## Qué te llevas hoy

- Diseñas funciones claras, con parámetros adecuados y retornos útiles.

## Siguiente paso

- Clase 11: clases y objetos (modela entidades con comportamiento).

---

**⬅️ [Anterior: Clase 09 - Bucles](CLASE_09.md) | ⏭️ [Siguiente: Clase 11 - Clases](CLASE_11.md) | [🏠 Volver al Índice](../../HelloPython.md)**
