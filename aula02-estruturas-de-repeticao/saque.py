conta = 999
senha = 456
saldo = 100

usr_conta = int(input("digite o número da sua conta\n"))

usr_senha = int(input("digite o número da senha\n"))

if usr_conta == conta and usr_senha == senha:
    
    saque = int(input("quanto deseja sacar?"))

    if saque <= saldo:
        #saldo = saldo - saque
        saldo-=saque
        print("operação realizada com sucesso!")
        print("o seu saldo restante é de R$ ",saldo," reais")
    
    else: 
        print("você não possuí saldo suficiente para finalizar a operação")

else:
    print("conta ou senha inválidos")

