print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 50":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
soma = 0
for x in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print(soma)