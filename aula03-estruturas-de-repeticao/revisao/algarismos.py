import math

numero = 945

unidade = numero % 10 

dezena = int((numero % 100 - unidade) /10)

centena = math.floor(numero / 100)

print("centena: ",centena)
print("dezena: ",dezena)
print("unidade: ",unidade)