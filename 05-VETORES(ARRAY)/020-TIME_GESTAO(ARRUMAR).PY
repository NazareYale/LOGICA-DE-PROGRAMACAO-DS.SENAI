import os
os.system('cls')

lista_jogadores = []
jogador = 0
posicao = 0
camisa = 0

while True:

    print('''
1. Cadastrar jogador
2. Listar jogadores
3. Atualizar jogador
4. Excluir jogador
0. Sair
''')

    opcao = int(input('Digite a opção escolhida: '))
    
    match opcao:

        case 1:
            print('=CADASTRANDO JOGADOR=')
            jogador = input('Digite o seu nome: ').strip().upper()
            posicao = input('Digite a sua posição: ').strip().upper()
            camisa = int(input('Digite o número da camisa: '))
            if jogador == '':
                print('O nome não pode ficar em branco! Por favor responda.')
            elif jogador in lista_jogadores:
                print(f'{jogador} já está cadastrado.')
            else:
                lista_jogadores.append(jogador)
                print('Jogador cadastrado com sucesso!')

        case 2:
            print('=LISTANDO ELENCO=')
            for i, jogador in enumerate(lista_jogadores, start=1):
                print(f'{i}º) {jogador} | {posicao} | CAMISA {camisa}')
            print(f'Total de jogadores cadastrados: {len(lista_jogadores)}')

        case 3:
            print('=ATUALIZANDO A LISTA DOS JOGADORES=')
            nome = input('Qual jogador deseja atualizar?: ').strip().upper()
            if nome in lista_jogadores:
                posicao = lista_jogadores.index(nome)
                novo = input('Digite o novo nome: ').strip().upper()
                novo = input('Digite a nova posição: ').strip().upper()
                novo = int(input('Digite a nova camisa: '))
                lista_jogadores[posicao] = novo
                print('Jogador alterado com sucesso!')
            else:
                print('Jogador não encontrado.')

        case 4:
            print('=EXCLUÍNDO JOGADORES=')
            nome = input('Digite o nome do jogador que deseja remover: ').upper().strip()
            if nome in lista_jogadores:
                lista_jogadores.remove(nome)
                print('Jogador removido com sucesso!')
            else:
                print('Jogador não encontrado.')
        
        case 0:
            print('Finalizando o programa.....')
            break

        case _:
            print('\nInválido!\nTente novamente....')
        
    input('Aperte qualquer tecla para continuar....')
    os.system('cls')