soma=0
alunossala=int(input('Digite a quantidade de alunos na turma: '))
for alunossala in range(1,alunossala+1): #o +1 é pq ta partindo do 1
    notasalunos= float(input(f'Digite a nota do aluno: '))
    soma=soma + notasalunos
media= soma/alunossala #é necessario ficar fora do for para dar o resultado final total
print(f'A média da turma é {media:.2f}.')