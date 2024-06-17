diccionario = {
    "nombre" : 'lucas',
    1 : 'dalto',
    "subs" : 100000
}

#KEYS nos devuelve un objeto dict_item
#claves = diccionario.keys()
#print(claves)

#GET devuelve el elemnto que buscas (no me lanza una excepcion y si no encuentra nada el programa continua)
claves = diccionario.get(1)
print(claves)

#CLEAR elima todos los elementos de la lista
#diccionario.clear()

#POP eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario)
