
precogasolina= 5.80
precoetanol= 4.90
litros=float(input('Digite a quantidade de litros: '))
combustivel=input( 'Digite o tipo de combustível: ')
preco=0
if combustivel== 'E' or combustivel== 'e':
    preco= precoetanol * litros
    print(f'O valor que será pago é {preco}')

elif combustivel== 'G'or combustivel=='e':
    preco= precogasolina * litros
    print(f'O valor que será pago é {preco}')
#ou seja, se n for o if, pode ser...(pode dar verdadeira mas o if teria q ser falso)
else:
    print('Tipo de combustível inválido. Por favor, digite "e" ou "E"'
          ' para etanol ou "g" ou "G" para gasolina.')
#ou seja; se n for nenhum desses dois..(os dois é falso)

