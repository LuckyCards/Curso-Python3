print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 69":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
maior = M = F = 0
while True:
    age = str(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo(F/M): ')).strip() [0]
    if age.isnumeric() == True and sexo in 'FMfm':
        age = int(age)
        if age >= 18:
            maior += 1
        if sexo in 'Mm':
            M += 1
        elif sexo in 'Ff' and age <= 20:
            F += 1
    else:
        print('Digite um valor valido!')
    choice = str(input('Deseja continuar? (S/N): ')).strip() [0]
    if choice in 'Nn':
        print('\033[31mVocê ativou o break\033[m')
        break
print(f'''Pessoas com mais de 18: {maior}
Quantidade de Homens: {M}
Quantidade de Mulheres abaixo de 20 anos: {F}
      ''')