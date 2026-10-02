import os
os.system('cls')

print('= TELA PARA CADASTRO =')
login_cadastrado = input('Digite o seu login: ')
senha_cadastrada = input('Digite a sua senha: ')

while True:
    os.system('cls')
    print('= TELA PARA LOGIN =')
    login_informado = input('Digite o seu login: ')
    senha_informada = input('Digite a sua senha: ')

    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        print()
        print(f'Bem-Vindo {login_cadastrado}!!')
        break
    else:
        print()
        print('Login ou senha inválidos! \nTente novamente.')
        print()
        input('Pressione qualquer tecla para reiniciar o login.....')