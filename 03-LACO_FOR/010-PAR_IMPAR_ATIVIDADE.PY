import os
os.system('cls')

#CONSTANTE
quantidade = 5
pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        pares = pares + 1
#pares += 1 Outra forma de se fazer a operação feita da forma de cima, mas funcionando do mesmo jeito. Acrescentando mais um valor a variável depois da operção ter sido feita.
    else:
        impares = impares + 1

print(f'Quantidade de Pares: {pares}')
print(f'Quantidade de Ímpares: {impares}')

print('==FIM==')