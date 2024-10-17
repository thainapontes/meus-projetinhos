#um programa que leia 5 valores númericos, guarde na lista
#e no final msotre qual maior e o menor e suas respectivas posições na lista
listaValores=[]
for x in range (5):
    valor=int(input('Digite um valor: '))
    listaValores.append(valor)
maior=max(listaValores)
menor=min(listaValores)
posicaomaior=listaValores.index(maior)
posicaomenor=listaValores.index(menor)
print(f'Os valores digitados foram {listaValores}\nO maior valor é {maior} e sua posição é {posicaomaior}\n'
      f'\nO menor valor é {menor} e sua posição é {posicaomenor}\n')