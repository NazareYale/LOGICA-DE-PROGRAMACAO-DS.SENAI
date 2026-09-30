import os
import time
os.system('cls')

media = 0

#ENTRADA E PROCESSAMENTO
print('=Solicitando Notas=')
for i in range(1,5):
    notas = float(input(f'Digite a sua {i}º nota: '))
    media += (notas) / 4

#SAÍDA
print(f'\nGerando resultado...')
time.sleep(1)
print(f'Sua média é: {media}')

#OUTRA FORMA DE SE FAZER O CÓDIGO DE CIMA.
#ENTRADA
#print('=Solicitando Notas=')
#QUANTIDADE_NOTAS = 4
#soma_notas = 0.0

#for i in range(QUANTIDADE_NOTAS):
#    soma_notas = float(input(f'Digite a sua {i}º nota: '))

#PROCESSAMENTO
#media = soma_notas / QUANTIDADE_NOTAS

#SAÍDA
#print(f'\nGerando resultado...')
#print(f'Sua média é: {media}')