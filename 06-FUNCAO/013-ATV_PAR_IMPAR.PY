import os
os.system('cls')

def verificar_par_impar(numero):
    if numero % 2 == 0:
        resultado = 'par.'
    else:
        resultado = 'ímpar.'
    return(resultado)

print('= SOLICITANDO NÚMEROS =')
numero = int(input('Digite um número: '))

resultado = verificar_par_impar(numero)

print('\n= EXIBINDO NÚMEROS =')
print(f'O número {numero} é {resultado}')
