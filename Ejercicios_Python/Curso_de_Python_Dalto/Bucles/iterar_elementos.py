animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista de animales
for animal in animales:
    print(f"Animal: {animal}")
    
#recorriendo una lista con numeros y multiplicando cada valor por 10
for num in numeros:
    resultado = num * 10
    print(resultado)
    
#recorriendo dos listas a la vez del mismo tamaño
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
#imprimir un rando de numeros, del 5 al 9
for num in range(5,10):
    print(num)

#imprime del 0 al 4 
for num in range(5):
    print(num)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)

#para acceder al indice
for num in enumerate(numeros):
    print(num[0])   

#para acceder al valor
for num in enumerate(numeros):
    print(num[1])
    
#para acceder al indice y al valor
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')
    
#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    
#todo lo anterior se puede usar con tuplas y conjuntos
    

    
  
