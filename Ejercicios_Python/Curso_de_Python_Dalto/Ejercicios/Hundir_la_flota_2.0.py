

import os


tablero = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " ",10: " ",
           11: " ",12: " ",13: " ",14: " ",15: " ",16: " ",17: " ",18: " ",19: " ",20: " ",
           21: " ",22: " ",23: " ",24: " ",25: " ",26: " ",27: " ",28: " ",29: " ",30: " ",
           31: " ",32: " ",33: " ",34: " ",35: " ",36: " ",37: " ",38: " ",39: " ",40: " ",
           41: " ",42: " "}

mensaje1=" "
def imprimir_tablero():
    print("   A   B   C   D   E   F   G")
    print(" +---+---+---+---+---+---+---+")
    print(f"0| {tablero[1]} | {tablero[2]} | {tablero[3]} | {tablero[4]} | {tablero[5]} | {tablero[6]} | {tablero[7]} |0                    ////HUNDIR LA FLOTA////")
    print(" +---+---+---+---+---+---+---+")
    print(f"1| {tablero[8]} | {tablero[9]} | {tablero[10]} | {tablero[11]} | {tablero[12]} | {tablero[13]} | {tablero[14]} |1")
    print(" +---+---+---+---+---+---+---+")
    print(f"2| {tablero[15]} | {tablero[16]} | {tablero[17]} | {tablero[18]} | {tablero[19]} | {tablero[20]} | {tablero[21]} |2")
    print(" +---+---+---+---+---+---+---+")
    print(f"3| {tablero[22]} | {tablero[23]} | {tablero[24]} | {tablero[25]} | {tablero[26]} | {tablero[27]} | {tablero[28]} |3")
    print(" +---+---+---+---+---+---+---+")
    print(f"4| {tablero[29]} | {tablero[30]} | {tablero[31]} | {tablero[32]} | {tablero[33]} | {tablero[34]} | {tablero[35]} |4")
    print(" +---+---+---+---+---+---+---+")
    print(f"5| {tablero[36]} | {tablero[37]} | {tablero[38]} | {tablero[39]} | {tablero[40]} | {tablero[41]} | {tablero[42]} |5")
    print(" +---+---+---+---+---+---+---+")
    print("   A   B   C   D   E   F   G")

# Función para convertir letras a números
def letra_a_numero(letra):
    letras = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
    return letras.get(letra.upper(), 0)  # Devuelve 0 si la letra no es válida

def comprueba_posicion_tiene_X(posicion):
    if posicion in tablero:
        if tablero[posicion] == "X":
            return 1 #tiene X
        else:
            return 0 #No tiene X
        
def comprueba_posicion_tiene_X_player(posicion):
    if posicion in tablero_player:
        if tablero_player[posicion] == "X":
            return 1 #tiene X
        else:
            return 0 #No tiene X
        
def comprueba_posc_alrededor(posicion):
    posicion_izq = posicion - 1
    posicion_der = posicion +1
    posicion_arrib = posicion -7
    posicion_abaj = posicion +7
    if posicion in tablero:
        if tablero[posicion_izq] == " " and tablero[posicion_der] == " " and tablero[posicion_arrib] == " " and tablero[posicion_abaj] == " ":
            return 1 #no tiene x al rededor
        elif tablero[posicion_izq] == "X" and tablero[posicion_der] == " " and tablero[posicion_arrib] == " " and tablero[posicion_abaj] == " ":
            return 2
        elif tablero[posicion_izq] == "X" and tablero[posicion_der] == "X" and tablero[posicion_arrib] == " " and tablero[posicion_abaj] == " ":
            return 3
        elif tablero[posicion_izq] == "X" and tablero[posicion_der] == "X" and tablero[posicion_arrib] == "X" and tablero[posicion_abaj] == " ":
            return 4
        else:
            return 0 #tiene x al rededor
        
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
""" 
    ELECCION DE LOS BARCOS
        -1 barco de 4 posiciones
        -3 barcos de 3 posiciones
        -1 barco de 2 posiciones
"""
#Barco de 4 posiciones
cont_barco_4 = 0
print("Bienvendio al juego de Hundir la flota")
print("Vamos a empezar colocando un barco de 4 posiciones")

while cont_barco_4 < 4:
    
    vertical = int(input("Dime posición vertical, tiene que ser un número entre 0 y 5: "))
    horizontal = input("Dime posición horizontal, tiene que ser una letra entre la A y la G: ")

    
    num_horizontal = letra_a_numero(horizontal)
    if num_horizontal != 0 and 0 <= vertical <= 5:
        posicion = vertical * 7 + num_horizontal
        if 1 <= posicion <= 42 and comprueba_posicion_tiene_X(posicion) == 0:
            tablero[posicion] = "X"
            cont_barco_4 += 1 
        else:
            print("Posición fuera de rango o posición repetida")
    else:
        print("Posición inválida")
    
    limpiar_pantalla()
    imprimir_tablero()

#3 barcos de 3 posiciones
cont_ronda3=0
while cont_ronda3 < 3:
    print("Vamos a colocar un nuevo barco de 3 posiciones")
    cont_barco_3 = 0
    while cont_barco_3 < 3:
        
        vertical = int(input("Dime posición vertical, tiene que ser un número entre 0 y 5: "))
        horizontal = input("Dime posición horizontal, tiene que ser una letra entre la A y la G: ")

        
        num_horizontal = letra_a_numero(horizontal)
        if num_horizontal != 0 and 0 <= vertical <= 5:
            posicion = vertical * 7 + num_horizontal
            if 1 <= posicion <= 42 and comprueba_posicion_tiene_X(posicion) == 0:
                tablero[posicion] = "X"
                cont_barco_3 += 1 
            else:
                print("Posición fuera de rango o posición repetida")
        else:
            print("Posición inválida")
        
        limpiar_pantalla()
        imprimir_tablero()
    cont_ronda3+=1
    
#Colocamos un barco de dos posiciones

print("Vamos a colocar un nuevo barco de 2 posiciones")
cont_barco_2 = 0
while cont_barco_2 < 2:
        
    vertical = int(input("Dime posición vertical, tiene que ser un número entre 0 y 5: "))
    horizontal = input("Dime posición horizontal, tiene que ser una letra entre la A y la G: ")

        
    num_horizontal = letra_a_numero(horizontal)
    if num_horizontal != 0 and 0 <= vertical <= 5:
        posicion = vertical * 7 + num_horizontal
        if 1 <= posicion <= 42 and comprueba_posicion_tiene_X(posicion) == 0:
            tablero[posicion] = "X"
            cont_barco_2 += 1 
        else:
            print("Posición fuera de rango o posición repetida")
    else:
        print("Posición inválida")
        
    limpiar_pantalla()
    imprimir_tablero()
    
#TURNO PARA EL JUGADOR

tablero_player = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " ",10: " ",
           11: " ",12: " ",13: " ",14: " ",15: " ",16: " ",17: " ",18: " ",19: " ",20: " ",
           21: " ",22: " ",23: " ",24: " ",25: " ",26: " ",27: " ",28: " ",29: " ",30: " ",
           31: " ",32: " ",33: " ",34: " ",35: " ",36: " ",37: " ",38: " ",39: " ",40: " ",
           41: " ",42: " "}

def imprimir_tablero_player():
    print("   A   B   C   D   E   F   G")
    print(" +---+---+---+---+---+---+---+")
    print(f"0| {tablero_player[1]} | {tablero_player[2]} | {tablero_player[3]} | {tablero_player[4]} | {tablero_player[5]} | {tablero_player[6]} | {tablero_player[7]} |0                    ////HUNDIR LA FLOTA////")
    print(" +---+---+---+---+---+---+---+")
    print(f"1| {tablero_player[8]} | {tablero_player[9]} | {tablero_player[10]} | {tablero_player[11]} | {tablero_player[12]} | {tablero_player[13]} | {tablero_player[14]} |1                      {mensaje1}")              
    print(" +---+---+---+---+---+---+---+")
    print(f"2| {tablero_player[15]} | {tablero_player[16]} | {tablero_player[17]} | {tablero_player[18]} | {tablero_player[19]} | {tablero_player[20]} | {tablero_player[21]} |2")
    print(" +---+---+---+---+---+---+---+")
    print(f"3| {tablero_player[22]} | {tablero_player[23]} | {tablero_player[24]} | {tablero_player[25]} | {tablero_player[26]} | {tablero_player[27]} | {tablero_player[28]} |3")
    print(" +---+---+---+---+---+---+---+")
    print(f"4| {tablero_player[29]} | {tablero_player[30]} | {tablero_player[31]} | {tablero_player[32]} | {tablero_player[33]} | {tablero_player[34]} | {tablero_player[35]} |4")
    print(" +---+---+---+---+---+---+---+")
    print(f"5| {tablero_player[36]} | {tablero_player[37]} | {tablero_player[38]} | {tablero_player[39]} | {tablero_player[40]} | {tablero_player[41]} | {tablero_player[42]} |5")
    print(" +---+---+---+---+---+---+---+")
    print("   A   B   C   D   E   F   G")


def comprobar_barco_hundido(posicion, tablero):
    # Check horizontal
    for i in range(-1, 2):
        pos = posicion + i
        if pos < 1 or pos > 42:
            continue
        if tablero[pos]!= "X":
            break
    else:
        return 1

    # Check vertical
    for i in range(-7, 8, 7):
        pos = posicion + i
        if pos < 1 or pos > 42:
            continue
        if tablero[pos]!= "X":
            break
    else:
        return 1

    return 0
    

print("-------------------------------")
print("EMPIEZA EL JUEGO!! ADIVINA DONDE HA COLOCADO LOS BARCOS TU CONTRINCANTE Y HUNDELOS!!")
print("-------------------------------")
imprimir_tablero_player()



cont_player=0
while cont_player < 15:
    
    mensaje1= " "
    vertical_player = int(input("Dime posición vertical, tiene que ser un número entre 0 y 5: "))
    horizontal_player = input("Dime posición horizontal, tiene que ser una letra entre la A y la G: ")
    
    num_horizontal_player = letra_a_numero(horizontal_player)
    if num_horizontal_player != 0 and 0 <= vertical_player <= 5:
        posicion = vertical_player * 7 + num_horizontal_player
        if 1 <= posicion <= 42 and comprueba_posicion_tiene_X(posicion) == 1:
            tablero_player[posicion] = "X"
            cont_player += 1 
            if comprobar_barco_hundido(posicion,tablero) == 1 and comprobar_barco_hundido(posicion,tablero_player) == 1:
                mensaje1 = ("+++ BARCO HUNDIDO  AAAAAAAAAAAAAA+++")
            else:
                print("sigue")
            
        else:
            tablero_player[posicion] = "O"
            print("Casiiii! Has Fallado!!!!!")
    else:
        print("Posición inválida")
        
    limpiar_pantalla()
    imprimir_tablero_player()