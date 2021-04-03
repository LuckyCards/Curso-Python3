print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 35":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\nDigite o comprimento das retas para formar um triangulo:')
rA = float(input('\033[31mcomprimento A: '))
rB = float(input('\033[32mcomprimento B: '))
rC = float(input('\033[33mcomprimento C: '))
print('\n\033[4;36mResultado:\033[m')
maiorReta = rA
x = rB
x2 = rC
if rB>rA and rB>rC:
    maiorReta = rB
    x = rA
    x2 = rC
if rC>rA and rC>rB:
    maiorReta = rC
    x = rA
    x2 = rB

if maiorReta < (x + x2):
    print('\033[32mPode formar um triangulo')
else:
    print('\033[31mNão pode formar um triangulo')