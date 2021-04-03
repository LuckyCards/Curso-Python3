print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 53":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
palavra = str(input('Digite o palindromo: ')).strip().upper().replace(' ', '')
for x in range(0, len(palavra)):
    if palavra[x] != palavra[(x+1)*-1]:
        print('não é palindromo')
        break
    if x == len(palavra) - 1:
        print('é um palindromo')