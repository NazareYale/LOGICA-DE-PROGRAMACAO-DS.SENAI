import os
os.system('cls')
import time

soma = 0
for i in range(5):
    numero = int(input('Digite um número:'))
    soma = numero + soma

time.sleep(1)
print(f'RESULTADO: {soma}')
time.sleep(0.5)
print('==FIM==')

