#Diferencia en porcentaje entre el curso actual y:
#-el mas rápido de otros cursos
#-el mas lento de otros cursos
#-el promedio de los cursos

curso_nuestro = 1.5
curso_mas_rapido = 2.5
curso_promedio = 4
curso_maximo = 7

#Diferencia entre el curso actual y el mas rapido en porcentaje
porcentaje_nuestro =  curso_nuestro * 100 / curso_maximo
print(f"Porcentaje de nuestro curso:  {porcentaje_nuestro}")

porcentaje_mas_rapido = curso_mas_rapido * 100 / curso_maximo
print(f"Porcentaje del más rápido:  {porcentaje_mas_rapido}")

print(f"Diferencia con el más rápido: {porcentaje_mas_rapido - porcentaje_nuestro}")

#Diferencia con el mas lento
print(f"Diferencia con el mas lento: {100 - porcentaje_nuestro}")

#El promedio de los cursos
porcentaje_promedio = curso_promedio * 100 / curso_maximo
print(f"Porcentaje del más rápido:  {porcentaje_promedio}")
print(f"Diferencia con el promedio: {porcentaje_promedio - porcentaje_nuestro}")
