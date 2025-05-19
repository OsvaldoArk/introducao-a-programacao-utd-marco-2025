def fib(enesimo):
    contador = 0
    a = 1
    b = 0
    c = 0

    while contador < enesimo:
        print(c,end=" ")

        c = a + b
        a = b
        b = c

        contador+=1


fib(20)