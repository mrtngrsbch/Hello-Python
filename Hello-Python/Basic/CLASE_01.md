<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 01**

# Clase 01 — Hola Mundo e I/O

## Apertura narrativa
Comenzamos dándole “voz” al ordenador. Con print decides qué comunicar; con input, qué preguntar. Ese ida y vuelta (mostrar → leer → responder) es el ciclo básico de cualquier programa, desde un script simple hasta un chatbot o una API. Hoy no buscamos memorizar funciones, sino sentir el flujo: escribir, ejecutar, observar, ajustar.

## Por qué te importa
- Te permite crear tu primera interacción real con el usuario.
- Te prepara para validar entradas y formatear salidas en proyectos más grandes.
- Establece el ciclo de trabajo que repetirás en todo el curso.

## Demostración guiada
1) Mostrar un mensaje
```python
print("Hola Python")
```
2) Pedir un dato (pausa de ejecución hasta que el usuario escribe y pulsa Enter)
```python
nombre = input("¿Cómo te llamas? ")
```
3) Responder con un saludo personalizado (f-string = texto con “huecos” que se rellenan)
```python
print(f"Encantado, {nombre}!")
```
Punto clave: input devuelve un str. Si más adelante necesitas un número, lo convertirás (int/float), pero hoy nos centramos en texto.

## Ejercicio dirigido (3–5 min)
- Pide el nombre con input y guarda en una variable.
- Muestra: "Hola, {nombre}" con f-string.
- Pide una frase y vuelve a imprimir: "Tu frase fue: ...".
Sugerencia: si quieres, limpia espacios laterales con `.strip()` al leer.

## Cheatsheet rápido (I/O)
- f-strings: `f"Hola, {nombre}"`
- Concatenación: "Hola, " `+` nombre
- Salto de línea: "Primera\nSegunda"
- Conversión a texto: "Edad: " `+` str(edad)
- print avanzado: `print("a", "b", sep=", ", end="\n")`

## Prueba automática (opcional)
- Ejecuta desde la carpeta Hello-Python: `../.venv/bin/python -m unittest -v`
- Deben pasar los tests de `tests/test_hello_module.py`.

## Errores frecuentes
- Comillas abiertas/cerradas distintas: usa siempre pares "..." o '...'.
- Ejecutar en otra carpeta: confirma tu directorio actual antes de correr.
- Leer pero no usar: si no imprimes el resultado, no verás nada en pantalla.

## Material de apoyo
- Ejemplo: `Basic/00_helloworld.py`
- Módulo para pruebas: `Basic/hello_module.py`

## Qué te llevas hoy
- Ya puedes mantener una mini conversación con el programa (mostrar, pedir, responder).
- Tienes la base para validar entradas y mejorar mensajes.

## Siguiente paso
- Clase 02: variables y strings para transformar y preparar texto con seguridad.

---

**⬅️ [Anterior: Clase 00 - Instalación](CLASE_00.md) | ⏭️ [Siguiente: Clase 02 - Variables](CLASE_02.md) | [🏠 Volver al Índice](../../HelloPython.md)**