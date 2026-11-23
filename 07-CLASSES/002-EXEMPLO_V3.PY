from dataclasses import dataclass
import os
os.system('cls')

#USA STR NO TELEFONE POR CAUSA DA QUANTIDADE DE BYTES QUE A VARIÁVEL INT USA, ASSIM ECONOMIZANDO A MEMÓRIA DO HD/SSD.
@dataclass
class Cliente:
    nome:str
    telefone:str
    email:str

    #FUNÇÃO DENTRO DA CLASSE.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Email: {self.email}')
        print('='*30)
    
    #FUNÇÃO SOMENTE PARA ENVIAR EMAILS.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print('='*30)

    #FUNÇÃO SOMENTE PARA ENVIAR WHATSAPP.
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)

lista_clientes = []

print('== SOLICITANDO DADOS ==')
for i in range(2):
    dados = Cliente(
        nome = input('Digite o seu nome: '),
        telefone = input('Digite o seu telefone: '),
        email = input('Digite o seu e-mail: ')
    )
    lista_clientes.append(dados)


print('\n== EXIBINDO DADOS ==')
for cliente in lista_clientes:
    cliente.mostrar_dados()

print('\n== EXIBINDO EMAIL MARKETING ==')
for cliente in lista_clientes:
    cliente.email_marketing()

print('\n== EXIBINDO WHATSAPP MARKETING ==')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()