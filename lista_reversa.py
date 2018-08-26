x = []
cont = 0

while cont < 10:
    n = float(input("Digite um valor: "))
    x.append(n)
    cont += 1
print (x)

x.reverse()
print ("Vetor inverso:" ,x)
