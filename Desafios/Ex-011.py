print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 11":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
y = float(input('Altura da parede: '))
x = float(input('Largura da parede: '))
preço = 157.88
area = x * y
litros = area / 2 
baldes = int(litros // 3.6 + 1)
print(f'Area da parede: {area:.2f}m²')
print(f'Baldes necessários: {baldes} baldes de 3.6L. Totalizando {litros:.2f} litros.')
print(f'Total gasto em baldes de tinta: R${preço * baldes:.2f}')

