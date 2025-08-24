<!-- NAVEGACIÓN -->
**📍 [Inicio](../HelloPython.md) > [Intermedio](.) > Clase 05**

# Clase 05 — Error Types (Manejo elegante de excepciones)

## Apertura narrativa
Los errores no son enemigos, son mensajeros que te indican qué salió mal. Dominar los tipos de errores es como aprender los diferentes tipos de señales de tráfico: cada uno tiene un significado específico y una respuesta apropiada.

## Por qué te importa
- Manejas errores de forma específica y elegante.
- Evitas el catch-all genérico que oculta problemas reales.
- Creas aplicaciones robustas que fallan con gracia.
- Mejoras la experiencia de usuario con mensajes claros.

## Demostración guiada
```python
from typing import Union, List
import json

def dividir_seguro(a: float, b: float) -> Union[float, str]:
    """Divide dos números con manejo específico de errores"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero"
    except TypeError:
        return "Error: Los parámetros deben ser números"
    except Exception as e:
        return f"Error inesperado: {e}"

def leer_archivo_json(ruta: str) -> Union[dict, str]:
    """Lee archivo JSON con manejo de errores específicos"""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return f"Error: El archivo '{ruta}' no existe"
    except json.JSONDecodeError:
        return "Error: El archivo no contiene JSON válido"
    except PermissionError:
        return "Error: Sin permisos para leer el archivo"
    except Exception as e:
        return f"Error al procesar archivo: {e}"

def procesar_lista_numeros(numeros: List[str]) -> List[float]:
    """Procesa lista de strings a números con manejo de errores"""
    resultados = []
    for num_str in numeros:
        try:
            numero = float(num_str)
            resultados.append(numero)
        except ValueError:
            print(f"Advertencia: '{num_str}' no es un número válido, ignorando")
            continue
        except Exception as e:
            print(f"Error procesando '{num_str}': {e}")
            continue
    return resultados

def validar_email(email: str) -> Union[str, None]:
    """Valida formato de email con manejo específico"""
    import re
    
    try:
        if not email:
            raise ValueError("El email no puede estar vacío")
        
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Formato de email inválido")
        
        return email
    except ValueError as e:
        return f"Error de validación: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Uso de else y finally
def operacion_segura(x: int, y: int) -> dict:
    """Operación segura con else y finally"""
    resultado = {}
    try:
        resultado['suma'] = x + y
        resultado['division'] = x / y
    except ZeroDivisionError as e:
        resultado['error'] = str(e)
    except TypeError as e:
        resultado['error'] = "Tipo de dato incorrecto"
    else:
        resultado['status'] = "éxito"
    finally:
        resultado['timestamp'] = str(__import__('datetime').datetime.now())
    
    return resultado

# Demostración de diferentes tipos de errores
if __name__ == "__main__":
    # ZeroDivisionError
    print("División:", dividir_seguro(10, 0))
    
    # ValueError
    print("Procesando números:", procesar_lista_numeros(["1", "2", "abc", "4.5"]))
    
    # FileNotFoundError
    print("JSON:", leer_archivo_json("archivo_inexistente.json"))
    
    # ValueError en email
    print("Email válido:", validar_email("test@example.com"))
    print("Email inválido:", validar_email("invalid-email"))
    
    # Uso de else/finally
    print("Operación segura:", operacion_segura(10, 2))
```

## Micro-kata (12-15 min)
- **Ejercicio 1**: Crea una función que maneje diferentes tipos de errores al leer un CSV.
- **Ejercicio 2**: Implementa un validador de números de tarjeta con manejo específico de errores.
- **Ejercicio 3**: Crea un parser de URLs que maneje errores de formato y protocolo.
- **Ejercicio 4**: Desarrolla un sistema de logs que capture diferentes tipos de excepciones.
- **Ejercicio 5**: Implementa un conversor de unidades con validación y manejo de errores.

## Cheatsheet de tipos de errores
- **Errores comunes**:
  - `ValueError`: valor incorrecto (int("abc"))
  - `TypeError`: tipo incorrecto ("texto" + 5)
  - `ZeroDivisionError`: división por cero
  - `FileNotFoundError`: archivo no existe
  - `PermissionError`: sin permisos
  - `JSONDecodeError`: JSON mal formado
  - `KeyError`: clave no existe en dict
  - `IndexError**: índice fuera de rango
- **Estructura de manejo**:
  ```python
  try:
      # código
  except ErrorEspecífico as e:
      # manejo específico
  except Exception as e:
      # manejo genérico
  else:
      # se ejecuta si no hay error
  finally:
      # siempre se ejecuta
  ```
- **Buenas prácticas**:
  - Ser específico con los tipos de errores
  - Proporcionar mensajes útiles
  - Loggear errores para debugging
  - No ocultar errores con catch-all

## Errores frecuentes
- Usar `except Exception` para todo (oculta errores específicos).
- No proporcionar mensajes de error claros.
- Abusar de try-except para control de flujo normal.
- No limpiar recursos en finally (archivos, conexiones).
- Swallowing exceptions sin loggear.

## Prueba/ejecución (opcional)
- Ejecuta `Intermediate/05_error_types.py` para ver las demos.
- Prueba cada tipo de error con diferentes escenarios.
- Crea tests unitarios para tus funciones con manejo de errores.

## Material de apoyo
- Código de referencia: `Intermediate/05_error_types.py`
- Documentación: Python Exception Hierarchy
- Herramientas: `logging` para logs estructurados
- Testing: `pytest.raises()` para testear excepciones

## Qué te llevas hoy
- Manejas errores de forma específica y elegante.
- Creas aplicaciones robustas que fallan con gracia.
- Sabes cuándo y cómo capturar cada tipo de error.

## Siguiente paso
- Clase 06: File Handling para trabajar con archivos de forma segura y eficiente.

---

**⬅️ [Anterior: Clase 04 - Funciones de Orden Superior](CLASE_04_HIGHER_ORDER.md) | ⏭️ [Siguiente: Clase 06 - Manejo de Archivos](CLASE_06_FILE_HANDLING.md) | [🏠 Volver al Índice](../HelloPython.md)**