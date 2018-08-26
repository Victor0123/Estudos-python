#Funções

def par_impar(numero):
    if(numero % 2 == 0):
        print("É par: ", numero)
    else:
        print("É impar: ", numero)

#Inicio programa
cont = 0
qtd_num_pares = 0

while(cont <= 10):
    if(cont % 2 == 0):
        qtd_num_pares = qtd_num_pares + 1
    par_impar(cont)    
    cont = cont + 1

print (qtd_num_pares)

