from unidecode import unidecode #Biblioteca para remover acentuação :)
from time import sleep
from random import randint
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 30":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\n\033[36mÍmpar ou Par contra o bot\033[m\n')
choice = str(unidecode(input(f'escolha \033[1mPar\033[m ou \033[1mÍmpar\033[m: '))).strip().upper()
num = int(input('escolha um número de 0 a 5: '))
numBot = randint(0,5)
sleep(1)
print('\n\033[36mProcessando dados...\033[m\n')
sleep(3)
if choice == "PAR" and (num + numBot) %2 == 0:
    print(f'Parabéns! Você escolheu \033[36m{choice}\033[m e \033[1;32mGANHOU\033[m contra o bot. \nEscolha do bot: \033[31m{numBot}\033[m\nSua Escolha: \033[32m{num}\033[m') 
elif choice == "PAR" and (num + numBot) %2 != 0:
    print(f'Que pena! Você escolheu \033[36m{choice}\033[m e \033[1;31mPERDEU\033[m contra o bot. \nEscolha do bot: \033[31m{numBot}\033[m\nSua Escolha: \033[32m{num}\033[m') 

if choice == "IMPAR" and (num + numBot) %2 != 0:
    print(f'Parabéns! Você escolheu \033[36m{choice}\033[m e \033[1;32mGANHOU\033[m contra o bot. \nEscolha do bot: \033[31m{numBot}\033[m\nSua Escolha: \033[32m{num}\033[m') 
elif choice == "IMPAR" and (num + numBot) %2 == 0:
    print(f'Que pena! Você escolheu \033[36m{choice}\033[m e \033[1;31mPERDEU\033[m contra o bot. \nEscolha do bot: \033[31m{numBot}\033[m\nSua Escolha: \033[32m{num}\033[m')

if num > 5:
    print(f'\033[1;31mVOCÊ É BURRO? EU PEDI PRA ESCOLHER ENTRE 0 E 5 VOCÊ ESCOLHE {num}?!')
if choice != "PAR" and choice != "IMPAR":
    print(f'\033[1;31mVOCÊ É BURRO? {choice} ⟵ ISSO POR ACASO É PAR OU ÍMPAR?!')