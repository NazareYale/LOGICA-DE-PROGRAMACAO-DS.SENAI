import os
from datetime import date
os.system('cls')

def verificar_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

ano_nascimento = int(input('Digite o seu ano_nascimento de nascimento: '))

idade = verificar_idade(ano_nascimento)

print(f'Ano de nascimento : {ano_nascimento}')
print(f'A sua idade é: {idade}')