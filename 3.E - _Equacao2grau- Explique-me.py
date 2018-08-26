#Importa a função de raiz quadrada do modulo math
from math import sqrt 

#Instruções para o calculo de raiz quadrada
print("Equações completas as variaveis A, B ou C devem ser diferentes de zero.")
print("Para obter 2 raizes utilize como ex: a = 1 b = -5 c = 6")
print("Para obter 1 raiz utilize como   ex: a = 4 b = 4 c = 1")
print("Para não obter raiz utilize como ex: a = 1 b = -4 c = 5 \n")

#Solicita os valores necessarios para o calculo da raiz quadrada
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

#Testa se é possivel efetuar o calculo da raiz quadrada com os valores fornecidos pelo usuario
if(a == 0 or b == 0 or c == 0):
    print("Valores informados não correspondem a uma equação de 2º grau completa.")
else:
    #Efetua o calculo do delta
    b2 = b * b
    delta = b2 - (4 * a * c)
    #Testa se é possivel calcular uma raiz quadrada com o valor de delta
    if delta < 0 or (2 * a) == 0 :
        print("Impossivel calcular - nenhuma raiz real")
    else:
        #Calcula delta A
        x1 = (-b + (sqrt(delta))) / (2 * a)
        print("X1 = ", x1)

        #Calcula delta B
        if(delta > 0):
            x2 = (-b - (sqrt(delta))) / (2 * a)		
            print("X2 = ", x2)
    
    
