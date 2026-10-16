import os
os.system('cls')

vetor_numeros = []
negativos = 0
soma_positivos = 0
QUANTIDADE_LOOPS = 5

for i in range(QUANTIDADE_LOOPS):
    numeros = int(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numeros)

    if numeros < 0:
        negativos += 1
    else:
        soma_positivos += numeros

print()
print(f'Soma dos positivos: {soma_positivos}')
print(f'Quantidade de negativos: {negativos}')