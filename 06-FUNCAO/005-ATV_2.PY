import os
import time
os.system('cls')

def logo_senai():
    print('='*21)
    print('    SENAI - BAHIA  ')
    print('='*21)

def menu():
    print('''
===== MENU =====
1 - CADASTRAR CLIENTE
2 - MOSTRAR DADOS
3 -SAIR
''')
    

def mostrar_dados(nome, email, telefone):
    print(f'Olá {nome}, Seja Bem-vindo! \nO clinte {nome} tem como telefone:{telefone} e tem como email registrado:{email}')

while True:
    print()
    logo_senai()
    menu()
    opcao = int(input('Digite a opção escolhida: '))

    match opcao:
        case 1:
            print()
            logo_senai()
            print('== SOLICITANDO DADOS ==')
            nome = input('Digite seu nome: ').upper().strip()
            email = input('Digite seu email: ').strip()
            telefone = int(input('Digite seu telefone: '))
        
        case 2:
            print()
            logo_senai()
            print('== EXIBINDO DADOS ==')
            mostrar_dados(nome, email, telefone)
        
        case 3:
            print('Finalizando o programa...')
            time.sleep(1)
            break

        case _:
            print('Inválido!\nTente novamente.')
    
    input('Pressione qualquer tecla para continuar...')
    os.system('cls')
