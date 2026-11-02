import os
os.system('cls')

QUANTIDADE_LEITURAS = 6
vetor_numeros = []
par = 0
impar = 0

for i in range(QUANTIDADE_LEITURAS):
    numeros = float(input(f'Digite o seu {i+1}º número: '))
    vetor_numeros.append(numeros)
    if numeros % 2 == 0:
        par += 1
    else:
        impar += 1


for posicao, numeros in enumerate(vetor_numeros, start=1):
    print(f'\nO seu {posicao}º número é: {numeros}')



print(f'\nQuantidade de pares: {par}.')
print(f'Quantidade de ímpares: {impar}')
