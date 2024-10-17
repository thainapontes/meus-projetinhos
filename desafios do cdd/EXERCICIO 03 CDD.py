menu=0
nomeuser=[] #lista
senhauser=[] #lista
tentativa=0

while menu!=4:
    menu= int(input('Escolha uma ação:\n'
           '1- Para realizar o cadastro\n'
           '2- Para encontrar usuários\n'
           '3- Para efetuar o login\n'
           '4-Sair\n'
           ''))

    if menu==1: #cadastro de usuários. Não precisa usar o for, pois a intenção é cadastrar uma unica vez por ação.
        nome=input('Cadastre seu nome de usuário: ') #nome é uma variavel temporaria
        senha=input('Cadastre sua senha: ') #senha é uma variavel, n pode ser a senhauser pq é uma lista
        nomeuser.append(nome)
        senhauser.append(senha)
        print('Cadastro realizado com sucesso!')


    elif menu==2: #usa o elif para otimizar inves do if, q seria desnecessario
        if nomeuser: #verifica se há usuarios cadastrados
            print('Usuários cadastrados: ')
            for nome in nomeuser: #percorre a lista nomeuser e cada iteração armazena na variavel nome
                print(nome)# imprime cada nome de usuario
        else:
            print('Nenhum usuário cadastrado.')

    elif menu==3:
        while tentativa<3:
            nome=input('Digite seu nome de usuário: ')
            if nome in nomeuser:
                senha=input('Digite sua senha: ')
                indice=nomeuser.index(nome)
                if senha==senhauser[indice]:
                     print('Login efetuado com sucesso!')
                     break #para sair do loop de tentativas

                else:
                    print('Senha inválida.')
            else:
                print('Usuário não encontrado.')
            tentativa=tentativa+1
        if tentativa==3:
            print('Acesso bloqueado após 3 tentativas.')

    elif menu==4:
        print('Saindo...')
    else:
        print('Escolha uma opção válida: ')

