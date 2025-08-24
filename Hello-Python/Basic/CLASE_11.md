<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 11**

# Clase 11 — Clases y Objetos (modelado de entidades)

## Apertura narrativa
Las clases son planos; los objetos, las casas construidas con esos planos. Te permiten agrupar estado (atributos) y comportamiento (métodos) de forma coherente.

## Por qué te importa
- Modelas dominios reales (Usuario, Pedido, Producto) de manera expresiva.
- Encapsulas lógica y datos, mejorando mantenibilidad.
- Facilitas pruebas y reutilización.

## Demostración guiada
```python
# Clase simple
class Persona:
    pass

p = Persona()
print(type(p))

# Atributos y constructor (__init__)
class Persona:
    def __init__(self, nombre: str, apellido: str, alias: str | None = None):
        self.nombre = nombre
        self.apellido = apellido
        self.alias = alias

    def nombre_completo(self) -> str:
        if self.alias:
            return f"{self.nombre} {self.apellido} ({self.alias})"
        return f"{self.nombre} {self.apellido}"

p1 = Persona("Brais", "Moure")
print(p1.nombre_completo())

# Alias y mutación (referencias al mismo objeto)
p2 = p1
p2.alias = "mouredev"
print(p1.nombre_completo())  # también refleja el alias
```

## Micro‑kata (7–10 min)
- Crea `Libro(titulo, autor, paginas)` con método `descripcion()`.
- Implementa `CuentaBancaria(titular, saldo=0)` con `depositar()` y `retirar()` (valida saldo suficiente).

## Cheatsheet de clases
- Definición: `class Nombre: ...`
- Constructor: `__init__(self, ...)`
- Métodos: reciben `self` como primer parámetro
- Representación útil (opcional): `__str__`, `__repr__`
- Mutabilidad: múltiples variables pueden apuntar al mismo objeto

## Errores frecuentes
- Olvidar `self` en métodos.
- Usar variables de clase cuando querías de instancia.
- Mutar objetos compartidos sin entender aliasing.

## Prueba/ejecución (opcional)
- Ejecuta `Basic/11_classes.py` para ver las demos.

## Material de apoyo
- Código de referencia: `Basic/11_classes.py`

## Qué te llevas hoy
- Modelas entidades con atributos y métodos y entiendes aliasing/mutación.

## Siguiente paso
- Clase 12: manejo de excepciones (código robusto ante errores).

---

**⬅️ [Anterior: Clase 10 - Funciones](CLASE_10.md) | ⏭️ [Siguiente: Clase 12 - Excepciones](CLASE_12.md) | [🏠 Volver al Índice](../../HelloPython.md)**