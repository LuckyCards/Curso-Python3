print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 27":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
name = str(input('Digite seu nome completo: ')).strip().title().split()
print(f'\nSeu primeiro nome é: \033[4;36m{name[0]}\033[m \nSeu último nome é: \033[4;36m{name[len(name) - 1]}\033[m')
