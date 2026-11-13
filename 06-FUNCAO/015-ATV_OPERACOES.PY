import os
os.system('cls')


def calcular_soma(numero1 , numero2):
    soma = (numero1 + numero2)
    return soma

def calcular_subtracao(numero1 , numero2):
    subtracao = (numero1 - numero2)
    return subtracao

def calcular_divisao(numero1 , numero2):
    if numero2 == 0:
        return 'Atenção! Divisão por zero.'
    return numero1 / numero2

def calcular_multiplicacao(numero1 , numero2):
    multiplicacao = (numero1 * numero2)
    return multiplicacao

print('= SOLICITANDO NÚMEROS =')
numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a segunda nota: '))


soma = calcular_soma(numero1, numero2)
subtracao = calcular_subtracao(numero1, numero2)
divisao = calcular_divisao(numero1, numero2)
multiplicacao = calcular_multiplicacao(numero1, numero2)

print('\n= EXIBINDO NOTAS =')
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Divisão: {divisao:.2f}')
print(f'Multiplicação {multiplicacao:.2f}')