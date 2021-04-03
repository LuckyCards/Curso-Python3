print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 48":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
soma = 0
total = 0
for x in range(1, 500, 2):
    if x % 3 == 0:
        total += 1
        soma += x
print(soma, total)