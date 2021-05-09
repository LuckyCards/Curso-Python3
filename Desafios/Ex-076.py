listagem = ('Cebola', 2.79, 'Batata', 1.47, 'Feijão', 11.54, 'Energético', 5.98)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    elif pos % 2 != 0:
        print(f'R${listagem[pos]:.2f}')