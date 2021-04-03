print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 67":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
x = c = 0
while True:
    n = int(input('Digite um número: '))
    for x in range (0, 11):
        print(f'{n:>2} x {x} = {n * x}')
    if n < 0:
        print('\033[31mVocê ativou o break\033[m')
        break