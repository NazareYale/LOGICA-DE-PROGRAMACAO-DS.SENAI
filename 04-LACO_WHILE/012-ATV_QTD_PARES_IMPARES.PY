import os
os.system('cls')

qtd_pares = 0
qtd_impares = 0
soma_pares = 0
soma_total = 0

while True:
    numero = int(input('Digite um inteiro positivo (0 para encerrar): '))

    if numero == 0:
        break

    soma_total += numero

    if numero % 2 == 0:
        qtd_pares += 1
        soma_pares += numero
    else:
        qtd_impares += 1

total = qtd_pares + qtd_impares
media_pares = soma_pares / qtd_pares
media_total = soma_total / total
print(f'Quantidade de pares: {qtd_pares}')
print(f'Quantidade de ímpares: {qtd_impares}')

if qtd_pares > 0:
    print(f'Média dos pares: {media_pares}')
else:
    print('Média dos pares: não há números pares.')

if total > 0:
    print(f'Média geral: {media_total}')
else:
    print('Média geral: nenhum número foi informado.')