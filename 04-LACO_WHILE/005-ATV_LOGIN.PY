import os
import time
os.system('cls')

login = 'Nazza'
senha = '@1234'

while True:
    login = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    
    if login != 'Nazza' or senha != '@1234':
        print()
        print('Login ou Senha incorretos, tente novamente.')
        print()
        time.sleep(2)
        os.system('cls')
        #input('Pressione uma tecla para continuar.....')
# Uma outra forma para se apagar o terminal sem ser com o time.sleep
    else:
        print()
        print(f'Bem-vindo {login}!')
        break
