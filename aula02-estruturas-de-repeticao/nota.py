nota01 = 7
nota02 = 4
nota03 = 8

media = (nota01+nota02+nota03)/3

if media >= 3 and media <7: 
    print("recuperacao")
    nota_final = 5
    media = (media+nota_final)/2

    if media >= 5:
        print("aprovado na recuperação")
    else:
        print("reprovado na recuperação")   

elif media >= 7:
    print("aprovado")
else:
    print("reprovado")

print("média: ",media)