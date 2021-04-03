print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 44":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
preço = int(input('Preço do produto: R$'))
print('[1] À vista em dinheiro/cheque (10% de desconto)')
print('[2] À vista no cartão (5% de desconto)')
print('[3] Parcelado no cartão')
choice = int(input('Forma de pagamento: '))

if choice == 1:
    print(f'Você vai pagar R${preço - (10 / 100 * preço):.2f} pelo produto!')
elif choice == 2:
    print(f'Você vai pagar R${preço - (5 / 100 * preço):.2f} pelo produto!')
elif choice == 3:
    numParcela = int(input('Número de parcelas: '))
    if numParcela <= 2:
        print(preço)
    else:
        print(f'Você vai pagar R${preço + (20 / 100 * preço):.2f} pelo produto!')
