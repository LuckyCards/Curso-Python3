from datetime import date
print(f'\033[33m{"—"*54:^54}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 39":^54}\033[m')
print(f'\033[33m{"—"*54:^54}\033[m')
print(f'\033[1m{"ALISTAMENTO JEDI":^54}\033[m')

anoNasc = int(input('\nDigite seu ano de nascimento: '))
idade = date.today().year - anoNasc
if idade < 18:
    print(f'\n{"Sua hora ainda não chegou, jovem padawan!":^54}')
    print(f'{f"Falta {18 - idade} anos para se tornar um Jedi!":^54}')
elif idade == 18:
    print(f'\n{"Sua hora de se tornar um Jedi é agora, jovem padawan!":^54}')
    print(f'{"Se apresente a um Mestre, e comece seu treinamento!":^54}')
else:
    print(f'\n{"Você já é um Jedi! Use sua força com sabedoria!":^54}')
    print(f'{f"Você luta contra o Império a {idade - 18} anos!":^54}')
print(f'\033[33m{"—"*54:^54}\033[m')





'''print(int(str(datetime.date.today()).replace('-', '')))

print(str(datetime.date.today()).split('-')[2], end='/')
print(str(datetime.date.today()).split('-')[1], end='/')
print(str(datetime.date.today()).split('-')[0])'''