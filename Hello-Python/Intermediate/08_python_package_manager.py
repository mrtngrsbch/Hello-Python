"""
Clase 08 — Python Package Manager (gestor de paquetes)

Propósito pedagógico:
- Aprender a gestionar paquetes externos con pip.
- Practicar la importación y uso de paquetes populares.

Cómo ejecutar:
- python3 Hello-Python/Intermediate/08_python_package_manager.py

NOTA: Antes de ejecutar, instala las dependencias necesarias:
- pip install pandas requests numpy
"""

from __future__ import annotations
try:
    import pandas as pd
    import requests
    import numpy as np
    print("✅ Todas las dependencias están instaladas correctamente")
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("💡 Instala las dependencias faltantes con:")
    print("   pip install pandas requests numpy")
    print("\n⚠️  Continuando con ejemplos alternativos sin estas librerías...")
    
    # Módulos alternativos nativos de Python
    import json
    import urllib.request
    import math

from mypackage import arithmetics


def demo_package_manager() -> None:
    print("\n=== EJEMPLOS DE USO DE PAQUETES ===")

    try:
        print("\n1. Ejemplo con pandas:")
        df = pd.DataFrame({
            'nombre': ['Ana', 'Luis', 'María'],
            'edad': [25, 30, 28],
            'ciudad': ['Madrid', 'Barcelona', 'Valencia']
        })
        print(df)
    except NameError:
        print("   (pandas no disponible - usando ejemplo alternativo)")
        usuarios = [
            {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'},
            {'nombre': 'Luis', 'edad': 30, 'ciudad': 'Barcelona'},
            {'nombre': 'María', 'edad': 28, 'ciudad': 'Valencia'}
        ]
        for usuario in usuarios:
            print(f"   {usuario['nombre']} - {usuario['edad']} años - {usuario['ciudad']}")

    try:
        print("\n2. Ejemplo con requests:")
        response = requests.get('https://api.github.com', timeout=5)
        print(f"Estado de la API de GitHub: {response.status_code}")
    except NameError:
        print("   (requests no disponible - usando urllib)")
        try:
            with urllib.request.urlopen('https://api.github.com', timeout=5) as response:
                print(f"Estado de la API de GitHub: {response.getcode()}")
        except Exception as e:
            print(f"   Error al conectar: {e}")

    try:
        print("\n3. Ejemplo con numpy:")
        arr = np.array([1, 2, 3, 4, 5])
        print(f"Array: {arr}")
        print(f"Media: {np.mean(arr)}")
    except NameError:
        print("   (numpy no disponible - usando math)")
        numeros = [1, 2, 3, 4, 5]
        media = sum(numeros) / len(numeros)
        print(f"Lista: {numeros}")
        print(f"Media: {media}")

    print("\n4. Ejemplo con módulo personalizado:")
    print(f"Suma de 1 + 4 = {arithmetics.sum_two_values(1, 4)}")


if __name__ == "__main__":
    demo_package_manager()
