from datetime import date
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 54":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
maior = 0
menor = 0
for x in range(0, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    if date.today().year - ano > 21:
        maior += 1
    else:
        menor += 1
print(f'\nPessoas maiores de idade: {maior}\nPessoa menores de idade: {menor}')