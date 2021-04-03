print(f'\033[33m{"—"*35:^35}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 36":^35}\033[m')
print(f'\033[33m{"—"*35:^35}\033[m')
tvVal = int(input('Digite o valor da Smart Tv QLED 8K: '))
sal = int(input('Digite o seu salário mensal: '))
parcelaMensal = int(input('Digite a anuídade: ')) * 12
preçoMensal = tvVal / parcelaMensal
if preçoMensal > 30 / 100 * sal:
    print('Seu empréstimo foi \033[31mNEGADO\033[m')
else:
    print('Seu empréstimo foi \033[36mAPROVADO\033[m')
print(f'Parcelas de R${preçoMensal:.2f}')
