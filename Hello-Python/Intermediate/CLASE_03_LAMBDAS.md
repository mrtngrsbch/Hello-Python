<!-- NAVEGACIÓN -->
**📍 [Inicio](../HelloPython.md) > [Intermedio](.) > Clase 03**

# Clase 03 — Lambdas: Funciones Anónimas y Elegantes

## Apertura narrativa

Las lambdas son funciones express: pequeñas, sin nombre, perfectas para tareas puntuales. Como un café rápido en vez de una cena formal: cuando necesitas una función simple sin la ceremonia de `def`, las lambdas te dan poder inmediato.

## Por qué te importa

- Creas funciones simples al vuelo sin declararlas formalmente.
- Perfectas para usar con `map()`, `filter()`, `sorted()` y funciones de orden superior.
- Hacen tu código más conciso y funcional.
- Ideal para transformaciones y filtros rápidos.

## Demostración guiada

```python
# Lambda básica
cuadrado = lambda x: x**2
print("Cuadrado de 5:", cuadrado(5))

# Lambda con múltiples parámetros
sumar = lambda x, y: x + y
print("Suma:", sumar(3, 7))

# Lambda con condicionales
es_par = lambda x: "par" if x % 2 == 0 else "impar"
print("8 es", es_par(8))

# Usando con map()
números = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, números))
print("Cuadrados con map:", cuadrados)

# Usando con filter()
pares = list(filter(lambda x: x % 2 == 0, números))
print("Pares con filter:", pares)

# Usando con sorted()
palabras = ["Python", "es", "increíble", "para", "datos"]
ordenadas_longitud = sorted(palabras, key=lambda x: len(x))
print("Ordenadas por longitud:", ordenadas_longitud)

# Lambda en diccionarios
usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Beatriz", "edad": 22}
]
ordenados_edad = sorted(usuarios, key=lambda u: u["edad"])
print("Usuarios ordenados por edad:", ordenados_edad)

# Lambda con valor por defecto (usando or)
get_name = lambda user: user.get("nombre", "Anónimo")
print("Nombre:", get_name({"nombre": "Juan"}))
print("Nombre anónimo:", get_name({}))
```

## Micro-kata (10-12 min)

- **Ejercicio 1**: Crea una lambda que calcule el área de un círculo dado su radio.
- **Ejercicio 2**: Usa lambda con `filter()` para obtener solo palabras con más de 3 letras.
- **Ejercicio 3**: Ordena una lista de tuplas (nombre, edad) por edad descendente usando lambda.
- **Ejercicio 4**: Crea una lambda que valide si un email tiene formato básico.
- **Ejercicio 5**: Combina map y filter con lambdas para procesar datos complejos.

## Cheatsheet de lambdas

- Sintaxis: `lambda parámetros: expresión`
- Múltiples parámetros: `lambda x, y: x + y`
- Condicionales: `lambda x: "verdadero" if condición else "falso"`
- Sin parámetros: `lambda: valor_constante`
- **Funciones útiles**:
  - `map(función, iterable)` → aplica función a cada elemento
  - `filter(función, iterable)` → filtra elementos
  - `sorted(iterable, key=función)` → ordena con criterio personalizado
  - `reduce(función, iterable)` → reduce a un solo valor (importar de functools)
- **Limitaciones**:
  - Solo una expresión (no puede tener múltiples statements)
  - No puede tener docstrings
  - Úsala para funciones simples, no complejas

## Errores frecuentes

- Intentar usar múltiples líneas (lambdas solo permiten una expresión).
- Abusar de la complejidad (si es muy compleja, usa def).
- Olvidar que lambdas no tienen nombre (no son reutilizables fácilmente).
- No usar paréntesis cuando hay condicionales complejos.
- Confundir el scope de las variables (cuidado con closures).

## Prueba/ejecución (opcional)

- Ejecuta `Intermediate/03_lambdas.py` para ver las demos.
- Compara la legibilidad entre lambda y funciones normales.
- Benchmark: mide la velocidad vs funciones definidas con def.

## Material de apoyo

- Código de referencia: `Intermediate/03_lambdas.py`
- Módulos relacionados: `functools`, `operator`
- PEP 8: guía sobre cuándo usar lambdas vs funciones nombradas

## Qué te llevas hoy

- Creas funciones anónimas para transformaciones rápidas.
- Dominas el uso de lambdas con funciones de orden superior.
- Sabes cuándo usar lambda vs funciones nombradas.

## Siguiente paso

- Clase 04: funciones de orden superior (map, filter, reduce, decoradores).

---

**⬅️ [Anterior: Clase 02 - Retos Prácticos](CLASE_02_CHALLENGES.md) | ⏭️ [Siguiente: Clase 04 - Funciones de Orden Superior](CLASE_04_HIGHER_ORDER.md) | [🏠 Volver al Índice](../HelloPython.md)**
