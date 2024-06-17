#creando un diccionario con dict()
diccionario = dict(nombre='lucas',apellido='dalto')

#las listas no pueden ser claves y usamos fronzet para meter conjuntos
diccionario = {frozenset(["dalto","dato2"]):"jajaja"}

#las tuplas si que pueden ser claves
diccionario = {("dalto","dato2"):"jajaja"}

#creando diccionarios con fromkeys(), sirve para crear un diccionario vacio
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys(), sirve para crear un diccionario vacio, igual a no se
diccionario5 = dict.fromkeys(["nombre","apellido"],"No se")
print(diccionario5)

#creando un diccionario sin valores, cada letra igual a none
diccionario2 = dict.fromkeys("abcdefghi")
print(diccionario2)

#creando un diccionario con el valor de cada letra igual a valor2
diccionario3 = dict.fromkeys("abcdefghi", "valor2")
print(diccionario3)

