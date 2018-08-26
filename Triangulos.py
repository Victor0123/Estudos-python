a = int(input("Digite o primeiro valor do triângulo: "))
b = int(input("Digite o segundo valor do triângulo: "))
c = int(input("Digite o terceiro valor do triângulo: "))

if a <= b + c and b <= a + c and c <= a + b:
    if a == b and b == c:
        print("Triângulo equilatero")
    elif a == b or a == c or c == b:
        print("Triângulo isóceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é triângulo")
