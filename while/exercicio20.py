pergunta=1
while pergunta ==1:
    n = int(input('Digite um número: '))
    while n <= 0:
        n = int(input('Valor inválido. Digite outro número: '))
    for i in range(1,n):
        print(i, end= ' ')
    pergunta= int(input('\nDeseja digitar outro número?\n'
                         'Digite 1 para sim\n'
                         'e 2 para não.\n'))


