import os
os.system('cls')

soma = 0

for i in range(1,5):
    notas = float(input(f'Digite a sua {i}º nota: '))
    soma += (notas) / 4
print(f'A média das notas é: {soma}')
