print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 25":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
name = str(input('Digite seu nome: ')).strip()
print(f'Este nome tem Silva? {"SILVA" in name.upper()}')