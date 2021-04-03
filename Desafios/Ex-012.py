print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 12":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
produto = input('Produto: ')
preço = float(input('Preço do produto: '))
desconto = int(input('Desconto aplicado: '))
promo = desconto / 100 * preço 
print('\nTabela do produto:')
print(f'Produto: {produto}. \nPreço Real: R${preço:.2f} \nDesconto: {desconto}% \nPreço com Desconto: R${preço - promo:.2f}')