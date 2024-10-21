galera=[]
dado=[] #lista temporária que servirá para depois depositar na lista galera
totmai=totmen=0
for x in range(1,3+1,1):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#fazendo uma cópia em galera do que está em dado
    dado.clear()#após fazer isso, já posso limpar essa lista.
for p in galera: #ou seja, para cada pessoa em galera..
    if p[1]>=18: #esse p[1] é a idade.
        print(f'{p[0]} é maior de idade.') #p[0] é o nome
        totmai=totmai+1 #aqui vai estar contando a quantidade de maiores de idade
    else:
        print(f'{p[0]} é menor de idade.')
        totmen=totmen+1 # aqui vai estar contando a quantida de menor de idade
print(f'Portanto, temos {totmai} maiores de idade e {totmen} menores de idade.')