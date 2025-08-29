<!-- NAVEGACIÓN -->
**📍 [Inicio](../HelloPython.md) > [Intermedio](.) > Clase 08**

# Clase 08 — Python Package Manager (Gestión profesional de dependencias)

## Apertura narrativa

El gestor de paquetes es como el sistema nervioso de tu proyecto: conecta todas las piezas externas que necesitas. Dominar pip y los entornos virtuales te permite crear proyectos reproducibles y compartibles.

## Por qué te importa

- Gestiona dependencias de forma profesional.
- Crea entornos aislados para cada proyecto.
- Comparte proyectos con requisitos exactos.
- Instala y actualiza paquetes de forma segura.
- Trabaja con paquetes populares como numpy, pandas, requests.

## Demostración guiada

```python
# Este archivo demuestra el uso de paquetes populares
# Para ejecutar: primero instala los paquetes necesarios

# pip install numpy pandas requests

def demo_numpy():
    """Demuestra uso básico de NumPy"""
    try:
        import numpy as np
        
        # Crear arrays
        arr = np.array([1, 2, 3, 4, 5])
        print("Array NumPy:", arr)
        print("Tipo:", type(arr))
        print("Media:", np.mean(arr))
        print("Desviación estándar:", np.std(arr))
        
        # Operaciones vectorizadas
        cuadrados = arr ** 2
        print("Cuadrados:", cuadrados)
        
        # Array 2D
        matriz = np.array([[1, 2], [3, 4]])
        print("Matriz:\n", matriz)
        print("Determinante:", np.linalg.det(matriz))
        
    except ImportError:
        print("NumPy no está instalado. Ejecuta: pip install numpy")

def demo_pandas():
    """Demuestra uso básico de Pandas"""
    try:
        import pandas as pd
        
        # Crear DataFrame
        datos = {
            'nombre': ['Ana', 'Carlos', 'Beatriz'],
            'edad': [25, 30, 22],
            'ciudad': ['Madrid', 'Barcelona', 'Valencia']
        }
        df = pd.DataFrame(datos)
        print("DataFrame Pandas:")
        print(df)
        print("\nResumen estadístico:")
        print(df.describe())
        
        # Filtrar datos
        mayores_25 = df[df['edad'] > 25]
        print("\nMayores de 25:")
        print(mayores_25)
        
    except ImportError:
        print("Pandas no está instalado. Ejecuta: pip install pandas")

def demo_requests():
    """Demuestra uso básico de Requests"""
    try:
        import requests
        
        # Hacer petición GET
        url = "https://jsonplaceholder.typicode.com/posts/1"
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()  # Lanza excepción si hay error HTTP
            
            print("Petición exitosa!")
            print("Status:", respuesta.status_code)
            print("Headers:", dict(respuesta.headers))
            print("JSON:", respuesta.json())
            
        except requests.exceptions.RequestException as e:
            print(f"Error en la petición: {e}")
            
    except ImportError:
        print("Requests no está instalado. Ejecuta: pip install requests")

def crear_requirements():
    """Crea archivo requirements.txt de ejemplo"""
    requirements = """# Dependencias del proyecto
numpy>=1.21.0
pandas>=1.3.0
requests>=2.25.0

# Desarrollo
pytest>=6.0.0
black>=21.0.0"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    print("Archivo requirements.txt creado")

def gestionar_paquetes():
    """Demuestra comandos comunes de pip"""
    print("=== COMANDOS ÚTILES DE PIP ===")
    print("Instalar paquete:")
    print("  pip install numpy")
    print("  pip install numpy==1.21.0")
    print("  pip install numpy>=1.21.0")
    
    print("\nInstalar desde requirements:")
    print("  pip install -r requirements.txt")
    
    print("\nDesinstalar paquete:")
    print("  pip uninstall numpy")
    
    print("\nListar paquetes instalados:")
    print("  pip list")
    
    print("\nBuscar paquetes:")
    print("  pip search pandas")
    
    print("\nVer información del paquete:")
    print("  pip show numpy")
    
    print("\nActualizar paquete:")
    print("  pip install --upgrade numpy")

def crear_setup_py():
    """Crea archivo setup.py básico"""
    setup_content = '''from setuptools import setup, find_packages

setup(
    name="mi-proyecto",
    version="0.1.0",
    description="Mi primer proyecto Python",
    author="Tu Nombre",
    author_email="tu@email.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "requests>=2.25.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)'''
    
    with open('setup.py', 'w') as f:
        f.write(setup_content)
    print("Archivo setup.py creado")

# Demostración completa
if __name__ == "__main__":
    print("=== PYTHON PACKAGE MANAGER ===")
    
    # Crear archivos de configuración
    crear_requirements()
    crear_setup_py()
    
    # Mostrar comandos
    gestionar_paquetes()
    
    # Demostrar paquetes (si están instalados)
    print("\n=== DEMOSTRACIONES ===")
    demo_numpy()
    demo_pandas()
    demo_requests()
    
    # Limpiar archivos de demo
    import os
    try:
        os.remove('requirements.txt')
        os.remove('setup.py')
    except FileNotFoundError:
        pass
    
    print("\n=== RECURSOS ADICIONALES ===")
    print("PyPI: https://pypi.org/")
    print("Documentación paquetes: https://docs.python.org/3/library/")
    print("Entornos virtuales: python -m venv mi_entorno")
```

## Micro-kata (12-15 min)

- **Ejercicio 1**: Crea un proyecto con requirements.txt y setup.py.
- **Ejercicio 2**: Investiga y usa 3 paquetes nuevos de PyPI.
- **Ejercicio 3**: Crea un entorno virtual y instala tus dependencias.
- **Ejercicio 4**: Publica un paquete simple en TestPyPI.
- **Ejercicio 5**: Automatiza la instalación con un script de setup.

## Cheatsheet de gestión de paquetes

- **Comandos pip**:
  - `pip install paquete`: instalar
  - `pip install paquete==version`: versión específica
  - `pip install -r requirements.txt`: desde archivo
  - `pip list`: listar instalados
  - `pip show paquete`: información detallada
  - `pip freeze > requirements.txt`: generar archivo
  - `pip uninstall paquete`: desinstalar
  - `pip install --upgrade paquete`: actualizar
- **Archivos de configuración**:
  - `requirements.txt`: dependencias simples
  - `setup.py`: configuración completa
  - `pyproject.toml`: formato moderno (PEP 517)
- **Entornos virtuales**:
  - `python -m venv mi_entorno`: crear
  - `source mi_entorno/bin/activate`: activar (Linux/Mac)
  - `mi_entorno\Scripts\activate`: activar (Windows)
  - `deactivate`: desactivar
- **Buenas prácticas**:
  - Usar entornos virtuales para cada proyecto
  - Congelar versiones en producción
  - Documentar dependencias
  - Usar pip-tools o poetry para gestión avanzada

## Errores frecuentes

- Instalar paquetes globalmente sin entorno virtual.
- No especificar versiones exactas en producción.
- Confundir pip con pip3 (problemas de versión).
- No actualizar pip antes de instalar paquetes.
- Ignorar conflictos de versiones entre paquetes.
- No leer documentación de paquetes antes de usar.

## Prueba/ejecución (opcional)

- Ejecuta `Intermediate/08_python_package_manager.py` para ver las demos.
- Crea un entorno virtual y practica la instalación.
- Explora PyPI buscando paquetes interesantes.
- Intenta crear tu primer paquete.

## Material de apoyo

- Código de referencia: `Intermediate/08_python_package_manager.py`
- PyPI: <https://pypi.org/>
- Documentación: <https://packaging.python.org/>
- Herramientas modernas: Poetry, Pipenv, Hatch
- Tutorial: "Packaging Python Projects" en docs.python.org

## Qué te llevas hoy

- Dominas la gestión profesional de dependencias.
- Puedes crear proyectos reproducibles y compartibles.
- Sabes instalar y usar paquetes populares de la comunidad.
- Preparas el terreno para proyectos de producción real.

## Siguiente paso

- ¡Felicidades! Has completado el nivel intermedio. Ahora estás listo para explorar el backend con FastAPI y bases de datos.

---

**⬅️ [Anterior: Clase 07 - Expresiones Regulares](CLASE_07_REGEX.md) | [🏠 Volver al Índice](../HelloPython.md) | ⚡ [Siguiente: Nivel Backend](../Backend/)**
