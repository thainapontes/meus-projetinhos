numeros=[0]*10
tam=len(numeros)
quantidade=0
for i in range(tam):
    numeros[i]=int(input('Digite um número: '))
numero= int(input('Digite um número de comparação:'))
for x in range(tam):
    if numero==numeros[x]:
        quantidade= quantidade+1
print(f'O {numero[x]} apareceu {quantidade} vezes.')
