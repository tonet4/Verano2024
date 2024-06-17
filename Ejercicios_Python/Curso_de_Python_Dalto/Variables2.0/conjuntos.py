#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#creando un set con una tupla dentro
conjunto = set(["dato1",("dato2","dato3")])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"dato1","dato2"})
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos

#verificar si es un subconjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)
print(resultado)