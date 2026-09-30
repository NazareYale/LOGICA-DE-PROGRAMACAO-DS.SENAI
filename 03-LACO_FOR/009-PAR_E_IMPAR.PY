import os
import time
os.system('cls')

#print('MOSTRANDO OS NÚMEROS PARES ENTRE 1 ATÉ 10.')
#for i in range(1,11):
#    if i % 2 ==0:
#        print(f'{i} é par.')

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'{numero} é par.')
else:
    print(f'{numero} é ímpar.')