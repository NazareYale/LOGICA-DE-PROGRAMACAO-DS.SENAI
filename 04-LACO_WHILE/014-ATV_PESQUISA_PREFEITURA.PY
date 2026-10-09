import os
import time
os.system('cls')

total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print('''    ===== MENU =====
1 - Adicionar família
2 - Sair e exibir resultados
    ''')

    opcao = input('Escolha uma opção: ') 

    if opcao == '1':
        print()
        os.system('cls')
        print('===== CADASTRO =====')
        salario = float(input('Salário da família: R$'))
        filhos = int(input('Número de filhos: '))

        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario

        print()
        input('Pressione qualquer tecla para apagar as respostas e continuar a pesquisa......')
        os.system('cls')

    elif opcao == '2':
        break

    else:
        print()
        print('Opção inválida, tente novamente.')
        print()


print('Carregando os resultados......')
time.sleep(1)
os.system('cls')
if total_familias > 0:
    print('===== RESULTADOS =====')
    print(f'Total de famílias: {total_familias}')
    print(f'Média salarial: R$ {soma_salarios / total_familias:.2f}')
    print(f'Média de filhos: {soma_filhos / total_familias:.2f}')
    print(f'Maior salário: R$ {maior_salario:.2f}')
    print(f'Menor salário: R$ {menor_salario:.2f}')
else:
    print('Nenhuma família foi cadastrada.')