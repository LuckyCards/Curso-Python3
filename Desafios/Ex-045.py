import random
from time import sleep
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 45":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\n\033[32mJO\033[33mKEN\033[36mPÔ\033[m')
choice = str(input('Escolha: ')).lower()
lista = ['pedra','papel','tesoura']
pc = lista[random.randrange(len(lista))]
sleep(0.2)
print('\033[32mJO')
sleep(0.6)
print('\033[33mKEN')
sleep(0.6)
print('\033[36mPÔ')
sleep(1)
print(f'\033[mO computador escolheu: {pc}.')
if choice == pc:
    print('Ninguém ganhou!')
elif choice == 'pedra' and pc == 'tesoura': #pedra
    print('Pedra ganha de tesoura. Você \033[32mganhou\033[m!')
elif choice == 'pedra' and pc == 'papel':
    print('Papel ganha de pedra. Você \033[31mperdeu\033[m!')
    
elif choice == 'papel' and pc == 'tesoura': #papel
    print('Tesoura ganha de papel. Você \033[31mperdeu\033[m!')
elif choice == 'papel' and pc == 'pedra':
    print('Papel ganha de pedra. Você \033[32mganhou\033[m!')
    
elif choice == 'tesoura' and pc == 'pedra': #tesoura
    print('Pedra ganha de tesoura. Você \033[31mperdeu\033[m!')
elif choice == 'tesoura' and pc == 'papel':
    print('Tesoura ganha de papel. Você \033[32mganhou\033[m!')