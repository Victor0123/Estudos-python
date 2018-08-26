def print_forca(letras,palavra):
    forca = ""
    for l in palavra:
        if l in letras:
            forca += l
        else:
            forca += '-'
           
    print(forca)


palavra = "farmacia"
letra = input("Digite uma letra: ")

erros = 0
letras = []
letras.append(letra)

print_forca(letras,palavra)

