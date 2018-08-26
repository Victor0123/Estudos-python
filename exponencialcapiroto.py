def exponencial(x,y):
    cont = 0
    exp = x
    x_i = 1
    while(cont < y):
        cont = cont + 1
        x_i = x_i * x
    return x_i



x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))

resultado = exponencial(x,y)
print(resultado)
