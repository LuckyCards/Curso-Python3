print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 51":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for x in range(t, t + r*10, r):
    print(x,"➝ ", end=' ')
print('ACABOU.')