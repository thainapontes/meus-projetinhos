time1=input('Digite um time: ' )
time2=input('Digite um time: ' )
gol1=int(input(f'Quantidade de gols marcados do {time1}: '))
gol2=int(input(f'Quantidade de gols marcados: do {time2}: '))
if gol1==gol2:
    print(f'O {time1} e o {time2} estão empatados.')
else:
    if gol1>gol2:
        print(f'O vencedor é o {time1}.')
    else:
        print(f'O vencedor é o {time2}.')