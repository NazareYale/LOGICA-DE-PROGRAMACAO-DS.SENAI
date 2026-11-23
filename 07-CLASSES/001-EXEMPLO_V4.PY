from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #NOME DA VARIÁVEL : TIPO DA VARIÁVEL
    nome: str
    idade: int
    altura: float
    peso: float

lista_clientes = []

# SOLICITANDO DADOS DE UM CLIENTE.
print('== SOLICITANDO DADOS ==')
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('\nDigite o seu nome: '), 
        idade = int(input('Digite a sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite o seu peso: '))
    )
    lista_clientes.append(dados_do_cliente)
    

print('== EXIBINDO DADOS ==')
for cliente in lista_clientes:
    print(f'='*15)
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print(f'Peso: {cliente.peso}')
    print(f'='*15)