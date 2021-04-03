print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 8":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('Conversões')
metro = float(input('Digite um valor métrico: '))
km = metro / 1000.0
dm = metro / 100.0
cm = metro * 100.0
ml = metro * 1000.0
print(f'\nAs conversões da únidade métrica digitada são: ')
print(f'Metros para {"Quilometros":.<15}: {km:.5f}')
print(f'Metros para {"Decâmetros":.<15}: {dm:.4f}')
print(f'Metros para {"Metros:":.<15}: {metro}')
print(f'Metros para {"Centimetros":.<15}: {cm}')
print(f'Metros para {"Milímetros":.<15}: {ml}')
