a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))

maior,menor = a,a

if maior < b:
    maior = b

if maior < c:
    maior = c

if maior < d:
    maior = d

if maior < e:
    maior = e

if menor > b:
    menor = b

if menor > c:
    menor = c

if menor > d:
    menor = d

if menor > e:
    menor = e

print("Maior valor %d menor valor %d" %(maior,menor))
