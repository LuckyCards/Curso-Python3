print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 66":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        print('\033[31mVocê ativou o break\033[m')
        break
    cont += 1
    soma += num
    if soma >= 1000 or cont == 25:
        print('\033[31mVocê ativou o break\033[m')
        break

print(f'''
Números digitados: {cont}
Soma total dos números: {soma}
    ''')