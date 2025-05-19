numeros = []
soma = 0

for contador in range(0,5):
    numeros.append(int(input("digite um número")))

for valor in numeros:
    #soma = soma + valor
    soma+=valor

print(soma)