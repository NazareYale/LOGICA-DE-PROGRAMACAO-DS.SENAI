import os
os.system('cls')

while True:
    nota = float(input('Digite sua nota: '))
    if nota < 0 or nota > 10:
        print()
        print('Nota inválida, digite novamente.')
        print()
    if nota >= 7:
        print(f'A sua nota é: {nota}')
        print('Aprovado!')
    elif nota <= 6:
        print(f'A sua nota é: {nota}')
        print('Reprovado.')
    else:
        print()
        print(f'A sua nota é: {nota}')
    break