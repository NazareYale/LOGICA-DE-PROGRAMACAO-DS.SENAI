import os
os.system('cls')

lista_pacientes = []

while True:

    print('''
=== MENU PARA PACIENTES ===
1-Cadastrar paciente
2-Listar pacientes
3-Atualizar paciente
4-Excluir paciente
0-Sair

''')
    opcao = int(input('Digite a opção escolhida: '))

    match opcao:

        case 1:
            print('=CADASTRANDO PACIENTE=')
            paciente = input('Digite o seu nome completo: ').strip().upper()
            if paciente == '':
                print('O nome não podem ficar em branco! Por favor responda.')
            elif paciente in lista_pacientes:
                print(f'{paciente} já está cadastrado.')
            else:
                lista_pacientes.append(paciente)
                print('Paciente cadastrado com sucesso!')

        case 2:
            print('=LISTANDO PACIENTES=')
            for posicao, paciente in enumerate(lista_pacientes, start=1):
                    print(f'{posicao}º) {paciente}')
            print(f'Total de pacientes cadastrados: {len(lista_pacientes)}')
            
        case 3:
            print('=ATUALIZANDO LISTA DOS PACIENTES=')
            nome = input('Qual paciente deseja atualizar?: ').strip().upper()
            if nome in lista_pacientes:
                posicao = lista_pacientes.index(nome)
                novo = input('Digite o novo nome: ').strip().upper()
                lista_pacientes[posicao] = novo
                print('Paciente alterado com sucesso!')
            else:
                print('Paciente não encontrado.')

        case 4:
            print('=EXCLUÍNDO PACIENTES=')
            nome = input('Digite o nome do paciente que deseja remover: ').strip().upper()
            if nome in lista_pacientes:
                lista_pacientes.remove(nome)
                print('Paciente removido com sucesso!')
            else:
                print('Paciente não encontrado.')


        case 0:
            print('Finalizando o programa....')
            break

        case _:
            print('\nOpção inválida!\nTente novamente....')

    input('Aperte uma tecla para continuar....')
    os.system('cls')