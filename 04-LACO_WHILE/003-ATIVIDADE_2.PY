import os
os.system('cls')

while True:
    primeira_nota = float(input('Digite a sua 1º nota: '))
    segunda_nota = float(input('Digite a sua 2º nota: '))
    media = (primeira_nota + segunda_nota) / 2
    if primeira_nota or segunda_nota < 0:
        print()
        print('Nota inválida, digite novamente')
        print()
    elif primeira_nota or segunda_nota > 10:
        print()
        print('Nota inválida, digite novamente')
        print()
    elif media >= 7:
        print('Aprovado!')
    elif media <= 6:
        print('Reprovado.')
    break

