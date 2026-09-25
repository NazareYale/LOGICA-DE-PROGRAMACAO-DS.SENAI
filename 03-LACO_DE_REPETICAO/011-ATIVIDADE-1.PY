import os
os.system('cls')

#for i in range(100, 121): NESSE ELE PERCORRE CADA NÚMERO PARA VERIFICAR SE É PAR.
#for i in range(100, 121, 2): NESSE ELE PERCORRE DE 2 EM 2 PARA VERIFICAR SE É PAR.
for i in range(100, 121):
    if i % 2 == 0:
        print(f'O número {i} é par.')
