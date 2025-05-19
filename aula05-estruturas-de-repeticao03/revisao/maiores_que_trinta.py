import random

numeros = []
maior = 0
contador = 0

while contador < 15:
    numeros.append(random.randrange(10,40))

    contador+=1

contador = 0

while contador < len(numeros):
    if(numeros[contador] > 30):
        maior+=1
    
    contador+=1

print(numeros)
print("existem ",maior," números maiores do que 30")
