#programa onde o usuário possa digitar 7 valores e cadastre-os em uma unica lista
#que mantenha separados os valores pares e ímpares
#no final, mostre os valores pares e impares em ordem crescente
lista=[[],[]] # duas sublistas: [0] para pares, [1] para ímpares, desse jeito, sem precisar usar listas extras
#para armazenar os valores pares e impares

for x in range(1,7+1,1):
    valor=int(input(f'Digite o {x}° valor: '))
    if valor%2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()#para deixar em ordem crescente
lista[1].sort()
print('-='*30) #para ficar bonitinho
print(f'Os valores pares foram:{lista[0]} ')
print(f'Os valores ímpares foram:{lista[1]} ')
