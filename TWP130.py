'''
  Faça um programa que leia três números e mostre o maior deles
'''

'''
#Esse eu fiz sem ver o video
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if(num_1 > num_2 and num_1 > num_3):
    print("O número", num_1 ,"é maior que", num_2 ,"e", num_3)
if(num_2 > num_1 and num_2 > num_3):
    print("O número", num_2 ,"é maior que", num_1 ,"e", num_3)
if(num_3 > num_1 and num_3 > num_2):
    print("O número", num_3 ,"é maior que", num_1 ,"e", num_2)
'''

a = int(input("Primeiro: "))
b = int(input("Segundo: "))
c = int(input("Terceiro: "))

if a >= b and a >= c:
    print ("Primeiro: %d" %a)
elif b >= c:
    print ("Segundo: %d" %b)
else:
    print ("Terceiro: %d" %c)
    
#TWP120 com elif
minutos = int(input("Minutos utilizados: "))
if minutos < 200:
    preço = 0.20
elif minutos <= 400:
    preço = 0.18
elif minutos <= 800:
    preço = 0.15
else:
    preço = 0.08
       
print("Cont telefônica: R$%6.2f" % (minutos * preço))
    
