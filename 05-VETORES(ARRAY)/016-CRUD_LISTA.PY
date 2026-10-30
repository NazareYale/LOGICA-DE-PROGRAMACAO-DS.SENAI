import os
os.system('cls')

lista_produtos = []

while True:
    os.system('cls')
    print('''
==== MERCADINHO DENDEZEIROS ====
1 - Cadastrar produtos
2 - Listar produtos
0 - Sair

''')
    
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:
        case 1:
            print('\n== Cadastrar um produto ==')
            produto = input('Digite o nome do produto: ').strip().upper()
            #.strip() Funciona retirando os espaços vazios no final.
            #.upper() Todas as letras maiúsculas.
            if produto == '':
              print('O nome não pode ficar vazio.')
            elif produto in lista_produtos:
              print(f'{produto} já está cadastrado.')
            else:
            # .append(produto) Adiciona o nome do produto na lista.
              lista_produtos.append(produto)
              print('Produto cadastrado com sucesso!')
            input('\nPressione qualquer tecla para continuar...')
        
        case 2:
            print('\n== Exibindo produtos ==')
            if len(lista_produtos) == 0:
              print('O estoque está vazio.')
            else:
              for i, produto in enumerate(lista_produtos):
                print(f'{i+1}. {produto}')
              
              #len(lista_produtos) mostra a quantidade de produtos na lista.
            print(f'Total de produtos: {len(lista_produtos)}')
            input('\nPressione qualquer tecla para continuar...')
        
        case 0:
          print('==FIM==')
          break
        
        case _:
          print('Código inválido, tente novamente....')
          input('\nPressione qualquer tecla para continuar...')