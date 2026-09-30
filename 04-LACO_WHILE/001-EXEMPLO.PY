import os
os.system('cls')

while True:
    numero = int(input('Digite um número entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print() #PULAR UMA LINHA
        print('Número inválido, tente novamente!')
    else:
        print() #ASSIM COMO O \N
        print('O número está entre 1 e 10.')
        break #SERVE PARA PARAR O LAÇO DE REPETIÇÃO.

print('=FIM=')