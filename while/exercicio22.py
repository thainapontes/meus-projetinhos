pergunta=1
while pergunta==1:
    nota1 = float(input('Digite a primeira nota: '))
    while nota1<0 or nota1>10:
        nota1= float(input('Nota inválida. Digite novamente: '))
    nota2 = float(input('Digite a segunda nota: '))
    while nota2<0 or nota2>10:
        nota2=float(input('Nota inválida. Digite novamente: '))
    calculo= (nota1+nota2)/2
    print(f'A média desse aluno é {calculo}.')
    pergunta= int(input('Deseja fazer outro cálculo?\nDigite 1 para sim e 2 para não.\n'))
if pergunta==2:
    print('Fim.')


