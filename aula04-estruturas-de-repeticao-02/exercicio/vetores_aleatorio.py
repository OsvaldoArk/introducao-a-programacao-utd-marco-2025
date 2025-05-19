import random

numeros = []

contador_positivo = 0
contador_negativo = 0

for x in range(0,20):
    numeros.append(random.randint(-10,10))

for x in numeros:
    if(x >= 0):
        contador_positivo+=1
    else:
        contador_negativo+=1
    
print(numeros)
print("positivos: ",contador_positivo)
print("negativos: ",contador_negativo)


