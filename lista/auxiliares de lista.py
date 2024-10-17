numero=[2,5,9,1]
numero[2]=3
numero.append(7)#adicionando o valor 7 no ultimo indice
numero.sort() # é para colocar tudo em ordem crescente
numero.sort(reverse=True) #coloca tudo em ordem decrescente
numero.insert(2,0) #inserindo na posição 2 o numero 0
numero.pop()#remove o ultimo indice
if 4 in numero:
    numero.remove(4)
else:
    print('Não há o valor 4 para remover.')
tam=len(numero)
print(f'Essa lista tem {tam} elementos.')
print(numero)