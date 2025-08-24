<!-- NAVEGACIÓN -->
**📍 [Inicio](../../HelloPython.md) > [Fundamentos](.) > Clase 00**

# Clase 00 — Instalación y Configuración (macOS)

## Objetivos

- Usar el entorno virtual existente en la raíz del proyecto (.venv)
- Verificar instalación ejecutando un test de humo
- Dejar listo el entorno para las siguientes clases

## Prerrequisitos

- macOS con Python 3.11+ instalado
- VS Code (o tu editor preferido)

## Pasos (macOS)

1) Activar el entorno virtual del proyecto (ya existe en la raíz):
      - `cd /Users/mrtn/Documents/GitHub/_LearnPyhton`
      - `source .venv/bin/activate`
2) (Opcional) Actualizar pip: `python -m pip install --upgrade pip`
3) Ejecutar los tests de humo del proyecto:
      - `cd Hello-Python`
      - `python -m unittest discover -s tests -p "test_*.py" -v`
4) (Opcional) Desactivar el entorno cuando termines: `deactivate`

## Resultados esperados

- Debes ver pasar los tests de hello_module sin errores (OK en verde).

## Checklist

- [ ] .venv activado (el prompt muestra el nombre del entorno)
- [ ] `python --version` muestra 3.11+
- [ ] Tests pasan en verde

## Problemas comunes y solución (macOS)

- Si `python` apunta a 2.x, usa `python3` o ajusta alias en tu shell.
- Si no puedes activar el entorno, verifica que `.venv/bin/activate` existe.

---

**⏭️ [Siguiente: Clase 01 - Variables](CLASE_01.md) | [🏠 Volver al Índice](../../HelloPython.md)**