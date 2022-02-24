#Autor: Axel Alva
#En este desafio usamos condicionales y listas.


alumnos_aprobados = ["Ana", "Juan", "Pedro", "Carlos", "Camilo"]
alumnos_desaprobados = ["Lucas", "Pepe", "Malena", "Ivan", "Florencia"]

#Entrada de datos:

nombre = input("Por favor ingrese un nombre: ")



#Operaciones con datos

#Salida de datos:
if nombre in alumnos_aprobados:
    print("El alumno esta aprobado")
elif nombre in alumnos_desaprobados:
        print("El alumno esta reprobado")
else:
        print("El alumno no se encuentra en las listas")
