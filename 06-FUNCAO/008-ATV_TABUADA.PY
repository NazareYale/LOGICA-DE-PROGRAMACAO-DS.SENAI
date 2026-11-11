import os
os.system('cls')

def mostrar_tabuada():
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

print('= SOLICITANDO DADOS =')
numero = int(input('Digite um número para tabuada: '))

print('= EXIBINDO DADOS =')
mostrar_tabuada(numero)