nota_a = int(input("Primeira nota: "))
nota_b = int(input("Segunda nota: "))
nota_c = int(input("Terceira nota: "))
nota_d = int(input("Quarta nota: "))
nota_parce = nota_a + nota_b + nota_c + nota_d
media = nota_parce / 4

if media >= 7 :
    print("Aprovado. Nota:", media)
else:
    exame = int(input("Nota de exame: "))
    if exame >= 5 :
        print("Aprovado em exame. Nota:", exame)
    else:
        print("Reprovado. Nota:", exame)
