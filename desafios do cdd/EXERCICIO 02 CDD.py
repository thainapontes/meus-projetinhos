tentativas=0
senha=1234
while tentativas<3: #não precisa do for pois o while já toma conta das repetições naturalmente sem redundancias
    senhauser = int(input('Digite sua senha: '))
    if senhauser==senha:
        print('Acesso liberado.')
        break

    else:
        tentativas=tentativas+1
        if tentativas<3:
            print('Senha incorreta, digite sua senha novamente: ')#n precisa colocar um input, já q o codigo volta do incio pedindo a senha dnv
        else:
            print('Acesso bloqueado')



