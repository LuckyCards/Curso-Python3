print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 62":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
n = int(input('Digite um número: '))
c = 0

x = 0
y = 1
z = 0

while c < n:
    print(x, end= ' ➝  ')
    z = x + y
    x = y
    y = z   
    
    c += 1
print('Acabou.')