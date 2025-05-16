numero01 = 10
numero02 = 60
numero03 = 90


if(numero01 > numero02):

    if(numero01 > numero03):

        if(numero02 > numero03):
            print(numero03," - ",numero02," - ",numero01)
        else:
            print(numero02," - ",numero03," - ",numero01)
    
    else:
        print(numero02," - ",numero01," - ",numero03)

elif(numero01 > numero03):
    print(numero03," - ",numero01," - ",numero02)

else: 
    if(numero02 > numero03):
        print(numero01," - ",numero03," - ",numero02)
    else:
        print(numero01," - ",numero02," - ",numero03)