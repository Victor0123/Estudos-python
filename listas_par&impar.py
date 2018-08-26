numeros = []
par = []
impar = []
i = 0

while i <= 20:
    v = int(input("Digite o número: "))
    numeros.append(v)
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    elif numeros[i] % 2 == 1:
        impar.append(numeros[i])

    i += 1

print ("Números:", numeros)
print ("Pares:", par)
print ("Impares:", impar)
        
