def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def digite_numero(mensagem):
    try:
        return int(input(mensagem))
    except ValueError as e:
        print ("Precisa ser um numero")
        return 0

valor1 = digite_numero("Digite um valor: ")
valor2 = digite_numero("Digite outro valor: ")

soma = somar(valor1,valor2)
print ("resultado da soma", soma)

sub = subtrair(valor1,valor2)
print ("resulta da subtração", sub)

multi = multiplicar(valor1,valor2)
print("resutado da multiplicação", multi)
