print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 61":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
c = 0
while c < 10:
    print(t + r * c, end= '➝ ')
    c += 1
print('ACABOU.')