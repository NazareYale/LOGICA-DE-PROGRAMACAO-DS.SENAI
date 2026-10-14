import os
os.system('cls')

vetor_notas = []
QUANTIDADE_NOTAS = 3
for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f'Digite a sua {i +1}º nota: '))
    vetor_notas.append(notas)

#soma = sum(vetor_notas)#FUNCIONA SOMANDO TODOS OS NÚMEROS INFRORMADOS NO VETOR.
media = sum(vetor_notas) / QUANTIDADE_NOTAS

for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'A sua {posicao}º nota é: {nota}')
    #print(f'A soma das notas é: {soma}')

print(f'A sua média é: {media:.2f}')