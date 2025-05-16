import math
numero01 = 30

numero02 = 5

operacao = "^"

match operacao:
    case "+": print(numero01+numero02)
    case "-": print(numero01-numero02)
    case "*": print(numero01*numero02)
    case "/": print(numero01/numero02)
    case "^": print(numero01**numero02)
    case _: print("operador inválido")