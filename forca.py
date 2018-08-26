palavra = ['v','e','s','t','i','b','u','l','a','r']
letras = []


for i in range(0, len(palavra)):
    letras.append('-')
    
acerto = False

while acerto == False:
    letra = input("Digite uma letra: ")

    for i in range(0, len(palavra)):
        if letra == palavra[i]:
           letras[i] == letra
           
        print(letras[i])

    acerto == True

    for x in range(0, len(letras)):
        if letras[x] == '-':
            acerto = False
