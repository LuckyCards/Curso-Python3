print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 6":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
num = int(input('Digite um número: '))
print('\nResultados:')
print(f'O dobro de {num}, equivale a {num * 2}!', end = '. ')
print(f'O triplo de {num}, equivale a {num * 3}!')
print(f'A Raiz Quadrada de {num}, equivale a {num ** (1/2):.3f}!', end = '. ')
print(f'A Raiz Cúbica de {num}, equivale a {num ** (1/3):.3f}!')