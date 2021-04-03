print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 49":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('TABUADA!')
n = int(input('Digite um número: '))
for x in range(0, 11):
    print(f' {x:>2} x {n} = {x * n}')