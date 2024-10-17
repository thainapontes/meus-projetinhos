#Tabuada de um numero que o usuário escolher utilizando laço for
multiplicacao=0
numero=int(input('Digite um número: '))
for x in range(1,11):
    multiplicacao= numero * x
    print(f'{numero}x{x}= {multiplicacao}') #tem q estar dentro do for p exibir todos 