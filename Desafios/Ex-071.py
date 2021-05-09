print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 71":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
saque = int(input('Digite o valor a ser sacado: '))
ced50 = saque // 50
saque = saque - ced50 * 50
ced20 = saque // 20
saque = saque - ced20 * 20
ced10 = saque // 10
saque = saque - ced10 * 10
ced5 = saque // 5
saque = saque - ced5 * 5
ced1 = saque // 1
saque = saque - ced1 * 1
    

print(f'''
O valor de R${saque:.2f} foi sacado!
cédulas de R$50: {ced50}
cédulas de R$20: {ced20}
cédulas de R$10: {ced10}
cédulas de R$5: {ced5}
cédulas de R$1: {ced1}
      ''')
