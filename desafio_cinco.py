#Autor: Axel Alva

"""De un triangulo rectángulo, conocemos el valor de los lados que forman el angulo recto (catetos) y desconocemos el valor del 3er lado (hipotenusa).

Escribí una función que reciba el valor de ambos catetos y devuelva el perímetro del triangulo (la suma de su 3 lados)
Como ayuda podes escribir otra función que calcule la hipotenusa y llamarla desde esta función de perímetro.

Escribí una función que reciba el valor de ambos catetos y devuelva la superficie del triangulo.

Proba las funciones perimetroTrianguloRectangulo() y superficieTrianguloRectangulo() con 2 o mas juegos de valores para observar su funcionamiento. """


#Datos de entrada:


#Operaciones con datos:
import math

def hipotenusaTrianguloRectangulo(n1,n2) :
	
	hipotenusa = math.sqrt(n1**2 + n2**2)

	return hipotenusa


def  perimetroTrianguloRectangulo(cateto1, cateto2) :

        perimetro = cateto1 + cateto2 + hipotenusaTrianguloRectangulo(cateto1, cateto2) #La suma de los 3 lados
        
        return perimetro

def superficieTrianguloRectangulo(cateto1, cateto2) :

	superficie_triangulo = (cateto1 * cateto2) / 2

	return superficie_triangulo


print (perimetroTrianguloRectangulo(8,8))
print (perimetroTrianguloRectangulo(7,7))
print (superficieTrianguloRectangulo(2,2))
print (superficieTrianguloRectangulo(1,1))





#Salida de datos:
