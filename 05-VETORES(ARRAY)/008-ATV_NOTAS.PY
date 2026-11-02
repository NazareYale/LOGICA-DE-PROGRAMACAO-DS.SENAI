import os
os.system('cls')

vetor_notas = []
QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f'Digite a sua {i +1}º nota: '))
    vetor_notas.append(notas)

soma += notas
media = soma / QUANTIDADE_NOTAS

for indice, resultados in enumerate(vetor_notas, start=1):
    print(f'A sua {indice}º nota é: {resultados}')
    print(f'A sua média é: {media}')