# #programa onde o usuario digite varios valores e cadastre os em uma
# lista. se o numero ja existir la, ele n sera adicionado. no final tds serao
# exibidos em ordem crescente
lista=[]
for x in range(1,5+1,1):
    valores=int(input(f'Digite o {x}° valor: '))
    if valores not in lista:
        lista.append(valores)
        print('Adicionado!')
    else:
        print('Esse valor já existe. Por isso, não adicionei.')
lista.sort() #ordena a lista
print(f' Esses são os valores que eu adicionei: {lista}.')
