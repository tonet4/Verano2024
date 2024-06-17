import random

tablero = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

def imprimir_tablero():
    print(f"| {tablero[1]} | {tablero[2]} | {tablero[3]} |")
    print(f"| {tablero[4]} | {tablero[5]} | {tablero[6]} |")
    print(f"| {tablero[7]} | {tablero[8]} | {tablero[9]} |")

def verificar_victoria(simbolo):
    combinaciones_ganadoras = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Filas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columnas
        [1, 5, 9], [3, 5, 7]              # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[pos] == simbolo for pos in combinacion):
            return True
    return False

def juego_terminado():
    return all(tablero[pos] != " " for pos in tablero)

while True:
    imprimir_tablero()

    # Turno del usuario
    while True:
        usuario = int(input("Dime posición, tiene que ser un número entre 1 y 9: "))
        if 1 <= usuario <= 9 and tablero[usuario] == " ":
            tablero[usuario] = "X"
            break
        else:
            print(f"La casilla {usuario} ya está ocupada o es inválida")

    if verificar_victoria("X"):
        imprimir_tablero()
        print("¡Has ganado!")
        break

    if juego_terminado():
        imprimir_tablero()
        print("¡Es un empate!")
        break

    # Turno de la máquina
    while True:
        maquina = random.randint(1, 9)
        if tablero[maquina] == " ":
            tablero[maquina] = "O"
            print(f"La máquina eligió la posición {maquina}")
            break

    if verificar_victoria("O"):
        imprimir_tablero()
        print("¡La máquina ha ganado!")
        break

    if juego_terminado():
        imprimir_tablero()
        print("¡Es un empate!")
        break
