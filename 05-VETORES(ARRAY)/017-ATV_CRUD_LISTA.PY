import os
os.system('cls')

lista_series = []

while True:
    os.system('cls')
    print('''
==== MERCADINHO DENDEZEIROS ====
1 - Cadastrar serie
2 - Listar series
0 - Sair

''')
    
    opcao = int(input('Escolha uma opção: '))
    
    match opcao:
        case 1:
            print('\n== Cadastrar serie ==')
            serie = input('Digite o nome da serie: ').strip().upper()
            #.strip() Funciona retirando os espaços vazios no final.
            #.upper() Todas as letras maiúsculas.
            if serie == '':
              print('O nome não pode ficar vazio.')
            elif serie in lista_series:
              print(f'{serie} já está cadastrado.')
            else:
            # .append(serie) Adiciona o nome do serie na lista.
              lista_series.append(serie)
              print('Serie cadastrado com sucesso!')
            input('\nPressione qualquer tecla para continuar...')
        
        case 2:
            print('\n== Exibindo as series ==')
            if len(lista_series) == 0:
              print('O catálogo está vazio.')
            else:
              for i, serie in enumerate(lista_series):
                print(f'{i+1}. {serie}')
              
              #len(lista_series) mostra a quantidade de produtos na lista.
            print(f'Total de series cadastradas: {len(lista_series)}')
            input('\nPressione qualquer tecla para continuar...')
        
        case 0:
          print('==FIM==')
          break
        
        case _:
          print('Código inválido, tente novamente....')
          input('\nPressione qualquer tecla para continuar...')