from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #NOME DA VARIÁVEL : TIPO DA VARIÁVEL
    nome: str
    idade: int

lista_clientes = []

# SOLICITANDO DADOS DE UM CLIENTE.
lista_clientes.append(Cliente(nome= 'Marta', idade= 30))
lista_clientes.append(Cliente(nome= 'José', idade= 40))

for cliente in lista_clientes:
    print(f'='*15)
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'='*15)