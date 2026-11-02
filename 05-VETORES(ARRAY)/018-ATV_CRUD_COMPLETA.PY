import os
os.system('cls')

lista_produtos = []

while True:
    print('''
=== MERCADINHO DENDEZEIROS ====

1- Cadastrar produto
2- Listar todos os produtos
3- Atualizar produto
4- Remover produto
5- Buscar produto
0- Sair
''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:
        
        case 1:
        #CREATE (INSERIR)
            print('\n== CADASTRAR PRODUTO ==')
            nome_produto = input('Digite o nome do novo produto: ').strip().upper()
            if nome_produto == '':
                print('o nome do produto deve ser inserido....')
            elif nome_produto in lista_produtos:
                print('Produto já cadastrado.')
            else:
                lista_produtos.append(nome_produto)
                print('Produto cadastrado com sucesso!')

        case 2:
        #READ (LER/CONSULTAR/BUSCAR)
            print('\n== PRODUTOS NO ESTOQUE ==')
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'Total: {len(lista_produtos)}')

        case 3:
        #UPDATE (ATUALIZAR)
            print('==\n ATUALIZAR PRODUTO ==')
            nome = input('Qual produto deseja atualizar?: ').strip().upper()
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('novo nome: ').strip().upper()
                lista_produtos[posicao] = novo
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado.')

        case 4:
        #DELETE (REMOVER)
            print('\n== REMOVER PRODUTO ==')
            nome = input('Qual produto deseja remover?: ').strip().upper()
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('Produto excluído com sucesso!')
            else:
                print('Produto não encontrado.')

        case 5:
        #FILTRAR
        #READ (LER/CONSULTAR/BUSCAR)
            print('== ENCONTRAR PRODUTO ==')
            nome = input('Qual produto deseja buscar?: ').strip().upper()
            if nome in lista_produtos:
                print('Produto encontrado!')
            else:
                print('Este produto não está no estoque.')

        case 0:
            print('Saindo do programa.....')
            break
        
        case _:
            print('\nOpção inválida! \nTente novamente....')

    input('Pressione uma tecla para continuar....')
    os.system('cls')