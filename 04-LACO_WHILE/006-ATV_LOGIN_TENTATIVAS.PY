import os
os.system('cls')

login = 'Nazza'
senha = '@1234'
tentativas = 1

while True:
    if tentativas <=3:
        print(f'Tentativa: {tentativas}:')
        login = input('Digite o login: ')
        senha = input('Digite a senha: ')
        tentativas += 1

        if login == 'Nazza' and senha == '@1234':
            print(f'Bem-vindo {login}!')
            break
        else:
            print('Login ou Senha incorretos, tente novamente.')
            print()
            input('Pressione uma tecla para continuar......')
            os.system('cls')
    else:
        print('==FIM==')
        break