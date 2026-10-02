import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a sua {i+1}º nota: '))
        if nota < 0 or nota > 10:
            print()
            print('Nota inválida, digite a sua nota novamente.')
            print(input('Pressione qualquer tecla para voltar a pergunta.....'))
            os.system('cls')
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print()
print(f'A sua média é: {media}')

if nota >= 7:
    print('Aprovado!')
            
elif nota >= 5 and nota <= 6.9:
    print('Em recuperação!')

else:
    print('Reprovado!') 
    


