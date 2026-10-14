import os
os.system('cls')

QUANTIDADE_NOTAS = 4
vetor_notas = []


for i in range(QUANTIDADE_NOTAS):
    notas =  float(input(f'Digite a sua {i+1}º nota: '))
    vetor_notas.append(notas)

media = sum(vetor_notas) / QUANTIDADE_NOTAS

for posicao, notas in enumerate(vetor_notas, start=1):
    print()
    print(f'A sua {posicao}º nota é: {notas}')

print(f'\nA sua média é: {media}')
if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Em recuperação.')
else:
    print('Reprovado!')