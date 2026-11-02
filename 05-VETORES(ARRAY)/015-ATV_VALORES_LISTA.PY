import os
os.system('cls')

vetor_numeros = []
QUANTIDADE_LOOPS = 5

print('==SOLICITANDO DADOS==')
for i in range(QUANTIDADE_LOOPS):
    numero = int(input(f'Digite o {i+1}º número: '))

    if numero < 0:
        numero = 0

    vetor_numeros.append(numero)
    
print('\n==EXIBINDO DADOS==')
for posicao, numero in enumerate(vetor_numeros, start=1):
    print(f'\n{posicao}º) {numero}')