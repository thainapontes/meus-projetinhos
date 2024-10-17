lista= [' ']*5
tam=len(lista)
for i in range(tam): #esse for é para adicionar valores
    lista[i]=input(f'Digite o nome do {i+1}º aluno: ')
for indice in range(tam): #for para imprimir e ler oq tem no primeiro array
    print(indice,lista[indice]) #usa-se a virgula para juntar