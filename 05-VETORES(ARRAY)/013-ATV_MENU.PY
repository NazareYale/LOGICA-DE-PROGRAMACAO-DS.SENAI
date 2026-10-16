import os
os.system('cls')

print('''              ==MENU==

CÓDIGO         PRATO            VALOR

1              PICANHA          R$25.00

2              LASANHA          R$20.00

3              STROGONOFF       R$15.00

4              SALADA MISTA     R$15.00

5              MISTO QUENTE     R$5.00

''')

while True:
    Codigo = input('Digite a opção desejada: ')

    match Codigo:
        case '1':
            print('Prato: Picanha \nvalor: R$25,00')
            break
        case '2':
            print('Prato: Lasanha \nvalor: R$20,00')
            break
        case '3':
            print('Prato: Strogonoff \nvalor: R$15,00')
            break
        case '4':
            print('Prato: Salada Mista \nvalor: R$15,00')
            break
        case '5':
            print('Prato: Misto Quente \nvalor: R$5,00')
            break
        case _:
                    print()
                    print('Opção inválida!')
                    print()