import os
os.system('cls')

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f'Digite a {i+1}º nota: '))
    soma += notas

#PROCESSAMENTO
media = soma / QUANTIDADE_NOTAS

if notas >= 7:
    resultado = 'Aprovado.'
elif media >=4:
    resultado = 'Reprovado'
else:
    resultado = 'Reprovado.'


#SAÍDA
print(f'\nExibindo resultados')
print(f'A sua média é: {media}')
print(f'Resultado: {resultado}')
