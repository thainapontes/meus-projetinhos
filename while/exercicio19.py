numero = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))
while numero2==0: #enquanto
    print('Digite outro valor diferente de zero.')
    numero2 = float(input('Digite um número: '))
divisao= numero/numero2
print(f' O resultado da divisão é {divisao:.2f}.')