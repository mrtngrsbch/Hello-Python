#!/usr/bin/env python3
"""Script para verificar la configuración de Python."""

import sys
import platform
import subprocess
from pathlib import Path

def check_python():
    """Verifica la instalación de Python."""
    print("🐍 Información de Python")
    print("=" * 50)
    print(f"Versión: {sys.version}")
    print(f"Ejecutable: {sys.executable}")
    print(f"Plataforma: {platform.platform()}")
    print(f"Arquitectura: {platform.machine()}")
    
def check_packages():
    """Lista los paquetes principales instalados."""
    print("\n📦 Paquetes principales instalados")
    print("=" * 50)
    
    packages = ["numpy", "pandas", "requests", "ipython", "black", "pylint"]
    for package in packages:
        try:
            __import__(package)
            version = subprocess.check_output(
                [sys.executable, "-m", "pip", "show", package],
                text=True
            )
            for line in version.split('\n'):
                if line.startswith('Version:'):
                    print(f"✅ {package:15} {line.split()[1]}")
                    break
        except ImportError:
            print(f"❌ {package:15} No instalado")
            
def check_pyenv():
    """Verifica las versiones de Python disponibles en pyenv."""
    print("\n🔧 Versiones de Python en pyenv")
    print("=" * 50)
    try:
        result = subprocess.run(
            ["pyenv", "versions"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("pyenv no encontrado")

if __name__ == "__main__":
    check_python()
    check_packages()
    check_pyenv()
    print("\n✨ Verificación completada!")
