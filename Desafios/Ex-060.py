print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 60":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')

n1 = int(input('Digite um número (For): '))
print(f'{n1}! = {n1}x', end= '')
for x in range (n1 - 1, 0, -1):
    n1 = n1 * x
    if x == 1:
        print(f'1 = {n1}')
    else:
        print(f'{x}x', end= '')
        
n = int(input('Digite um número (While): '))
c = n - 1
print(f'{n}! = {n}x', end= '')
while c > 0:
    n = n * c
    if c == 1:
        print(f'1 = {n}')
    else:
        print(f'{c}x', end= '')
    c -= 1
