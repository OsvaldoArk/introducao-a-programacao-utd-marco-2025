numero = int(input("digite um número para gerar sua tabuada"))

for multiplicador in range(0,11):
    if multiplicador % 2 == 0:
        continue

    print(numero,"x",multiplicador,"=",numero*multiplicador)
