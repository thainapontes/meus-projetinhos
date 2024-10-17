nomeuser=['']*5
senhauser=['']*5
tam=len(nomeuser)#pega so de um pq o tamamho é igual
for i in range(tam):#for para preencher
    nomeuser[i]= input('Digite seu nome de usuário: ')
    senhauser[i] = int(input('Digite sua senha: '))
for x in range(tam):# for para percorrer
    print(f'Olá,{nomeuser[x]}, sua posição é {x}º e sua senha é {senhauser[x]}.')#n coloca o i pq o i esta travado
#no ultimo indice e n vai dar certo.

#fazer um menu = 1- cadastro 2-mostrar usuarios cadastrados 3- login no sistema  e so vale 3 tentativas 4 - sair do sistema
#falar qnd a sdenha ta errada, falar qnd o usuario n encontrado e etc


