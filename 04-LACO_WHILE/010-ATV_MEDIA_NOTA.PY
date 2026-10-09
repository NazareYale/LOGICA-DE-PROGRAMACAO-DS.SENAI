import os
os.system('cls')

soma = 0
quantidade_notas = 0

while True:
    os.system('cls')
    print('''    === MENU===
S - Inserir nota
N - Calcular Média''')
    
    resposta = input('Deseja inserir uma nota: ').lower()


    match resposta:
        case 's':
            nota = float(input('Digite sua nota: '))
            soma += nota
            quantidade_notas += 1
        case 'n':
            break
        
        case _:
            print('Opção inválida!')
            input('Pressione qualquer tecla para continuar.....')


if quantidade_notas == 0:
    print('Não foram inseridas notas. \n')
else:
    media = soma / quantidade_notas
    print(f'Média: {media}')