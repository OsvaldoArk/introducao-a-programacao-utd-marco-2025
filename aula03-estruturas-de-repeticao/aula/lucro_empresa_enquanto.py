capital_inicial = 800_000
lucro = 15_000
mes = 0

print("capital inicial: ",capital_inicial," lucro por mês: ",lucro)

while mes < 11:
    # capital_inicial = capital_inicial + lucro
    capital_inicial+=lucro
    mes+=1
    print(mes+1,"º mês capital: ",capital_inicial)

print("resposta: ",capital_inicial)

