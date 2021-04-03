from random import randint
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 58":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
n = randint(0,10)
n2 = 20
attempts = 0
print('Adivinhe o número que estou pensando!')
while n2 != n:
    n2 = int(input(f'Tentativa {attempts}: '))
    attempts += 1
    if n2 > n:
        print('Menos... Está quase lá!')
    elif n2 < n:
        print('Mais... Está muito perto!')

if attempts > 1:
    print(f'Parabéns! O número que pensei foi {n}. Você precisou usar {attempts} tentativas.')
else:
    print(f'Parabéns! Você acertou em apenas 1 tentativa!!! O número que eu pensei foi {n}!')