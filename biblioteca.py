def imprimir_nome(nome):
    print(f'O nome é: {nome}')
def imprimir1_a_5(n):
    for i in range(1,n+1):
        print(i)

def somar(n1,n2,n3,n4,n5):
    soma=n1+n2+n3+n4+n5
    print(f'{n1}+{n2}+{n3}+{n4}+{n5}={soma}')

def somar2(*numeros): #tupla, assim é p independente do q vc receber(vc n sabe) ela vai somar
    soma = 0
    for x in numeros:
        soma=soma+x
    print(soma)

def somar_letras(texto):
    tam=len(texto)
    cont=0
    for i in range(tam):
        if texto[i] != ' ': #poderia usar tb o " if x not in ' ' " (se o x n estiver em)
            cont=cont+1
    print(f' O texto tem {cont} letras.')
    for x in range(tam-1,-1,-1): #for para ficar ao contrario
       print(texto[x],end= '')

def lista(*listaunica):
    nova_lista=[]
    for x in listaunica:
        print(x,end=' ')
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

def numero_primo(numero):
    if (numero==1):
        return numero,"Não é primo"
    elif (numero==2):
        return numero, "É primo."
    else:
        for x in range(2,numero):
            if(numero%x==0):
                return numero, "Não é primo."
                return numero, "É primo"

def viacep(cep):
    import requests
    cep=(input("Qual o cep?"))
    if len(cep)==8:
        link=f'https://viacep.com.br/ws/{cep}/json'
        requisicao=requests.get(link)
        print(requisicao)
        dic_requisicao=requisicao.json()
        uf=dic_requisicao['uf']
        cidade=dic_requisicao['localidade']
        bairro=dic_requisicao['bairro']
        print(dic_requisicao)
    else:
        print("CEP INVÁLIDO.")