'''
fim = 0
multi = 3

while (fim < 10):
    fim = fim + 1
    resultado = multi * fim
    print (multi , "X", fim , "=", resultado)



n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d número:" %n))
    soma = soma + x
    n = n + 1
print ("Soma: %d" %soma)

'''

n = 1
soma = 0

while n <= 10:
    x = int(input("Digite o %d número:" %n))
    soma = soma + x
    n = n + 1

print ("Média: %5.2f" %(soma%10))
