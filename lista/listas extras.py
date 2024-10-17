# crie um programa q vai ler numeros e colocar em uma lista
# depois, crie duas listas extras que vão conter apenas os valores pares e os impares
# no final, mostre o conteudo das tres listas geradas

lista=[]
listapares=[]
listaimpares=[]
for x in range(1,5+1,1):
    numero=int(input('Digite um número: '))
    lista.append(numero)
    if numero%2==0:
        listapares.append(numero) #adiciona o numero e n a lista toda
    else:
        listaimpares.append(numero)
print(f'Os valores totais digitados foram: {lista}')
print(f'Os valores pares digitados foram: {listapares}')
print(f'Os valores ímpares digitados foram: {listaimpares}')