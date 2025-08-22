# Clase 02 — Challenges (Integración de conceptos)

## Apertura narrativa
Los challenges son tu campo de entrenamiento real. Aquí combinas todo lo aprendido en contextos prácticos: desde analizar logs hasta procesar datos de usuarios. Cada challenge es una mini-aplicación que resuelve un problema del mundo real.

## Por qué te importa
- Aplicas múltiples conceptos en escenarios reales.
- Desarrollas pensamiento algorítmico y resolución de problemas.
- Preparas tu portfolio con proyectos pequeños pero significativos.
- Aprendes a dividir problemas grandes en partes manejables.

## Demostración guiada
```python
# Challenge 1: Analizador de logs
from datetime import datetime

def analizar_logs(logs):
    """Analiza logs de acceso web"""
    errores = [log for log in logs if 'ERROR' in log]
    fechas = [datetime.strptime(log.split()[0], '%Y-%m-%d') 
              for log in logs if 'ERROR' in log]
    return len(errores), fechas

# Challenge 2: Procesador de CSV
import csv
from typing import List, Dict

def procesar_emails(archivo: str) -> List[Dict[str, str]]:
    """Procesa archivo CSV de usuarios"""
    usuarios = []
    with open(archivo, 'r') as f:
        reader = csv.DictReader(f)
        usuarios = [row for row in reader if '@' in row.get('email', '')]
    return usuarios

# Challenge 3: Validador de contraseñas
import re

def validar_contraseña(password: str) -> bool:
    """Valida contraseña segura"""
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password))

# Challenge 4: Generador de reportes
def generar_reporte(ventas: List[float]) -> Dict[str, float]:
    """Genera reporte de ventas"""
    return {
        'total': sum(ventas),
        'promedio': sum(ventas) / len(ventas) if ventas else 0,
        'máximo': max(ventas) if ventas else 0,
        'mínimo': min(ventas) if ventas else 0
    }

# Uso integrado
if __name__ == "__main__":
    # Simular logs
    logs = [
        "2024-01-15 INFO Usuario login",
        "2024-01-15 ERROR Database timeout",
        "2024-01-16 INFO Usuario logout",
        "2024-01-16 ERROR Invalid credentials"
    ]
    
    errores, fechas = analizar_logs(logs)
    print(f"Total errores: {errores}")
    print(f"Fechas con errores: {fechas}")
    
    # Probar validador
    print("Contraseña válida:", validar_contraseña("Python123"))
    
    # Reporte de ventas
    ventas = [100, 200, 150, 300, 250]
    reporte = generar_reporte(ventas)
    print("Reporte de ventas:", reporte)
```

## Micro-kata (15-20 min)
- **Challenge 1**: Crea un analizador de texto que cuente palabras únicas y sus frecuencias.
- **Challenge 2**: Implementa un sistema de notas que calcule promedios, máximos y mínimos.
- **Challenge 3**: Desarrolla un validador de emails que verifique formato y dominio permitido.
- **Challenge 4**: Crea un generador de contraseñas seguras con longitud variable.
- **Challenge 5**: Implementa un mini-sistema de logs con niveles (INFO, WARNING, ERROR).

## Cheatsheet de challenges
- **Patrones comunes**:
  - Análisis de datos: list comprehension + funciones auxiliares
  - Validación: regex + condicionales
  - Procesamiento de archivos: with open + csv/json
  - Reportes: diccionarios con estadísticas
- **Estructuras útiles**:
  - `collections.Counter` para contar elementos
  - `defaultdict` para acumular datos
  - `namedtuple` para datos estructurados
- **Testing**: siempre prueba con datos de ejemplo
- **Documentación**: docstrings claros para cada función

## Errores frecuentes
- No manejar casos edge (listas vacías, división por cero).
- Acoplar demasiado la lógica (una función que hace todo).
- No validar entradas (asumir que los datos son correctos).
- Olvidar cerrar archivos (usar siempre `with open`).
- Documentar mal las funciones (sin docstrings claros).

## Prueba/ejecución (opcional)
- Ejecuta `Intermediate/02_challenges.py` para ver las demos.
- Crea tus propios tests con datos reales.
- Desafío: añade más casos de prueba a cada challenge.

## Material de apoyo
- Código de referencia: `Intermediate/02_challenges.py`
- Módulos útiles: `collections`, `itertools`, `functools`
- Recursos: Real Python challenges, LeetCode fácil

## Qué te llevas hoy
- Resuelves problemas reales combinando múltiples conceptos.
- Tienes mini-proyectos para tu portfolio.
- Sabes estructurar soluciones modulares y reutilizables.

## Siguiente paso
- Clase 03: Lambdas para crear funciones pequeñas y anónimas.