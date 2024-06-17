lista = list(["hola","dalto",34])
print(lista)

#LEN devuelve la cantidad de la lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#APPEND agrega un elemento a la lista
lista.append("jajaja")
print(lista)

#INSERT agrgando un elemento a la lista en un indice especifico
lista.insert(2,"TOMA MAMA")
print(lista)

#EXTEND agregando varios elementos a la lista
lista.extend([False,2030])
print(lista)

#POP eliminando un elemento de la lista por su indice
lista.pop(0) #poner el indice del indice que quieres eliminar
lista.pop(-1)#elimina el ultimo de la lista
lista.pop(-2) #eliminar el anteultimo
print(lista)

#REMOVE removiendo un elemento de la lista por su valor
lista.remove("TOMA MAMA") #si no esta en la lista saltará un exception
print(lista)

#CLEAR eliminando todos los elementos de la lista
#lista.clear()

#SORT ordena la lista, si la lista es numerica
lista2 = ([5,9,0,8,16])
lista2.sort() #ordena de menor a mayor
lista2.sort(reverse=True) #los ordena de mayor a menor
print(lista2)

#REVERSE invirtiendo los elementos de una lista
lista.reverse()
print(lista)

#INDEX verifoicando que un elemento se encuentra en la lista, si no esta lanza una excepcion
elemento_encontrado = lista.index(34) #te dice en que posicion esta
print(elemento_encontrado)