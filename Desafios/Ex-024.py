print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 24":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
city = str(input('Cidade: ')).upper().split()
print(f'Começa com Santo? {"SANTO" in city[0]}')