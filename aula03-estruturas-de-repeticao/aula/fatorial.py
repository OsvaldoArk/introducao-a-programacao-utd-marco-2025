import math

numero = 5
# 5! = 5 * 4 * 3 * 2 * 1
fatorial = 1

while numero >= 1:
    print("contagem: ",numero," X ",fatorial," = ",fatorial*numero)
    #fatorial = fatorial * numero
    fatorial*=numero
    #numero = numero -1
    numero-=1

print("resposta: ",fatorial)

print("biblioteca: ",math.factorial(5))