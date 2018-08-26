fib = 15
a,b = 1,1
cont = 1

while cont <= fib - 2:
    a,b = b,a + b
    cont = cont + 1

print("Fibonacci 15* posição:", b)
