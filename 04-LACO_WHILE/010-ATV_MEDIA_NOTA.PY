import os
os.system('cls')

VALOR_NOTAS = 7
QUANTIDADE_NOTAS = 2
LOOPS = 3

media = (VALOR_NOTAS * 2) / QUANTIDADE_NOTAS

while True:

    for i in range(LOOPS):
        nota = str(input('Deseja inserir outra nota(S/N)?')).lower()
        if nota == 'S' or 's':
            new_nota = float(input('Insira a nova nota: '))
            VALOR_NOTAS += new_nota
            media = input(f'A média é: {media}')
        break
    if nota == 'N' or 'n':
        media = input(f'A média é: {media}')
    break

