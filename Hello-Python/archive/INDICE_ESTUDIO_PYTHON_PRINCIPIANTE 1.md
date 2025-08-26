# Índice de estudio de Python para principiantes (v1)

Propósito
- Construir fundamentos sólidos y hábitos profesionales desde el inicio: estilo (PEP 8), documentación (PEP 257), pruebas (pytest), tipado (typing), empaquetado (pyproject/Poetry) y buenas prácticas.
- Progresión por unidades con ejercicios, mini-proyectos y un capstone por etapa.

Ruta de aprendizaje
- Unidad 0 — Entorno y mentalidad
  - Python 3.13.x, venv/pyenv, Poetry, pre-commit, black/ruff, mypy/pyright, pytest + coverage.
  - Filosofía Python: legibilidad, EAFP vs LBYL, "pythonic".
- Unidad 1 — Fundamentos con propósito
  - Tipos, colecciones, control de flujo, funciones, módulos/paquetes, I/O, errores básicos.
  - Buenas prácticas desde el día 1: nombres, PEP 8/257, estructura de proyecto.
  - Laboratorio: 3 automatizaciones pequeñas (renombrado de archivos; CSV→JSON→Excel; un CLI simple con logging).
- Unidad 2 — Pensar en Python
  - Iterables/iteradores, generadores, comprehensions, unpacking, slicing, data model y dunder methods.
  - Tipado moderno (typing) y dataclasses. Pattern matching (match/case).
  - Laboratorio: parsers y validación de datos con tipado.
- Unidad 3 — Biblioteca estándar productiva
  - itertools, functools (lru_cache/cache/partial), collections, contextlib, pathlib, datetime/zoneinfo, statistics, decimal.
  - logging, argparse, subprocess seguro; introducción a concurrencia (concurrent.futures/asyncio) y perfilado básico.
  - Laboratorio: pipeline IO‑bound concurrente con reporte de rendimiento.
- Unidad 4 — Calidad, pruebas y diseño
  - pytest (fixtures, parametrización, markers), coverage, hypothesis (property‑based testing), refactor guiado por tests.
  - Laboratorio: refactor seguro de un módulo propenso a errores.
- Unidad 5 — APIs modernas y datos
  - FastAPI, Pydantic v2, SQLModel/SQLAlchemy 2.x, OpenAPI.
  - httpx (sync/async), timeouts, retires, pruebas end‑to‑end.
  - Laboratorio: microservicio CRUD con validación, auth básica y tests.
- Unidad 6 — Empaquetado y distribución
  - pyproject.toml, Poetry, entry points (CLI), wheels, publicar paquete.
  - Documentación (docstrings de calidad, Sphinx/MkDocs) y CI local con pre‑commit.
- Unidad 7 — Rendimiento y robustez
  - Perfilado (CPU/IO), caching selectivo, memoria (tracemalloc, __slots__), resiliencia (reintentos, timeouts), logging estructurado.

Recursos recomendados (esenciales y prácticos)
- Principiante
  - Automate the Boring Stuff with Python (Sweigart)
  - Python Crash Course (Matthes)
  - Tutorial oficial de Python (referencia exacta)
- Intermedio
  - Effective Python (Slatkin)
  - The Hitchhiker’s Guide to Python (ecosistema y buenas prácticas)
- Avanzado
  - Fluent Python (Ramalho)
  - Python Cookbook (Beazley & Jones)
  - TDD with Python (Percival) y High Performance Python (Gorelick & Ozsvald)

Proyectos integradores (capstones)
- Capstone 1: CLI “Inbox Zero” (HTTP + SQLite con SQLModel, empaquetado como comando instalable).
- Capstone 2: Microservicio de catálogo (FastAPI + Pydantic v2 + SQLModel, paginación y caching selectivo, tests E2E).
- Capstone 3: Orquestador de descargas (httpx async, límites, reintentos exponenciales, colas, logging estructurado, perfilado).

Formato de cada lección
- Objetivos de aprendizaje operativos (lo que podrás hacer).
- 3 bloques de ejemplos: básico → idiomático → producción/robusto.
- Ejercicios “micro‑kata” con solución comentada.
- Caja de herramientas: atajos, trampas frecuentes y anti‑patrones.
- Checklist de producción: logging, errores, tipado, tests, estilo, docs.
- Mini‑quiz y tarjetas de repaso; snippets probados automáticamente con pytest.

Sugerencia de tiempos (orientativo)
- Unidades 0–1: 2–3 semanas
- Unidades 2–3: 2–3 semanas
- Unidad 4: 1–2 semanas
- Unidades 5–6: 2–3 semanas
- Unidad 7 y capstones: 2–3 semanas

Próximos pasos
- Crear la primera lección de la Unidad que elijas con: objetivos, ejemplos, ejercicios, tests (pytest) y guía de corrección.
- Integrar tests automáticos por carpeta para feedback inmediato.
- Programar capstone y rúbrica de evaluación.