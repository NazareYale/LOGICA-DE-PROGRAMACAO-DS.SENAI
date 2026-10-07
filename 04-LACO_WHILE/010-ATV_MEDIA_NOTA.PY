import os
os.system('cls')

VALOR_NOTAS = 7
QUANTIDADE_NOTAS = 2



media = SOMA / QUANTIDADE_NOTAS

while True:
    nota = str(input('Deseja inserir outra nota(S/N)?')).lower()
    if nota == 'S' or 's':
        new_nota = float(input('Insira a nova nota: '))
        VALOR_NOTAS += new_nota
        print(f'A média é: {media}')
    elif nota == 'N' or 'n':
        print(f'A média é: {media}')
    break