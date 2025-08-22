# Clase 06 — File Handling (Manejo seguro de archivos)

## Apertura narrativa
Los archivos son la memoria persistente de tus programas. Dominar su manejo es como ser un archivista experto: sabes guardar, organizar, leer y manipular información de forma segura y eficiente.

## Por qué te importa
- Persistes datos entre ejecuciones del programa.
- Trabajas con diferentes formatos (texto, JSON, CSV).
- Manejas archivos grandes sin cargar todo en memoria.
- Creas pipelines de procesamiento de datos reales.

## Demostración guiada
```python
import json
import csv
from pathlib import Path

# Manejo básico de archivos de texto
def escribir_texto(ruta: str, contenido: str) -> None:
    """Escribe contenido en archivo de texto"""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def leer_texto(ruta: str) -> str:
    """Lee contenido de archivo de texto"""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "Archivo no encontrado"

# Trabajo con JSON
def guardar_json(ruta: str, datos: dict) -> None:
    """Guarda datos en formato JSON"""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

def cargar_json(ruta: str) -> dict:
    """Carga datos desde JSON"""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {"error": "JSON inválido"}

# Trabajo con CSV
def escribir_csv(ruta: str, datos: list[dict]) -> None:
    """Escribe datos en formato CSV"""
    if not datos:
        return
    
    with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)

def leer_csv(ruta: str) -> list[dict]:
    """Lee datos desde CSV"""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            return list(reader)
    except FileNotFoundError:
        return []

# Manejo de rutas con pathlib
def crear_estructura_directorios(base_path: str) -> None:
    """Crea estructura de directorios"""
    base = Path(base_path)
    
    # Crear directorios
    (base / "datos" / "json").mkdir(parents=True, exist_ok=True)
    (base / "datos" / "csv").mkdir(parents=True, exist_ok=True)
    (base / "logs").mkdir(parents=True, exist_ok=True)
    
    print("Estructura creada en:", base)

# Procesamiento de archivos grandes
def procesar_archivo_grande(ruta: str) -> dict:
    """Procesa archivo grande línea por línea"""
    contador = {"lineas": 0, "palabras": 0, "caracteres": 0}
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                contador["lineas"] += 1
                contador["palabras"] += len(linea.split())
                contador["caracteres"] += len(linea)
    except FileNotFoundError:
        return {"error": "Archivo no encontrado"}
    
    return contador

# Demostración completa
if __name__ == "__main__":
    # Crear estructura de directorios
    crear_estructura_directorios("demo_archivos")
    
    # Datos de ejemplo
    usuarios = [
        {"nombre": "Ana García", "edad": 28, "email": "ana@example.com"},
        {"nombre": "Carlos López", "edad": 32, "email": "carlos@example.com"},
        {"nombre": "Beatriz Martín", "edad": 25, "email": "bea@example.com"}
    ]
    
    # Guardar y leer JSON
    ruta_json = "demo_archivos/datos/json/usuarios.json"
    guardar_json(ruta_json, {"usuarios": usuarios})
    datos_json = cargar_json(ruta_json)
    print("Datos JSON:", datos_json)
    
    # Guardar y leer CSV
    ruta_csv = "demo_archivos/datos/csv/usuarios.csv"
    escribir_csv(ruta_csv, usuarios)
    datos_csv = leer_csv(ruta_csv)
    print("Datos CSV:", datos_csv)
    
    # Archivo de texto
    ruta_txt = "demo_archivos/logs/info.txt"
    escribir_texto(ruta_txt, "Información del sistema\nVersión: 1.0")
    contenido = leer_texto(ruta_txt)
    print("Contenido TXT:", contenido)
    
    # Limpiar archivos de demo
    import shutil
    shutil.rmtree("demo_archivos", ignore_errors=True)
    print("Demo limpiada")
```

## Micro-kata (15-18 min)
- **Ejercicio 1**: Crea un sistema de backup que copie archivos importantes.
- **Ejercicio 2**: Implementa un procesador de logs que extraiga errores específicos.
- **Ejercicio 3**: Desarrolla un conversor entre JSON, CSV y texto plano.
- **Ejercicio 4**: Crea un buscador de archivos por contenido (grep simple).
- **Ejercicio 5**: Implementa un sistema de logs rotativos por tamaño.

## Cheatsheet de file handling
- **Modos de apertura**:
  - `'r'`: lectura (por defecto)
  - `'w'`: escritura (sobrescribe)
  - `'a'`: append (añadir)
  - `'x'`: crear (falla si existe)
  - `'b'`: binario (rb, wb)
- **Context managers**:
  ```python
  with open('archivo.txt', 'r') as f:
      contenido = f.read()
  # Se cierra automáticamente
  ```
- **Métodos útiles**:
  - `.read()`: todo el contenido
  - `.readline()`: una línea
  - `.readlines()`: todas las líneas como lista
  - `.write(texto)`: escribir string
  - `.writelines(lista)`: escribir lista de strings
- **Pathlib**:
  - `Path("ruta").exists()`
  - `Path("ruta").mkdir(parents=True)`
  - `Path("ruta").glob("*.txt")`
- **Formatos**:
  - JSON: `json.dump()`, `json.load()`
  - CSV: `csv.writer()`, `csv.DictReader()`

## Errores frecuentes
- No usar `with open()` y olvidar cerrar archivos.
- Usar encoding incorrecto (especialmente UTF-8).
- No manejar excepciones de archivos (FileNotFoundError, PermissionError).
- Cargar archivos grandes completos en memoria.
- Confundir rutas relativas y absolutas.
- No crear directorios padre antes de escribir archivos.

## Prueba/ejecución (opcional)
- Ejecuta `Intermediate/06_file_handling.py` para ver las demos.
- Crea archivos de prueba con diferentes formatos.
- Practica con archivos reales de tu sistema.

## Material de apoyo
- Código de referencia: `Intermediate/06_file_handling.py`
- Módulos: `pathlib`, `shutil`, `os`, `tempfile`
- Herramientas: `pandas` para archivos grandes
- Seguridad: siempre validar rutas de entrada

## Qué te llevas hoy
- Dominas el manejo seguro de archivos en diferentes formatos.
- Puedes crear sistemas de persistencia robustos.
- Sabes procesar archivos grandes sin problemas de memoria.

## Siguiente paso
- Clase 07: Regular Expressions para patrones de búsqueda y validación avanzada.