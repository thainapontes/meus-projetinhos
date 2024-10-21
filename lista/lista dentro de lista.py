teste=[]
teste.append('Thai Pontes')
teste.append(18)
galera=[]
galera.append(teste[:])
print(galera)

galera=[['João',19], ['Ana', 33], ['Thainá',18],['Gustavo',29]]
print(galera[3][1])
for pessoa in galera: #para cada pessoa na lista galera..
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')