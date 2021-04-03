print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 59":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')

n1 = 0
n2 = 0
choice = 4
while choice != 5:
    if choice == 4:
        print('Digite dois valores e escolha as opções a seguir!')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Digitar Novamente\n[5] Sair do Programa')
    choice = int(input('Escolha: '))
    elif choice == 1:
        print(f'\033[33m{"—"*40:^40}\033[m')
        print(f'A soma entre {n1} e {n2} resulta em {n1 + n2}!')
        print(f'\033[33m{"—"*40:^40}\033[m')
    elif choice == 2:
        print(f'\033[33m{"—"*40:^40}\033[m')
        print(f'A multiplicação entre {n1} e {n2} resulta em {n1 * n2}!')
        print(f'\033[33m{"—"*40:^40}\033[m')
    elif choice == 3:
        if n2 > n1:
            print(f'\033[33m{"—"*30:^30}\033[m')
            print(f'O maior número é {n2}')
            print(f'\033[33m{"—"*30:^30}\033[m')
        else:
            print(f'\033[33m{"—"*30:^30}\033[m')
            print(f'O maior número é {n1}')
            print(f'\033[33m{"—"*30:^30}\033[m')
print('Fim do programa.')       
        