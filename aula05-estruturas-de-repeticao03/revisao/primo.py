numero = 6
divisores = 1
quantidade_divisores = 0

while divisores <= numero:

    if(numero % divisores == 0): 
        quantidade_divisores+=1
    
    print(numero,"/",divisores,"=",int(numero/divisores)," resto: ",numero%divisores," qtd divisores: ",quantidade_divisores)

    divisores+=1

if(quantidade_divisores==2):
    print("o número ",numero," é primo com ",quantidade_divisores," divisores")
else:
     print("o número ",numero," não é primo com ",quantidade_divisores," divisores")