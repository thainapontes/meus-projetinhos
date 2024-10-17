numeros=[0]*5
tam=len(numeros)
for i in range(tam):
    numeros[i]=int(input(f'Digite o {i+1}º número: '))
for x in range (tam-1,-1,-1): #tam-1 = pq apesar do array ter espaço 5, ele só vai ate a posição 4.
   print(f'{numeros[x]}', end = ' ')