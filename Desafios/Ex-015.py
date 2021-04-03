print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 15":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('Algue seu \033[36mTesla Model S\033[m!')
aluguel = int(input('Dias Alugados: '))
aluguelPreço = 60
km = int(input('Quilometros rodados: '))
kmPreço = 0.15
total = aluguel * aluguelPreço + km * kmPreço
print (f'O total a pagar é de R${total:.2f}')