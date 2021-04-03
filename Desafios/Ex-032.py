print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 32":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\n\033[33mVeja se um ano é bissexto ou não:\033[m\n')
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (f'O ano de \033[1m{ano}\033[m é Bissexto')
else:
    print (f'O ano de \033[1m{ano}\033[1m \033[31mnão\033[m é Bissexto')