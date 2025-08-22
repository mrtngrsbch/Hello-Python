# Clase 01 — List Comprehension (Transformaciones elegantes)

## Apertura narrativa
List comprehension es la forma pitónica de decir "para cada elemento en esta colección, haz esto y devuelve una nueva lista". Es como tener un mini-fabricante de listas que combina bucles, filtros y transformaciones en una sola línea elegante.

## Por qué te importa
- Reduce 3-4 líneas de código a una sola expresión legible.
- Mejora la performance al ser más eficiente que los bucles tradicionales.
- Hace tu código más "pitónico" y fácil de mantener.
- Perfecto para transformaciones simples y filtros de colecciones.

## Demostración guiada
```python
# List comprehension básica
números = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in números]
print("Cuadrados:", cuadrados)

# Con filtro
pares = [x for x in números if x % 2 == 0]
print("Pares:", pares)

# Transformación compleja
palabras = ["python", "es", "genial"]
mayúsculas = [palabra.upper() for palabra in palabras if len(palabra) > 2]
print("Mayúsculas:", mayúsculas)

# List comprehension anidada
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [item for fila in matriz for item in fila]
print("Matriz plana:", plana)

# Con enumerate para obtener índices
enumerado = [(i, val) for i, val in enumerate(números)]
print("Enumerado:", enumerado)

# Generar pares (x, y)
pares = [(x, y) for x in range(3) for y in range(3) if x != y]
print("Pares únicos:", pares)

# Alternativa con dict comprehension (bonus)
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print("Dict comprehension:", cuadrados_dict)
```

## Micro-kata (12-15 min)
- Dada una lista de números, crea una nueva lista con solo los números positivos elevados al cuadrado.
- De una lista de palabras, filtra las que empiecen con vocal y conviértelas a mayúsculas.
- Crea una lista de todos los números primos menores que 50 usando list comprehension.
- Aplanar una lista de listas de listas (3 niveles) usando list comprehension anidada.

## Cheatsheet de list comprehension
- Sintaxis básica: `[expresión for elemento in iterable]`
- Con filtro: `[expresión for elemento in iterable if condición]`
- Múltiples condiciones: `[exp for x in iterable if cond1 if cond2]`
- Anidada: `[exp for x in iterable for y in otro_iterable]`
- Variables temporales: `[y for x in iterable for y in x]`
- Alternativas:
  - Dict comprehension: `{clave: valor for elemento in iterable}`
  - Set comprehension: `{expresión for elemento in iterable}`
- Performance: más rápido que append en bucles
- Legibilidad: mejor para operaciones simples, no abuses en complejidades

## Errores frecuentes
- Abusar de la complejidad: si necesitas más de 2-3 condiciones, usa bucles.
- Olvidar los corchetes: `[...]` es obligatorio para list comprehension.
- Confundir el orden en anidaciones: `for x in ... for y in ...`.
- Side effects en la expresión: evita funciones con efectos secundarios.

## Prueba/ejecución (opcional)
- Ejecuta `Intermediate/01_list_comprehension.py` para ver las demos.
- Compara la velocidad con bucles tradicionales para listas grandes.

## Material de apoyo
- Código de referencia: `Intermediate/01_list_comprehension.py`
- PEP 202: List Comprehensions

## Qué te llevas hoy
- Dominas la creación elegante y eficiente de listas transformadas.
- Puedes reemplazar bucles complejos con expresiones concisas.

## Siguiente paso
- Clase 02: Challenges para practicar todo lo aprendido con ejercicios integrados.