from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

QUANTIDADE_CLIENTES = 3
lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    cliente = fornecedor(
        nome= input('Digite seu nome: '),
        email= input('Digite seu email: '),
        telefone= input('Digite seu telefone: '),
        endereco= input('Digite seu endereço: ')
    )
    lista_clientes.append(cliente)

    arquivo = 'Dados_fornecedores.csv'
    with open(arquivo, 'a') as arquivo_fornecedores:
        for cliente in lista_clientes:
            arquivo_fornecedores.write(f'{cliente.nome}, {cliente.email}, {cliente.telefone}, {cliente.endereco}\n')
    
    print('Cliente salvo com sucesso!\n')