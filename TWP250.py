'''
i = 1
fat = 1
n = int(input("Digite um valor: "))

while i <= n:
    fat = fat * i
    i = i + 1

print ("Fatorial:", fat)
'''


soma = 0

while True:
    x = int(input("Digite o número (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma: %d" %soma)
