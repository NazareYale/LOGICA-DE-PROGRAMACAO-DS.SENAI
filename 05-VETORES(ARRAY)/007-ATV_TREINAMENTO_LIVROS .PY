import os
os.system('cls')

print('= INSERINDO LIVROS NO VETOR =')
vetor_livros = []

for i in range(5):
    livros = input(f'Digite o nome do {i+1}º livro: ')
    vetor_livros.append(livros)


print('\n=EXIBINDO LIVROS DO VETOR =')
for indice, livraria in enumerate(vetor_livros, start=1):#ForEach
    print(f'Seu {indice}º livro: {livraria}')