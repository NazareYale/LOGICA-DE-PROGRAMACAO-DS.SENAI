import os
os.system('cls')

print('''       ==MENU==
Opções      Produto     Preço

1           Macarrão    R$ 3,80

2           Arroz       R$ 5,30

3           Uvas        R$ 2,50

4           Abacaxi     R$ 4,95

5           Banana      R$ 3,75

''')



while True:
    opcao = input('Digite a opção desejada: ')

    match opcao:
        case '1':
            print('Produto: Macarrão \nPreço: R$3,80')
            break
        case '2':
            print('Produto: Arroz \nPreço: R$5,30')
            break
        case '3':
            print('Produto: Uvas \nPreço: R$2,50')
            break
        case '4':
            print('Produto: Abacaxi \nPreço: R$4,95')
            break
        case '5':
            print('Produto: Banana \nPreço: R$3,75')
            break
        case _:
            print()
            print('Opção inválida!')
            print()
