from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class paciente:
    nome : str
    idade : str
    telefone : str
    endereco : str

    def mostrar_pacientes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
    
    def mostrar_idade_pacientes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        
    
    def mostrar_whatsapp_pacientes(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        
lista_pacientes = []

print('== SOLICITANDO DADOS ==')
for i in range(1):
        dados = paciente(
        nome = input('Digite seu nome: '),
        idade = input('Digite sua idade: '),
        telefone = input('Digite seu telefone: '),
        endereco = input('Digite seu endereço: ')
        )
        lista_pacientes.append(dados)

print('\n== EXIBINDO DADOS ==')
for paciente in lista_pacientes:
    paciente.mostrar_pacientes()

print('\n== EXIBINDO IDADES ==')
for paciente in lista_pacientes:
    paciente.mostrar_idade_pacientes()
    
print('\n== EXIBINDO WHATSAPP ==')
for paciente in lista_pacientes:
    paciente.mostrar_whatsapp_pacientes()
