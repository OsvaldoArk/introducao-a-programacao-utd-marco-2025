acertos = 10

match acertos:
    case 1: print("ruim")
    case 2: print("insuficiente")
    case 3: print("regular")
    case 4: print("bom")
    case 5: print("ótimo")
    case _: print("número de acertos inválido")