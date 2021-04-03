from datetime import date
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 41":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('ATLETA DE NATAÇÃO\nveja sua classificação')
idade = date.today().year - int(input('\nDigite seu ano de nascimento: '))
cat = ''
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade <= 20:
    cat = 'SÊNIOR'
else:
    cat = 'MESTRE'
print(f'Você é um atleta \033[36m{cat}\033[m!')