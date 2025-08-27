<!-- NAVEGACIÓN -->
**📍 [Inicio](../HelloPython.md) > [Intermedio](.) > Clase 00**

# Clase 00 — Manejo de Fechas y Tiempo

## Apertura narrativa

Las fechas y el tiempo son el latido de cualquier sistema real: logs, auditorías, reservas, vencimientos. Dominar `datetime` te permite trabajar con momentos concretos, calcular duraciones y formatear salidas legibles para humanos y máquinas.

## Por qué te importa

- Registra eventos con precisión de segundos.
- Calcula diferencias entre fechas (edad, duración de tareas).
- Formatea fechas para APIs, reportes y usuarios internacionales.
- Maneja zonas horarias y ajustes de horario de verano.

## Demostración guiada

```python
from datetime import datetime, timedelta

# Fecha y hora actual
now = datetime.now()
print("Ahora:", now)

# Crear fecha específica
nacimiento = datetime(1990, 5, 15, 14, 30)
print("Nacimiento:", nacimiento)

# Calcular edad
edad = now - nacimiento
print("Días vividos:", edad.days)
print("Años aproximados:", edad.days // 365)

# Formatear fechas
formato_español = now.strftime("%d/%m/%Y %H:%M")
formato_iso = now.isoformat()
print("Formato español:", formato_español)
print("Formato ISO:", formato_iso)

# Parsear desde string
fecha_str = "2024-12-25"
navidad = datetime.strptime(fecha_str, "%Y-%m-%d")
print("Navidad:", navidad)

# Operaciones con fechas
mañana = now + timedelta(days=1)
print("Mañana:", mañana)

# Trabajar con componentes
print("Año:", now.year)
print("Mes:", now.month)
print("Día de la semana:", now.strftime("%A"))
```

## Micro-kata (10-12 min)

- Crea una función que calcule cuántos días faltan para tu próximo cumpleaños.
- Dado dos fechas de reserva (check-in y check-out), calcula la duración en noches.
- Formatea la fecha actual en tres formatos diferentes: español, inglés americano, y ISO completo.

## Cheatsheet de datetime

- Importar: `from datetime import datetime, timedelta, date, time`
- Actual: `datetime.now()`, `datetime.today()`
- Crear: `datetime(año, mes, día, hora=0, minuto=0)`
- Componentes: `.year`, `.month`, `.day`, `.hour`, `.minute`, `.second`
- Formatear: `.strftime(formato)` → string
- Parsear: `datetime.strptime(string, formato)` → datetime
- Diferencias: `fecha2 - fecha1` → timedelta
- Sumar/restar: `fecha + timedelta(days=n)`
- Timedelta: `days`, `seconds`, `total_seconds()`
- Formatos comunes:
  - `%d/%m/%Y` → 25/12/2024
  - `%m/%d/%Y` → 12/25/2024
  - `%Y-%m-%d` → 2024-12-25
  - `%A` → nombre completo del día

## Errores frecuentes

- `ValueError` al parsear fechas mal formateadas.
- Confundir `datetime.now()` con `date.today()` (uno incluye tiempo, otro no).
- Olvidar que los meses van de 1-12, no de 0-11.
- No considerar que `timedelta` maneja días enteros, no fracciones.

## Prueba/ejecución (opcional)

- Ejecuta `Intermediate/00_dates.py` para ver las demos.
- Practica en el REPL creando y manipulando fechas reales.

## Material de apoyo

- Código de referencia: `Intermediate/00_dates.py`
- Documentación oficial: `datetime` en docs.python.org

## Qué te llevas hoy

- Dominas la creación, manipulación y formateo de fechas.
- Puedes calcular duraciones y trabajar con fechas reales en proyectos.

## Siguiente paso

- Clase 01: List Comprehension para transformar colecciones con elegancia y eficiencia.

---

**⏭️ [Siguiente: Clase 01 - List Comprehension](CLASE_01_LIST_COMPREHENSION.md) | [🏠 Volver al Índice](../HelloPython.md)**
