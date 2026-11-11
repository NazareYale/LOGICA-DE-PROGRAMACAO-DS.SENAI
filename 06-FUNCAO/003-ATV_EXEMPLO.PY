import os
os.system('cls')

def mostrar_saudacao(nome, idade):
    print(f'{nome} tem {idade} anos.')

print('= Solicitando dados =')
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

print('\n= Exibindo dados =')
mostrar_saudacao(nome, idade) #Chamando a função