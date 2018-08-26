notas = []
cont = 0
x = 0

while cont < 4:
    n = int(input("Digite a nota: "))
    notas.append(n)
    x += notas[cont]
    cont += 1

   
print ("Notas:", notas)
media = x / 4
print ("Média: ", media)
