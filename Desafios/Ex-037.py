print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 37":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('CONVERSÕES LEGAIS')
num = int(input('Digite um número: '))
print(f'\nVocê digitou o número {num}')
print('Escolha a base de conversão:\n')
choice = int(input('\033[32m1 para Binário\n\033[33m2 para Octal\n\033[35m3 para Hexadecimal\033[m\n'))
if choice == 1:
    print('\nVocê escolheu \033[32mBinário\033[m')
    print(f'Seu número convertido para Binário: {bin(num)[2:]}')
elif choice == 2:
    print('\nVocê escolheu \033[33mOctal\033[m')
    print(f'Seu número convertido para Octal: {oct(num)[2:]}')
elif choice == 3:
    print('\nVocê escolheu \033[35mHexadecimal\033[m')
    print(f'Seu número convertido para Hexadecimal: {hex(num)[2:]}')
else:
    print('\n\033[31mESCOLHA UM VALOR DE 1 A 3.')