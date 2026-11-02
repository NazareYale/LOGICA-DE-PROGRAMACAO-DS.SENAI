import os
os.system('cls')

vetor_notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    vetor_notas.append(nota) #Append- Funciona inserindo a nota no vetor_notas.


for i in range(3):
    print(f'Nota: {vetor_notas[i]}')


#FEITO COM UMA LISTA DE NOMES
#vetor_nomes = []

#for i in range(4):
#    nome = str(input('Digite um nome: '))
#    vetor_nomes.append(nome) #Append- Funciona inserindo o nome no vetor_nomes.

#for i in range(4):
#    print(f'Nomes: {vetor_nomes[i]}')