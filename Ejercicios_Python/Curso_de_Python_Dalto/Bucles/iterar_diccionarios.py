diccionario = {
    "nombre": "Lucas",
    "apellido": "Dalto",
    "subs": 10000
}

#recorriendo diccionario para obtener las claves
for key in diccionario.items():
    print(key)
    
#recorriendo el diccionario con items para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")


