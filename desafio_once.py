#Autor: Axel Alva

"""Te proveen un archivo CSV (valores separados por comas) llamado proceres.csv que contiene datos de algunos próceres.
Cada linea del archivo contiene los datos de un prócer, separados por comas.
Se te pide que leas el total del archivo en una variable llamada texto.

Usando la información en texto, generar una lista de lineas de texto lista1.

Usando la información en lista1 y usando map() generar otra lista2 que contenga listas de datos de los próceres (eliminación de comas).

Usando la información en lista2 y usando map() generar otra lista de diccionarios llamada proceres, al estilo de formato de registro que se detalla:

{
    'Nombre' : nnnn,
    'Apellido' : aaaa,
    'Ciudad natal': cccc,
    'Año natal': aaaa,
    'Año muerte': aaaa
}

Probablemente tengas que escribir una función auxiliar para ayudarte en esta tarea.

Usando map(), agregar un campo extra 'Edad' en cada registro de la lista proceres, basado en la diferencia de años de muerte y nacimiento.
Probablemente tengas que escribir una función auxiliar para ayudarte en esta tarea.

Finalmente usando la lista proceres, mostrar todos los datos por pantalla (campo y valor) dejando una linea en blanco entre cada prócer. Un ejemplo de salida seria:

Nombre: ------
Apellido: ------
Ciudad natal: -----
Año natal: ----
Año muerte: ----
Edad: -- """

def CalculoDiccionario(procer) :     
		for elemento in procer :
			variable = {
    'Nombre' : procer[0],
    'Apellido' : procer[1],
    'Ciudad natal': procer[2],
    'Año natal': int(procer[3]),
    'Año muerte': int(procer[4])
}	
		return variable

def CalculoEdad(argumento) :    

	argumento["Edad"] = argumento["Año muerte"] - argumento["Año natal"]
	
	return argumento


archivo = open("proceres.csv", "r")   

texto = archivo.read() 

lista1 = texto.split("\n")	

lista2 = list(map(lambda x: x.split(","), lista1))  

proceres = list(map(CalculoDiccionario,lista2)) 

proceres = list(map(CalculoEdad,proceres))  

for procer in proceres: 
    print()
    for key, value in procer.items():
        print(f"{key}: {value}")


