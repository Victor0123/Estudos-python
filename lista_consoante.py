letras = []
x = 1

while x <= 10:
    letras.append(input("Letras: "))
    x += 1

x = 0
cont = 0

while x <= 9:
    if letras[x] not in 'aeiou':
        cont += 1
    x += 1

print ("Foram lidos %d consoantes" %cont)
    
