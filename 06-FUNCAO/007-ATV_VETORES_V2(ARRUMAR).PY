import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Produto:
    nome:str
    preco:float

lista_produtos = []

def mostrar_produto():
    produto = produto(
        nome = input('Digite o nome do produto: '),
        preco = float(input('Digite o preço: '))
    )
    lista_produtos.append(produto)

def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'{Produto.nome} custa R${Produto.preco}')

print('= SOLICITANDO DADOS =')
mostrar_produto()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)