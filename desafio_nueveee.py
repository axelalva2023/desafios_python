#Autor: Axel Alva



años_bisiestos = [x for x in range(1583,2051) if (x % 400 == 0) or (x % 4 == 0) and not (x % 100 == 0)]  #Genero lista

print(años_bisiestos) #Muestro lista

otra_años_bisiestos = [x for x in años_bisiestos if x % 10 == 0] #Genero lista con los datos anterior

print(otra_años_bisiestos) #Muestro lista

print(otra_años_bisiestos[:10]) #Muestro segmento

