import os
os.system('cls')

def inflacionar_preco(preco_produto):
    if preco_produto >= 100:
        resultado = preco_produto * 1.10
    else:
        resultado = preco_produto * 1.20
    return resultado

preco_produto = float(input('Digite o preço do produto: '))

preco_inflacionado = inflacionar_preco(preco_produto)

print(f'Preço inicial: R${preco_produto:.2f}')
print(f'Preço inflacionado: R${preco_inflacionado:.2f}')