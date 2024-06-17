frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]

for fruta in frutas:
    print(fruta)


#En esta itineracion se salta la granada con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(fruta)


#evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "pera":
        break
    print(fruta)
print("bucle terminado")

#recorrer una cadena de texto
cadena = "Hola dalto"

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros = [2,5,8,10]

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

for num in numeros:
    print(num)