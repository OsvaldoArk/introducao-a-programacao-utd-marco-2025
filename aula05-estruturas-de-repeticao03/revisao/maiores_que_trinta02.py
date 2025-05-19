import random

numeros = []
contador_maiores = 0

for numero in range(0,15):
    numeros.append(random.randrange(10,40))

for numero in numeros:
    if(numero>30):
        contador_maiores+=1

print(numeros)
print("existem ",contador_maiores," números maiores do que 30")
