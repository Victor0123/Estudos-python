
def exponencial(x,y):
    i = 0
    x_i = 1

    while(i < y):
        i = i + 1
        x_i = x_i * x
        
    return x_i

x = int(input("Digite a base: "))
y = int(input("Digite o expoente: "))
x_i = exponencial(x,y)
print(x_i)
