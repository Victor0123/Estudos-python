palavra = input("Digite uma palavra: ")
cont = 0
troca = ""

while cont < len(palavra):
    if palavra[cont] in "aeiou":
        troca += "*"

    else:
        troca += palavra[cont]
    cont += 1

    
print(troca)
