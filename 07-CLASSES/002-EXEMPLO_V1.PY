from dataclasses import dataclass
import os
os.system('cls')

#USA STR NO TELEFONE POR CAUSA DA QUANTIDADE DE BYTES QUE A VARIÁVEL INT USA, ASSIM ECONOMIZANDO A MEMÓRIA DO HD/SSD.
@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str
lista_clientes = []

print('== SOLICITANDO DADOS ==')
for i in range(1):
    dados_do_cliente = Cliente(
        nome = input('Digite o seu nome: '),
        telefone = input('Digite o seu telefone: '),
        email = input('Digite o seu e-mail: ')
    )
    lista_clientes.append(dados_do_cliente)

print('\n== EXIBINDO DADOS ==')
for cliente in lista_clientes:
    print(f'='*15)
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Email: {cliente.email}')
    print(f'='*15)