n1=float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
if n1==n2:
    print(f'Os números são iguais.')
else:
    if n1>n2:
        print(n2,n1)
    else:
        print(n1,n2)