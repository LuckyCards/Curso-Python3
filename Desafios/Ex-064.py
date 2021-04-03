print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 64":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
soma = contador = n = 0 #3 variaveis em uma linha!
print('[999] sair')
n = int(input(''))
while n != 999:
    contador += 1
    soma += n
    n = int(input(''))
print(f'Soma total: {soma}\nNúmeros digitados: {contador}')