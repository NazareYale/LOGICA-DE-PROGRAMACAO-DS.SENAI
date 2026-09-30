import os
os.system('cls')
#inicia a variável soma com zero.
#Para evitar dar erro quando acumular os valores na variável
soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}º nota entre 1 e 10: '))
        if nota < 0 or nota > 10:
            print()
            print('Nota inválida, tente novamente!')
            print()
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print(f'Média: {media}')
print('==FIM==')
