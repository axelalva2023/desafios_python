#Autor: Axel Alva

lista = [5, 'casa', 0]

try:

	print(lista[3])
	
except IndexError:
	print("Error indice fuera de rango")


try:
	print(67 / lista[2])

except ZeroDivisionError:
	print("Error Division por cero")



try:

	print(-12 + lista[1])

except TypeError:
	print("Tipos de operandos no permitidos")

try:

	print(listado[1])

except NameError:
	print("El nombre de la lista no esta definido")


print('- Final del programa -')