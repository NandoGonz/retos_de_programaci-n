# Documentación: `capturador__errores.py`

Este documento explica, de forma clara y línea por línea, el funcionamiento de
`capturador__errores.py` (una implementación de Tres en Raya en consola). Se
incluye el código original seguido de una explicación detallada por sección y
por línea.

---

## Código fuente

```python
# ── Clase de excepción ───────────────────────────────────────────────────────
class JuegoTerminacion(Exception):
    """Excepción para indicar que el juego debe terminar."""

    pass


# ── Función para imprimir el tablero ─────────────────────────────────────────
def imprimir_tablero(tablero):  # TODO: corrige la firma de la función si falta algo
    """Imprime el tablero de 3×3."""
    # TODO: recorre las 9 celdas e imprime cada fila con ' | ' y separadores '---------'
    for i in range(3):
        fila = tablero[3 * i : 3 * i + 3]
        print(" | ".join(fila))
        if i < 2:
            print("---------")
    print()


# ── Comprobar victoria y empate ──────────────────────────────────────────────
def comprobar_victoria(tablero, jugador):
    """Devuelve True si el jugador ha conseguido tres en raya."""
    combos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # filas
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # columnas
        (0, 4, 8),
        (2, 4, 6),  # diagonales
    ]
    # FIXME: revisa la expresión lógica; debe detectar correctamente cualquiera de los combos
    return any(all(tablero[i] == jugador for i in combo) for combo in combos)


def tablero_lleno(tablero):
    """True si no quedan espacios vacíos."""
    # TODO: completa la función para que devuelva True cuando no haya ' ' en tablero
    return " " not in tablero


# ── Pedir movimiento al jugador ─────────────────────────────────────────────
def pedir_movimiento(tablero, jugador):
    """
    Pide al jugador una posición del 1 al 9 y valida la elección.
    Controla ValueError y KeyboardInterrupt.
    """
    while True:
        try:
            entrada = input(f"Jugador {jugador}, elija casilla (1-9) o 'salir': ")
            # TODO: si escribe 'salir' o 'exit', lanza JuegoTerminacion
            if entrada.lower() in ["salir", "exit"]:
                raise JuegoTerminacion("Juego terminado por petición del usuario.")
            pos = int(entrada) - 1
            # TODO: valida que pos esté en 0–8 y que tablero[pos] == ' '
            if not (0 <= pos <= 8 and tablero[pos] == " "):
                print("Movimiento inválido. La casilla está ocupada o fuera de rango.")
                continue
            # TODO: si todo es válido, devuelve pos
            return pos
        except ValueError:
            print("Entrada inválida. Ingrese un número del 1 al 9 o 'salir'.")
        except KeyboardInterrupt:
            # TODO: maneja Ctrl+C lanzando JuegoTerminacion
            raise JuegoTerminacion("Juego terminado por interrupción del usuario.")


# ── Lógica de una partida ───────────────────────────────────────────────────
def partida():
    tablero = [" "] * 9
    turno = "X"
    # TODO: imprime el tablero inicial usando imprimir_tablero(tablero)
    imprimir_tablero(tablero)
    try:
        while True:
            # TODO: pide movimiento y actualiza tablero
            pos = pedir_movimiento(tablero, turno)
            tablero[pos] = turno
            # TODO: imprime tablero
            imprimir_tablero(tablero)
            # TODO: comprueba victoria (comprobar_victoria) y empate (tablero_lleno)
            if comprobar_victoria(tablero, turno):
                print(f"¡Jugador {turno} ha ganado!")
                break
            if tablero_lleno(tablero):
                print("¡Empate!")
                break
            # TODO: cambia turno entre 'X' y 'O'
            turno = "O" if turno == "X" else "X"
    except JuegoTerminacion as e:
        # TODO: mensaje de partida cancelada
        print(e)
        raise  # Re-lanza la excepción para que main la capture y termine el programa.


# ── Función principal ───────────────────────────────────────────────────────
def main():
    # TODO: mensaje de bienvenida indicando que se puede escribir 'salir'
    print(
        "¡Bienvenido a Tres en Raya! Escriba 'salir' en cualquier momento para terminar."
    )
    try:
        while True:
            partida()
            # TODO: pregunta "¿Jugar otra partida? (s/n)" y controla la respuesta
            respuesta = input("¿Jugar otra partida? (s/n): ").lower()
            if respuesta != "s":
                raise JuegoTerminacion("Juego terminado por petición del usuario.")
    except JuegoTerminacion as e:
        # TODO: mensaje de finalización por petición del usuario
        print(e)
    except Exception as e:
        # TODO: imprime un mensaje de error inesperado usando e
        print(f"¡Error inesperado!: {e}")
    finally:
        # TODO: mensaje final de cierre, p.ej. "Programa terminado."
        print("Programa terminado.")


if __name__ == "__main__":
    main()
```

---

## Explicación línea a línea

A continuación explico cada bloque y las líneas más relevantes. Para evitar una
lista excesivamente larga, agrupo líneas estrechamente relacionadas (por
bloques funcionales) y explico exactamente qué hace cada una.

### 1) Encabezado y excepción personalizada

- Línea: `class JuegoTerminacion(Exception):`
  - Crea una excepción personalizada llamada `JuegoTerminacion` que hereda de
    `Exception`. Se usa para indicar terminaciones controladas del juego
    (por ejemplo, cuando el usuario pide salir o presiona Ctrl+C).
- Línea: `"""Excepción para indicar que el juego debe terminar."""`
  - Docstring de la excepción que describe su propósito.
- Línea: `pass`
  - No añade comportamiento adicional; la clase se comporta como una excepción
    estándar pero con un nombre propio (útil para capturarla específicamente).


### 2) `imprimir_tablero(tablero)` — mostrar el tablero

- Firma: `def imprimir_tablero(tablero):`
  - Define una función que recibe `tablero`, una lista de 9 elementos.
- `for i in range(3):`
  - Recorre las 3 filas del tablero: índices 0,1,2.
- `fila = tablero[3 * i : 3 * i + 3]`
  - Extrae tres elementos consecutivos para la fila actual (slicing):
    fila 0 -> índices 0..2, fila 1 -> 3..5, fila 2 -> 6..8.
- `print(" | ".join(fila))`
  - Presenta la fila uniendo las tres casillas con " | ". Si una casilla es
    `' '` (vacía), se verá como un espacio.
- `if i < 2: print("---------")`
  - Imprime una línea separadora tras las filas 0 y 1 para dar formato.
- `print()`
  - Añade una línea en blanco al final para facilitar la lectura.


### 3) `comprobar_victoria(tablero, jugador)` — detectar ganador

- `combos = [...]`
  - Lista de tuplas con las combinaciones de índices que representan las
    posiciones ganadoras (3 filas, 3 columnas, 2 diagonales).
- `return any(all(tablero[i] == jugador for i in combo) for combo in combos)`
  - Para cada `combo` (p. ej. (0,1,2)) verifica si todas las posiciones de esa
    tupla contienen el símbolo del `jugador`. Si alguna combinación cumple la
    condición, `any(...)` devolverá True.


### 4) `tablero_lleno(tablero)` — empate

- `return " " not in tablero`
  - Devuelve True cuando no hay espacios vacíos en la lista `tablero`, es decir
    si ya se han llenado las 9 casillas.


### 5) `pedir_movimiento(tablero, jugador)` — entrada y validación

Bucle principal de entrada que valida la jugada del usuario:

- `entrada = input(...)`
  - Solicita al usuario una casilla (1-9) o la palabra 'salir'.
- `if entrada.lower() in ["salir", "exit"]: raise JuegoTerminacion(...)`
  - Si el usuario escribe 'salir' o 'exit', se lanza `JuegoTerminacion` para
    terminar la partida de forma controlada.
- `pos = int(entrada) - 1`
  - Convierte la entrada a entero y lo transforma a índice 0-based.
- `if not (0 <= pos <= 8 and tablero[pos] == " "):`
  - Valida que la posición esté en rango y que la casilla esté vacía; si no,
    muestra un mensaje y repite la petición.
- `return pos`
  - Devuelve el índice válido para usar en la actualización del tablero.
- `except ValueError:`
  - Captura entradas que no se convierten a entero y muestra un aviso.
- `except KeyboardInterrupt:`
  - Si el usuario presiona Ctrl+C, se lanza `JuegoTerminacion` para terminar
    limpiamente.


### 6) `partida()` — flujo de una partida

- `tablero = [" "] * 9`
  - Crea un tablero vacío con 9 espacios.
- `turno = "X"`
  - Inicializa el turno del jugador 'X'.
- `imprimir_tablero(tablero)`
  - Muestra el tablero vacío al iniciar partida.
- Bucle `while True:`
  - Repite turnos hasta que haya victoria, empate o terminación solicitada.
- `pos = pedir_movimiento(tablero, turno)` y `tablero[pos] = turno`
  - Solicita la jugada y la aplica al tablero.
- `imprimir_tablero(tablero)`
  - Muestra el tablero actualizado.
- `if comprobar_victoria(...): print(...); break`
  - Si la jugada produce victoria, notifica y finaliza la partida.
- `if tablero_lleno(tablero): print("¡Empate!"); break`
  - Si el tablero está lleno y no hay ganador, declara empate.
- `turno = "O" if turno == "X" else "X"`
  - Alterna el turno entre 'X' y 'O'.
- `except JuegoTerminacion as e:`
  - Si se lanza la excepción de terminación (por ejemplo, 'salir' o Ctrl+C),
    muestra el motivo y re-lanza para que `main()` gestione el cierre global.


### 7) `main()` — bucle principal y control de partidas repetidas

- Mensaje de bienvenida indicando que es posible escribir 'salir'.
- Bucle `while True:` que ejecuta `partida()` y luego pregunta si se desea jugar otra
  partida con `input("¿Jugar otra partida? (s/n): ")`.
- Si la respuesta no es 's', lanza `JuegoTerminacion` para indicar cierre por
  petición del usuario.
- Captura `JuegoTerminacion` y muestra el mensaje asociado.
- Captura `Exception` genérica e imprime el error inesperado para ayuda al
  diagnóstico.
- En el bloque `finally` se imprime "Programa terminado." para indicar que el
  programa finalizó y realizar limpieza si fuese necesario.


## Observaciones y mejoras sugeridas

- Se recomienda añadir docstrings y tipos (type hints) a todas las funciones
  para mejorar la comprensión y facilitar el análisis estático.
- En `imprimir_tablero` sería conveniente convertir células vacías a un
  carácter visible (por ejemplo '.' o ' ') si se desea una presentación más
  clara.
- La función `pedir_movimiento` podría desglosarse en validadores auxiliares
  (p. ej. `validar_posicion`) para facilitar pruebas unitarias.
- Actualmente el archivo contiene varios `TODO` y `FIXME`. Si desea, puedo:
  - 1) eliminar los `TODO` y aplicar las mejoras directamente en el código, o
  - 2) crear una versión alternativa `capturador__errores_annotated.py` con
       comentarios más extensos y tipos.

---

¿Deseas que aplique las mejoras (añadir docstrings y type hints al archivo,
limpiar los TODO y crear una versión anotada del código)? Puedo hacerlo ahora
mismo y ejecutar una comprobación de sintaxis.
