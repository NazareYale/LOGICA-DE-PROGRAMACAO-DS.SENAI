import os
from dataclasses import dataClass
os.system('cls')

@dataclass
class produto:
    nome:str
    preco:float

lista_produtos = []

def mostrar_produto():
    produto = produto(
        nome =input('Digite o nome do produto: ')
        preco = float(input('Digite o preço: '))
    )
    lista_produtos.append(produto)

def mostrar_dados(lista_produtos):
    for i in range(3):
        print(f'{produto.nome} custa R$ {produto.preco}')

print('= SOLICITANDO DADOS =')
solicitar_dados()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)