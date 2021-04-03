print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 55":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
n = int(input('Número de pessoas: '))
maiorPeso = 0
menorPeso = 0
for x in range(0, n):
    peso = int(input('Peso da pessoa: '))
    if x == 0:
        maiorPeso = peso
        menorPeso = peso
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'Maior peso: {maiorPeso}\nMenor peso: {menorPeso}')