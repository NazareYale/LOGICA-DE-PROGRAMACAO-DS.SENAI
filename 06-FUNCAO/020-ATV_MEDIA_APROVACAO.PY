import os
os.system('cls')

LOOPS = 2

def media_notas(nota):
    soma = nota * 2
    media = soma / LOOPS
    return media

#def valor_notas(nota):
#    if nota >10 or nota <0:
#        print('Inválido!\nReinicie para continuar.')

def aprovacao_notas(nota):
    if nota >= 7:
        resultado = 'Aprovado!'
    else:
        resultado = 'Reprovado.'
    return resultado

lista_notas = []

for i in range(LOOPS):
    while True:
        nota = float(input('Digite a sua nota: '))
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:
            print('Nota inválida, tente novamente!\n')

media = media_notas(nota)

resultado = aprovacao_notas(nota)

#valor_notas(nota)

print(f'A sua média é: {media}')
print(f'O resultado é: {resultado}')