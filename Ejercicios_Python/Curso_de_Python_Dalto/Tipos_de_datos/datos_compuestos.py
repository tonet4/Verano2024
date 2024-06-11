
#Esto es una list y sirve para agrupar datos y se puede modificar
lista = ["Antonio", "Estudiante", True, 1.85]
print(lista)
print(lista[1])
lista[3] = 1.95
print(lista)

#La tupla no se puede modificar y va con parentesis
tupla = ("Antonio", "Estudiante", True, 1.85)
print(tupla)

#Creando un conjunto set
#Es casi igual que la lista son elementos desordenados, no pueden modificar, pero si se pueden redifinir
#No puedes acceder por el incice

conjunto = {"Antonio", "Estudiante", True, 1.85}
print(conjunto)

#No permite repetir valores
conjunto = {"Antonio", "Estudiante", True, 1.85, "Antonio" }
print(conjunto)

#Creando un diccionario (dict)
#El indice en vez de ser un numero es el nombre que le ponemos
#clave : valor
diccionario = {
    'nombre' : "Antonio Esteban",
    'apodo' : "Esteban",
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : "Esteban"
    
}

print(diccionario["nombre"])
print(diccionario["altura"] + 2)