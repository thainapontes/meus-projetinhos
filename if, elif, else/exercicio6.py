altura=float(input('Informe sua altura: '))
peso=float(input('Informe seu peso:  '))
imc=peso/altura**2
if imc<=18.5:
    print('Você está abaixo do peso')
elif imc>= 18.6 and imc<25:
    print('Seu peso está ideal! Parabéns!')
elif imc>=25 and imc<30:
    print('Você está levemente acima do peso.')
elif imc>= 30 and  imc<35:
    print('Obesidade grau I.')
elif imc>=35 and imc<40:
    print('Obesidade grau II (severa).')
elif imc>=40:
    print('Obesidade grau III (mórbida). Você vai morrer se não se cuidar.')


 #match imc:
    #case imc <= 18.5:
