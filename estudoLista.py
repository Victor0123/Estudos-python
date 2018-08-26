#Listas aceitam todos os tipos de dados
#listas e tuplas são lineares
l = [1,2,3,4,5,6,7,8,9]

#l[0:0:0]de quanto:a quanto:de quanto em quanto

*a,b,c = l
a = [1,2,3,4,5,6,7]
b = [8]
c = [9]

x = []

for i in range(1,10):
    x.append(i)

print(x)#[1,2,3,4,5,6,7,8,9]


#Tuplas elas não são só listas imutavaeis, tuplas não desmontão

t = (1,2,3[4])#macete para mudar tuplas ahahshahshash

#conjuntos valores "fixos"

#conjuntos não aceitão repetições
set([1,2,3,3,3,3,3,3])
#{1,2,3}

#coisas q não varião são hash

#em conjuntos os menores saem primeiro (.pop)

#Dicionários, programador: Humano responsável por transformar café em linhas de código

pessoa = {
    'nome':'eduardo',
    'cargo':'programador',
    'função':lambda: f, *args:f(args),
    'saldo':{'dia 5':150, 'dia 10':[0, -100, -500]}
    }

