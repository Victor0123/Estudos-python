def digite_numero(mensagem):
    resultado = 0    
    while (True):
        try:
            resultado = int(input(mensagem))
            break
        except ValueError as e:
            print("Digite um valor valido!")
    return resultado
