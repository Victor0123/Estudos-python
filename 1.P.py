cont = 50
soma = 0
media = 0

while cont <= 70:
    cont = cont + 1
    if cont % 2 == 0:
        soma = cont + cont
        media = soma / 70
    
print("Soma:", soma, "Média:", media)    
