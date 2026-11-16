import os
os.system('cls')

def conversor(metros):
    resultado = metros * 10
    return resultado


metros = float(input('Digite um valor em metros: '))

resultado = conversor(metros)

print(f'\nO valor em metros é: {metros}')
print(f'O valor convertido para centímetro é: {resultado}')