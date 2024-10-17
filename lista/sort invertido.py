# crie um programa q vai ler varios numeros e por na lista,
# depois mostre quantos numeros foram digitados, a lista em forma desc.
# se o valor for 5 e esta ou n na lista

lista=[]
for x in range(1,5+1,1):
    numero=int(input('Digite um número: '))
    lista.append(numero)
if 5 in lista:
    print('O valor 5  está na lista.')
else:
    print('O valor 5 não está na lista.')
lista.sort(reverse=True)
print(f'{lista}')
