import os
os.system('cls')

def logo_senai():
    print('='*21)
    print('    SENAI - BAHIA  ')
    print('='*21)

def mostrar_dados(nome, email, telefone):
    print(f'Olá {nome}, Seja Bem-vindo! \nO clinte {nome} tem como telefone:{telefone} e tem como email registrado:{email}')

print()
logo_senai()
print('== SOLICITANDO DADOS ==')
nome = input('Digite seu nome: ').upper().strip()
email = input('Digite seu email: ').strip()
telefone = int(input('Digite seu telefone: '))

print()
logo_senai()
print('== EXIBINDO DADOS ==')
mostrar_dados(nome, email, telefone)