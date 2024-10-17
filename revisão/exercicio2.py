n= int(input('Digite o número: '))
if n>0:
    if n%2==0:
        print(f'{n} é um número positivo e par.')
    else:
        print(f'{n} é um número positivo e ímpar.')
if n<0:
    if n%2==1:
        print(f'{n} é um número negativo e ímpar.')
    else:
        print(f'{n} é um número negativo e par.')

