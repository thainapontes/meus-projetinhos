#usando array como lista
lista= [''] * 5
tam=len(lista) #precisa disso pq o for so aceita numeros e a lista é stinger
for i in range(tam):
    nomes=input(f"Digite o nome do {i+1}º aluno:  ")
    lista[i]=nomes
print(lista)

