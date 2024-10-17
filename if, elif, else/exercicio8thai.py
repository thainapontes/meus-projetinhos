n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))
media= (n1+n2+n3)/3
if media>=7:
    print(f'Aprovado!, sua média é {media:.2f}.')
else:
   if media>4:
       print(f'Você fará a prova de recuperação,'
             f' sua média é {media:.2f}.')
   if media<4:
       print(f'Reprovado! sua média é {media:.2f}.')
#Se for menor que 7 e maior que 4, ficará de recuperação. Se ficar abaixo de 4, será reprovado.
#Já que depois do if media>=7, o else já diz que o que vem é menor que 7, por isso, não é necessário fazer 4<media<7.