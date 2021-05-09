print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 70":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
prodRich = prodCheap = '' #Nome do produto mais caro e mais barato
priceRich = priceCheap = 0 #Preço do produto mais caro e mais barato
total = prod1000 = 0 #Total gasto e produtos acima de 1000 reais
while True:
    prod = str(input('Digite o nome do produto: '))
    price = float(input('Digite o preço do produto: R$'))
    if priceCheap == 0 and priceRich == 0:
        priceCheap = price
        prodCheap = prod
        priceRich = price
        prodRich = prod
    elif price > priceRich:
        prodRich = prod
        priceRich = price
    elif price < priceCheap: 
        prodCheap = prod
        priceCheap = price
    if price >= 1000:
        prod1000 += 1
    total += price
    choice = str(input('Deseja continuar? (S/N): ')).strip() [0]
    while choice not in 'SsNn':
        choice = str(input('Deseja continuar? (S/N): ')).strip() [0]
    if choice in 'Nn':
        print('\033[31mVocê ativou o break\033[m')
        break
print(f'''
Produto mais caro: {prodRich} - R${priceRich:.2f}
Produto mais barato: {prodCheap} - R${priceCheap:.2f}
Quantidade de produtos acima de R$1,000.00: {prod1000}
Total gasto na compra: {total:.2f}
      ''')