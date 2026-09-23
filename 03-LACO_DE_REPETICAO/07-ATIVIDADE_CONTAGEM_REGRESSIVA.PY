import os
import time
os.system('cls')

numero = int(input('Digite um número: '))

for i in range(numero,-1,-1):
    print(i)
    time.sleep(1)
#for i in range(10,0,-1):
#    print(i)
#    time.sleep(1)
#import time é uma biblioteca usada em comando com relação com tempo
#time.sleep é usado para definir um tempo para o qual o comando irá esperar antes de funcionar novamente