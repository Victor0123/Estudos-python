posicao = int(input("Digite a posição desejada da sequência: "))
a,b = 1,1
cont = 1

while cont <= posicao - 2 :
    a,b = b,a + b
    cont = cont + 1

print("Fibonacci(Número correspondente a posição):", b)
