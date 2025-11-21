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
