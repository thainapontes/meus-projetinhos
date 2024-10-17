alunos=['']*5
soma= 0 #variavel acumuladora
cont= 0 #variavel contadora
tam=len(alunos) #tb ajuda a atualizar os valores e otimizar o codigo em casos de alteraçoes
for posicao in range(tam):
    alunos[posicao]=float(input(f'Digite a nota do {posicao+1}º aluno:  ')) #o aluno tal em posiçao tal
for x in range(tam): #for para a soma da media
    soma=soma+alunos[posicao]
media=soma/tam
for i in range(tam): #for para saber os alunos q estao acima da media
    if alunos[i]>media:
        cont=cont+1
print(f'A média da turma é {media} e {cont} alunos ficaram com nota acima da média.')



