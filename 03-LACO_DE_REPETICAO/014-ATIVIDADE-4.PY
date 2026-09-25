import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL.')
soma = 0

print(f'Valor INICIAL da variável soma: {soma}')

for i in range(5):
    numero = int(input(f'\nDigite um número para se somar: '))
    soma += numero
    print(f'\nValor TEMPORÁRIO da variável soma: {soma}')
#soma += int(input('Digite um número para somar: '))
#UMA FORMA MAIS SIMPLES DE SE FAZER A MESMA OPERAÇÃO DE CIMA, FUNCIONANDO DO MESMO JEITO. A ÚNICA COISA QUE MUDOU FOI O NOME DA VARIÁVEL QUE MUDOU DE NUMERO PARA SOMA PARA QUE O CÓDIGO FUNCIONE.

print(f'\nValor FINAl da variável soma: {soma}')
