#ordenador es = 0
#usuario es = x

import random

cont = 0

tablero = ({1:" ",2:" ",3:" "})
tablero2 = ({4:" ",5:" ",6:" "})
tablero3 = ({7:" ",8:" ",9:" "})

while cont <= 20:

    print(f"| {tablero[1]} | {tablero[2]} | {tablero[3]} |")
    print(f"| {tablero2[4]} | {tablero2[5]} | {tablero2[6]} |")
    print(f"| {tablero3[7]} | {tablero3[8]} | {tablero3[9]} |")

    repe_usu = True
    repe_maqui = True
    salir = True
    print("TE TOCA")
    while repe_usu:
        usuario = int(input("Dime posición, tiene que ser un número entre 1 y 9: "))
    
        if (usuario >= 1) and (usuario <= 3):
            if tablero[usuario] == " ":
                tablero[usuario] = "X"
                cont+= 1
                repe_usu = False
            else:  
                print(f"La casilla {usuario} ya está ocupada")
        elif (usuario >= 4) and (usuario <= 6):
            if tablero[usuario] == " ":
                tablero2[usuario] = "X"
                cont+= 1
                repe_usu = False
            else:  
                print(f"La casilla {usuario} ya está ocupada")
        else:
            if tablero[usuario] == " ":
                tablero3[usuario] = "X"
                cont+= 1
                repe_usu = False
            else:  
                print(f"La casilla {usuario} ya está ocupada")
        
    
    maquina = int(random.randint(1,9))
    
    if (maquina >= 1) and (maquina <= 3):
        tablero[maquina] = "O"
        cont+= 1
        print(f"La máquina eligió la posición {maquina}")
    elif (maquina >= 4) and (maquina <= 6):
        tablero2[maquina] = "O"
        cont+= 1
        print(f"La máquina eligió la posición {maquina}")
    else:
        tablero3[maquina] = "O"
        cont+= 1
        print(f"La máquina eligió la posición {maquina}")
    
    