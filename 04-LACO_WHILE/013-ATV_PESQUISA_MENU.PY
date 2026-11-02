import os
import time
os.system('cls')

soma_salarios = 0
quantidade = 0
maior_idade = 0
menor_idade = 0
mulheres_5000 = 0

while True:
    print('''      === MENU ===
    1 - Adicionar pessoa
    2 - Exibir resultados
    3 - Sair
    ''')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        idade = int(input('Idade: '))
        sexo = input('Sexo(M/F): ').upper()
        salario = float(input('Salário: R$'))

        soma_salarios += salario
        quantidade += 1

        if quantidade == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade

        if sexo == 'F' and salario >= 5.000:
            mulheres_5000 += 1

        print()
        input('Pressione qualquer tecla para apagar as respostas e continuar a pesquisa......')
        os.system('cls')

    elif opcao == '2':
        if quantidade == 0:
            print('Nenhuma pessoa cadastrada ainda.')
        else:
            media = soma_salarios / quantidade
            print(f'Média de salários: R$ {media:.2f}')
            print(f'Maior idade: {maior_idade}')
            print(f'Menor idade: {menor_idade}')
            print(f'Mulheres com salário a partir de R$5.000,00: {mulheres_5000}')

            print()
            input('Aperte qualquer tecla para apagar o menu...')
            os.system('cls')

    elif opcao == '3':
        print()
        print('Encerrando o programa......')
        time.sleep(1)
        os.system('cls')
        print('==FIM==')
        break

    else:
        print('Opção inválida, tente novamente.')