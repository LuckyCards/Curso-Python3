from random import randint
from time import sleep
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 28":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\n\033[1;36mDesafio: acerte o número que estou pensando!\033[m')
numPlayer = int(input('\nQual número entre 0 e 10 eu pensei? '))
numBot = randint(0, 10)
sleep(0.2)
print('\n\033[36mProcessando...\033[m\n')
sleep(1)
if numPlayer == numBot:
    print(f'\033[32mParabéns!\033[m O número que eu pensei era \033[32m{numBot}\033[m.')
else:
    print(f'\033[31mQue pena!\033[m O número que eu pensei era \033[32m{numBot}\033[m.')
print('\nFim de jogo.')