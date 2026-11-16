import os
os.system('cls')

LOOPS = 3
vetor_notas = []

def calcular_notas(vetor_notas):
    #soma = sum(vetor_notas)
    #resultado = soma / 3
    return sum(vetor_notas) / len(vetor_notas)

def mostrar_notas(media, vetor_notas):
    print('= EXIBINDO NOTAS =')
    for nota in vetor_notas:
        print(f'Nota: {nota}')
    print(f'\nA sua média é: {media:.2f}')


for i in range(LOOPS):
    nota = float(input(f'Digite a sua {i+1}º nota: '))
    vetor_notas.append(nota)

media = calcular_notas(vetor_notas)

mostrar_notas(media, vetor_notas)