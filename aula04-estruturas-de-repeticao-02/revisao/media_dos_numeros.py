numero = 0
media = 0
contador = 0
flag = True

while flag:

    numero = int(input("digite qualquer número, zero para parar."))
    #media = media + numero
    media+=numero
    
    if numero == 0:
        flag = False
    
    contador+=1

media/=(contador-1)

print(contador)
print(media)
