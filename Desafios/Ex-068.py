from random import randint
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 68":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')

choice = ''
numPlayer = numBot = result = 0
while True:
    numBot = randint(0, 6)
    numPlayer = int(input('Qual número você escolhe? '))
    choice = str(input('Par ou Ímpar? [P/I]')).strip().upper() [0]
    result = (numBot + numPlayer) % 2
    if result == 0 and choice == 'P':
        print('Fiv')
        break
    elif result == 0 and choice == 'I':
        print('fOV')
        break
print(numPlayer, numBot, result)
    
    