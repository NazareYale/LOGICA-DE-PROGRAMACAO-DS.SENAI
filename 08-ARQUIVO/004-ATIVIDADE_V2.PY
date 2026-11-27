from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

lista_clientes = []

arquivo = 'Dados_fornecedores.csv'
with open(arquivo, 'r') as arquivo_fornecedor:
    for linha in arquivo_fornecedor:
        nome,email,telefone,endereco = linha.strip().split(',')
        lista_clientes.append(fornecedor(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco
        ))
    
print('\nExibindo fornecedores: ')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Email: {cliente.email}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Endereço: {cliente.endereco}')
    print('='*35)