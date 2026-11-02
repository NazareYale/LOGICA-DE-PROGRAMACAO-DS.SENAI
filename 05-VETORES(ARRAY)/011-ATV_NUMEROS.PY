import os
os.system('cls')

QUANTIDADE_LEITURAS = 5
vetor_numeros = []
maior_numero = 0
menor_numero = 9999

for i in range(QUANTIDADE_LEITURAS):
    numeros = float(input(f'Digite o seu {i+1}º número: '))
    vetor_numeros.append(numeros)

maior_numero = max(vetor_numeros)
menor_numero = min(vetor_numeros)

for posicao, numeros in enumerate(vetor_numeros, start=1):
    print(f'\nO seu {posicao}º número é: {numeros}')

print(f'\nO menor número é: {menor_numero}')
print(f'O maior número é: {maior_numero}')