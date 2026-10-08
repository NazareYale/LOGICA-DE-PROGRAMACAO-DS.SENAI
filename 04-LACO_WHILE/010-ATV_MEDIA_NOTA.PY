import os
os.system('cls')


soma = 0
contador = 0

while True:
    nota = float(input('Digite a sua nota: '))
    soma += nota
    contador = contador + 1

    resposta = input('Deseja inserir mais uma nota?(S/N): ')

    if resposta.upper() == 'N':
        break

media = soma / contador
print(f'Quantidade de notas informadas: {contador}')
print(f'A sua média é: {media:.2f}')