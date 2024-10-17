vetora=['']*10
vetorb=['']*10
tam=len(vetora)
for posicao in range(tam):
    vetora[posicao]=float(input('Digite um número: '))
x=int(input('Digite um número multiplicador: '))
mult= vetora[posicao]*x
for y in range(tam):
    vetorb[y]=vetora[y]*mult
print(vetora)
print(x)
print(vetorb)



