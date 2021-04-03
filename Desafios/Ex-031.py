from time import sleep
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 31":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
km = int(input('Qual a distância da sua viagem? '))
sleep(0.2)
print('\n\033[36mProcessando...\033[m\n')
sleep(3)
print('\n―――――PREÇO DAS PASSAGENS―――――')
if km <= 200:
    x = 0.50
    preço = km * x
else:
    x = 0.45
    preço = km * x
print(f'\nSua passagem custará \033[32mR${preço:.2f}\033[m\ntaxa de \033[31mR${x:.2f}\033[m por Km.\n')
print('―' * 29)