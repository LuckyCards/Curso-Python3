print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 52":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
n = int(input('Digite um número: '))
for x in range(2, n + 1):
    if x == n:
        print('Primo')
        break
    if n % x == 0:
        print('não é primo')
        break
