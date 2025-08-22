# Clase 04 — Higher Order Functions (Funciones que operan sobre funciones)

## Apertura narrativa
Las Higher Order Functions son como directores de orquesta: no tocan la música, pero dirigen a los músicos (funciones) para crear sinfonías complejas. Te permiten escribir código más genérico, reutilizable y funcional.

## Por qué te importa
- Escribes código más genérico y reutilizable.
- Dominas patrones funcionales avanzados.
- Preparas el terreno para conceptos como decoradores y closures.
- Mejoras la composición y abstracción de tu código.

## Demostración guiada
```python
from functools import reduce
from typing import Callable, List, Any

# Función que devuelve otra función
def crear_multiplicador(factor: int) -> Callable[[int], int]:
    """Crea una función multiplicadora"""
    return lambda x: x * factor

# Función que toma otra función como parámetro
def aplicar_operacion(numeros: List[int], 
                     operacion: Callable[[int], int]) -> List[int]:
    """Aplica una operación a cada número"""
    return [operacion(n) for n in numeros]

# Uso de map()
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print("Duplicados:", duplicados)

# Uso de filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# Uso de reduce()
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)

# Función decoradora simple
def logger(func: Callable) -> Callable:
    """Decorador simple que logea la ejecución"""
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@logger
def cuadrado(x: int) -> int:
    return x ** 2

print("Cuadrado con logging:", cuadrado(5))

# Composición de funciones
def componer(f: Callable, g: Callable) -> Callable:
    """Compone dos funciones: f(g(x))"""
    return lambda x: f(g(x))

# Uso de la composición
incrementar = lambda x: x + 1
duplicar = lambda x: x * 2

incrementar_y_duplicar = componer(duplicar, incrementar)
print("Incrementar y duplicar 5:", incrementar_y_duplicar(5))

# Funciones de orden superior personalizadas
def ordenar_por_clave(lista: List[Any], 
                     clave: Callable[[Any], Any]) -> List[Any]:
    """Ordena una lista usando una función clave"""
    return sorted(lista, key=clave)

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Beatriz", "edad": 22}
]

ordenados_por_edad = ordenar_por_clave(usuarios, lambda u: u["edad"])
print("Ordenados por edad:", ordenados_por_edad)
```

## Micro-kata (15-18 min)
- **Ejercicio 1**: Crea una función `aplicar_si` que tome una lista y aplique una función solo si cumplen una condición.
- **Ejercicio 2**: Implementa `pipe` que tome una lista de funciones y las aplique secuencialmente.
- **Ejercicio 3**: Crea un decorador que cachee resultados de funciones costosas.
- **Ejercicio 4**: Escribe una función `particionar` que divida una lista en dos según una condición.
- **Ejercicio 5**: Implementa `aplicar_operaciones` que tome una lista de funciones y las aplique a un valor.

## Cheatsheet de Higher Order Functions
- **Funciones incorporadas**:
  - `map(función, iterable)` → transforma elementos
  - `filter(función, iterable)` → filtra elementos
  - `reduce(función, iterable)` → reduce a un solo valor
  - `sorted(iterable, key=función)` → ordena con criterio
- **Funciones que devuelven funciones**:
  - Factory functions: `crear_función(parametros)`
  - Closures: funciones que recuerdan su entorno
- **Funciones que toman funciones**:
  - Callbacks: funciones pasadas como parámetros
  - Decorators: funciones que modifican otras funciones
- **Composición**:
  - `compose(f, g)(x) = f(g(x))`
  - `pipe(funciones)(valor)` = aplicar secuencialmente
- **Patrones útiles**:
  - Currying: convertir f(a,b) en f(a)(b)
  - Partial application: fijar algunos parámetros

## Errores frecuentes
- No entender el orden de aplicación en composición.
- Abusar de la complejidad y hacer el código ilegible.
- Olvidar que las funciones son objetos de primera clase.
- No manejar correctamente los tipos en funciones genéricas.
- Confundir `map`/`filter` con list comprehension.

## Prueba/ejecución (opcional)
- Ejecuta `Intermediate/04_higher_order_functions.py` para ver las demos.
- Compara diferentes enfoques para el mismo problema.
- Practica creando tus propias funciones de orden superior.

## Material de apoyo
- Código de referencia: `Intermediate/04_higher_order_functions.py`
- Módulos: `functools` (reduce, partial, wraps)
- Libro: "Functional Programming in Python"

## Qué te llevas hoy
- Dominas funciones que operan sobre otras funciones.
- Escribes código más genérico y reutilizable.
- Preparas el terreno para patrones avanzados como decoradores.

## Siguiente paso
- Clase 05: Error Types para manejar excepciones con elegancia y precisión.