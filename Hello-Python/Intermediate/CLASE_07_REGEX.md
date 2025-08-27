<!-- NAVEGACIÓN -->
**📍 [Inicio](../HelloPython.md) > [Intermedio](.) > Clase 07**

# Clase 07 — Regular Expressions (Patrones de búsqueda y validación)

## Apertura narrativa

Las expresiones regulares son como lenguaje mágico para el texto: describen patrones complejos con símbolos elegantes. Desde validar emails hasta extraer datos de logs, regex te da poder de búsqueda y transformación sobre cualquier texto.

## Por qué te importa

- Validas formatos complejos (emails, teléfonos, URLs) con precisión.
- Extraes información específica de grandes volúmenes de texto.
- Limpias y normalizas datos automáticamente.
- Dominas una herramienta universal presente en casi todos los lenguajes.

## Demostración guiada

```python
import re
from typing import List, Optional

def demo_match():
    """Demuestra match() - coincide al inicio"""
    texto = "Python es genial"
    
    # Match simple
    patron = r"Python"
    match = re.match(patron, texto)
    if match:
        print(f"Match encontrado: {match.group()}")
    
    # Match con grupos
    patron_grupo = r"(\w+)\s(\w+)"
    match = re.match(patron_grupo, texto)
    if match:
        print(f"Grupos: {match.groups()}")
        print(f"Grupo 1: {match.group(1)}")

def demo_search():
    """Demuestra search() - busca en cualquier posición"""
    texto = "Mi email es usuario@example.com"
    
    # Buscar email
    patron_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    busqueda = re.search(patron_email, texto)
    if busqueda:
        print(f"Email encontrado: {busqueda.group()}")
        print(f"Posición: {busqueda.start()}-{busqueda.end()}")

def demo_findall():
    """Demuestra findall() - encuentra todas las coincidencias"""
    texto = "Los números son 123, 456 y 789"
    
    # Encontrar todos los números
    numeros = re.findall(r"\d+", texto)
    print(f"Números encontrados: {numeros}")
    
    # Encontrar palabras
    palabras = re.findall(r"\b\w+\b", texto)
    print(f"Palabras: {palabras}")

def demo_sub():
    """Demuestra sub() - reemplaza patrones"""
    texto = "Mi número es 123-456-7890"
    
    # Reemplazar números
    nuevo_texto = re.sub(r"\d", "*", texto)
    print(f"Texto con números ocultos: {nuevo_texto}")
    
    # Formatear teléfono
    telefono_formateado = re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", texto)
    print(f"Teléfono formateado: {telefono_formateado}")

def demo_split():
    """Demuestra split() - divide por patrón"""
    texto = "Python,JavaScript,Python,Java"
    
    # Split por coma
    lenguajes = re.split(r",", texto)
    print(f"Lenguajes: {lenguajes}")
    
    # Split por varios espacios
    texto_espacios = "Python    es    genial"
    palabras = re.split(r"\s+", texto_espacios)
    print(f"Palabras sin espacios extra: {palabras}")

def validar_email(email: str) -> bool:
    """Valida formato de email"""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

def extraer_urls(texto: str) -> List[str]:
    """Extrae URLs de un texto"""
    patron_url = r"https?://[\w.-]+/\S*"
    return re.findall(patron_url, texto)

def limpiar_texto(texto: str) -> str:
    """Limpia texto eliminando caracteres especiales"""
    # Eliminar caracteres no alfanuméricos excepto espacios
    limpio = re.sub(r"[^\w\s]", "", texto)
    # Eliminar espacios múltiples
    limpio = re.sub(r"\s+", " ", limpio)
    return limpio.strip()

# Demostración completa
if __name__ == "__main__":
    print("=== DEMOSTRACIÓN DE REGEX ===")
    
    # Match
    print("\n1. Match():")
    demo_match()
    
    # Search
    print("\n2. Search():")
    demo_search()
    
    # Findall
    print("\n3. Findall():")
    demo_findall()
    
    # Sub
    print("\n4. Sub():")
    demo_sub()
    
    # Split
    print("\n5. Split():")
    demo_split()
    
    # Validaciones prácticas
    print("\n6. Validaciones:")
    emails = ["test@example.com", "invalid-email", "user@domain.co.uk"]
    for email in emails:
        print(f"{email}: {'Válido' if validar_email(email) else 'Inválido'}")
    
    # Extracción de URLs
    texto_con_urls = "Visita https://python.org y http://docs.python.org para más info"
    urls = extraer_urls(texto_con_urls)
    print(f"URLs encontradas: {urls}")
    
    # Limpieza de texto
    texto_sucio = "Python!!! es... genial???   Muy   útil"
    texto_limpio = limpiar_texto(texto_sucio)
    print(f"Texto limpio: '{texto_limpio}'")
```

## Micro-kata (15-18 min)
- **Ejercicio 1**: Crea un validador de números de tarjeta de crédito.
- **Ejercicio 2**: Implementa un extractor de hashtags de redes sociales.
- **Ejercicio 3**: Desarrolla un validador de contraseñas seguras.
- **Ejercicio 4**: Crea un parser de direcciones IP.
- **Ejercicio 5**: Implementa un extractor de precios de texto.

## Cheatsheet de regex

- **Metacaracteres básicos**:
  - `.`: cualquier carácter excepto nueva línea
  - `^`: inicio de línea
  - `$`: fin de línea
  - `\d`: dígito (equivale a [0-9])
  - `\w`: palabra (letras, dígitos, guión bajo)
  - `\s`: espacio en blanco
  - `\b`: límite de palabra
- **Cuantificadores**:
  - `*`: 0 o más
  - `+`: 1 o más
  - `?`: 0 o 1
  - `{n}`: exactamente n
  - `{n,}`: n o más
  - `{n,m}`: entre n y m
- **Grupos y rangos**:
  - `()`: grupo de captura
  - `[]`: conjunto de caracteres
  - `|`: alternativa (o)
- **Flags útiles**:
  - `re.IGNORECASE` (re.I): ignora mayúsculas/minúsculas
  - `re.MULTILINE` (re.M): ^ y $ coinciden con inicio/fin de línea
  - `re.DOTALL` (re.S): . incluye nueva línea
- **Métodos principales**:
  - `re.match()`: coincide al inicio
  - `re.search()`: busca en cualquier posición
  - `re.findall()`: encuentra todas las coincidencias
  - `re.sub()`: reemplaza
  - `re.split()`: divide

## Errores frecuentes

- Patrones demasiado permisivos o restrictivos.
- No escapar caracteres especiales (`.` → `\.`).
- Olvidar los límites (`^` y `$`) cuando se necesita coincidencia exacta.
- Abusar de regex para problemas simples (usar str métodos cuando sea más simple).
- No considerar el rendimiento con patrones complejos.

## Prueba/ejecución (opcional)

- Ejecuta `Intermediate/07_regular_expressions.py` para ver las demos.
- Prueba tus patrones en https://regex101.com/
- Crea un banco de pruebas para tus validadores.

## Material de apoyo

- Código de referencia: `Intermediate/07_regular_expressions.py`
- Herramientas online: regex101.com, regexr.com
- Librerías: `regex` (regex avanzado), `re` (built-in)
- Recursos: Regular Expressions Cookbook

## Qué te llevas hoy

- Dominas patrones complejos de búsqueda y validación.
- Puedes extraer y transformar texto con precisión.
- Tienes una herramienta universal para cualquier lenguaje.

## Siguiente paso

- Clase 08: Python Package Manager para gestionar dependencias y crear entornos reproducibles.

---

**⬅️ [Anterior: Clase 06 - Manejo de Archivos](CLASE_06_FILE_HANDLING.md) | ⏭️ [Siguiente: Clase 08 - Gestor de Paquetes](CLASE_08_PACKAGE_MANAGER.md) | [🏠 Volver al Índice](../HelloPython.md)**
