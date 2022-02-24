#Autor: Axel Alva

from math import *




def catetoDesconocidoTrianguloRectangulo(datoLado):
  	
	cateto = sqrt(datoLado**2 - (datoLado/2)**2) #Despejo 


	return cateto


def superficieTrianguloEquilatero(datoLado):


	return (datoLado * catetoDesconocidoTrianguloRectangulo(datoLado)) / 2 #Llamo a una funcion y saco superficie



def superficieHexagono(datoLado) :

	superficie = 6 * superficieTrianguloEquilatero(datoLado)  #Llamo a una funcion y saco superficie

	return superficie

print(superficieHexagono(6))
print(superficieHexagono(8))



