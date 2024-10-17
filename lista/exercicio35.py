numeros=[0]*3
tam=len(numeros)
maior=0
for x in range(tam):
    numeros[x]=int(input('Digite um número: '))
for i in range(tam):
    if numeros[i]%2==0:
        print(f' O número {numeros[i]} é par.')

for j in range(tam):
    if numeros[j]>maior:
        maior=numeros[j]
print(f' O {maior} é o valor maior da lista.')
menor=maior
for v in range (tam):
    if numeros[v]<menor:
        menor = numeros[v]
print(f' O {menor} é o valor menor da lista')


