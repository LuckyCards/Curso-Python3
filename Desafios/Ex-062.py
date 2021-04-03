print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 62":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
t = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
target = 10
c = 0
while target >= 0:
    print(t + r * c, end= ' ➝  ')
    c += 1
    target -= 1
    
    if target == 0:
        target = int(input('PAUSA\nAdiconar mais termos: '))