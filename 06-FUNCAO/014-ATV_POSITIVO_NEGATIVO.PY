import os
os.system('cls')

def verificar_positivo_negativo(numero):
    if numero > 0:
        resultado = 'Positivo.'
    elif numero < 0:
        resultado = 'Negativo.'
    else:
        resultado = 'Neutro.'
    return(resultado)

print('= SOLICITANDO NÚMEROS =')
numero = int(input('Digite um número: '))

resultado = verificar_positivo_negativo(numero)

print('\n= EXIBINDO NÚMEROS  =')
print(f'O número {numero} é {resultado}')