print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 43":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('Calculadora de IMC:')
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
s = ''
if imc <= 18.5:
    s = 'MAGREZA'
elif imc <= 24.9:
    s = 'NORMAL'
elif imc <= 29.9:
    s = 'SOBREPESO'
elif imc <= 39.9:
    s = 'OBESIDADE'
else:
    s ='OBESIDADE GRAVE'
print(f'Seu IMC está {imc:.1f}. Isso resulta em: {s}')