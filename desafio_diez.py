#Autor: Axel Alva


lista_numeros_enteros = [1,2,3,4,5,6,7,8,9,10]

lista_string = ",".join([str(n) for n in lista_numeros_enteros])

print(lista_string)

otra_lista_numeros_enteros = [int(elemento) for elemento in lista_string.split(",")]

print(otra_lista_numeros_enteros)








