for x in range(0,5,1):
    print('Eu te amo mil milhões!') #pedi para ele repetir isso 1 milhão de vezes.
print('Fim!') #vai printar apenas uma única vez, pois está fora do for.

print('-----------------------------------------')

for x in range(0,3,1):
    print(x) #dessa forma, ele vai printar as posições, o x é uma variável de controle.

print('------------------------------------------')

i=int(input('Ínicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for x in range (i,f+1,p):
    print(x)

print('------------------------------------------')

soma=0
for n in range(1,4,1):
    numero=int(input('Digite um número: '))
    soma=soma+numero
print(f'A soma de todos os valores foi {soma}.')