#Programa que calcule a soma entre todos os números ímpares
#que são múltiplos de 3 e que se encontram no intervalo de 1 até 500
soma=0
for x in range(1,500+1):
    if x%2==1 and x%3==0:
        soma=soma+x
        print(x) #aqui dentro ele mostra todos os números impares e multiplos de 3
print(soma) #aqui ele mostra a soma desses numeros
print(x) #aqui ele mostra o ultimo indice pq esta fora do for!
