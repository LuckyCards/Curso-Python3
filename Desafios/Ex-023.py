print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 23":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
num = int(input('Digite um número de 0 a 9999: '))
if num < 9999 and num > 0:
    unid = num // 1 % 10
    dez = num // 10 % 10
    cent = num // 100 % 10
    milh = num // 1000 % 10
    print(f'Unidade: {unid}')
    print(f'Dezena: {dez}')
    print(f'Centena: {cent}')
    print(f'Milhar: {milh}')
else:
    print(f'Você digitou: {num}\n\033[31mDIGITE UM NÚMERO ENTRE 0 E 9999!\033[m')