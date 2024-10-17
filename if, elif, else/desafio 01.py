hora01= int(input(' Digite a hora: '))
minuto01= int(input('Digite o minuto: '))
hora02= int(input(' Digite a hora: '))
minuto02= int(input('Digite o minuto: '))
calculo01= (minuto01 + minuto02)//60 #tá pegando a hora q dá entre os dois
calculo02= (minuto01 + minuto02)%60 # tá pegando os minutos, divididndo por 60(hr) e pegando
# o que resta dos  minutos e guardando
calculo03= hora01+ hora02 + calculo01 - 24 #tá juntando todas as horas
if calculo03 < 0:
    calculo03 *= -1
if calculo03 > 12:
    calculo03 -=12
print(f' entrada 1: {hora01} : {minuto01}')
print(f' entrada 1: {hora02} : {minuto02}')
print(f' saída: {calculo03} : {calculo02} ')