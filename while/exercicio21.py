confirma=1
contagem=0
while confirma == 1 and contagem <=3:
    somanegativo=0
    for i in range(1,11):
        numero= int(input(f'Informe o {i} número: '))
        if numero<0:
            somanegativo=somanegativo+1
print(somanegativo)
confirma=int(input('\n Deseja digitar outro numero...\n SIM 1 e \nao'))
contagem=contagem+1