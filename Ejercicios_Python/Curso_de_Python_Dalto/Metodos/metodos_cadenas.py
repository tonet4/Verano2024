cadena1 = "Hola soy Antonio5"
cadena2 = "Bienvenido maquina"

#DIR decuelve la lista de atributos validos del objeto que pasamos
#print(dir(cadena1))

#UPPER Metodo convierte en mayusculas
resultado = cadena1.upper()
print(resultado)

#LOWER metodo que convierte a minusculas
resultado = cadena1.lower()
print(resultado)

#CAPITALIZE convierte la primera letra en mayuscula
primera_letra_mayuscula = cadena1.capitalize()
print(primera_letra_mayuscula)

#FIND buscamos una cadena en otra cadena (tambien cuenta los espacios)
busqueda_find = cadena1.find("Hola") #devuelve 0
busqueda_find = cadena1.find("o") #devuelve 1
busqueda_find = cadena1.find("d") #devuelve -1 xq no hay ninguna d
print(f"Find: {busqueda_find}")

#INDEX buscamos una cadena dentro de otra cadena(si no hay concidencia nos lanza un exception)
busqueda_index = cadena1.index("o")
#print(busqueda_index)

#ISNUMERIC si es numerico devuelve true
es_numerico = cadena1.isnumeric()
print(es_numerico)

cadena3 = "tienequeestartodojunto"
#ISALPHA si es alfanumerico devuelve un true
es_alfanumerico = cadena3.isalpha()
print(f"alpha: {es_alfanumerico}")

#COUNT buscamos una cadena dentro de otra cadena, cuenta las veces que coincide
contar_coincidencias = cadena1.count("o")
print(f"contar: {contar_coincidencias}")

#LEND contamos las concidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias.
contar_caracteres = len(cadena1)
print(f"cuantos caracteres tiene: {contar_caracteres}")

#STARTSWITH verificamos si una cadena empieza con otra cadena dad, si es asi devuelve true
empieza_con = cadena1.startswith("H")
print(f"Empieza con: {empieza_con}")

#ENDSWITH verificamos si una cadena termina con otra cadena dad, si es asi devuelve true
termina_con = cadena1.endswith("a")
print(f"Termina con el caracter: {termina_con}")

#REPLACE remplaza un pedazo de la cadena dada, por otra dada
#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("la","lu")
print(cadena_nueva)

cadena4 = "Hola,como,estas"
cadena_nueva2 = cadena4.replace(","," ")
print(cadena_nueva2)

#SPLIT separar cadenas con la cadena que le pasemos
cadena_separada = cadena4.split(",")
print(cadena_separada)
print(cadena_separada[0])