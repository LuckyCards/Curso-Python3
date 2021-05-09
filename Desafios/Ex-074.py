from random import randint
'''n1 = randint(-10, 10)
n2 = randint(-10, 10)
n3 = randint(-10, 10)
n4 = randint(-10, 10)
n5 = randint(-10, 10)
numeros = (n1, n2, n3, n4, n5) 
print(f'Números da tupla: {numeros}')
print(f'Maior número: {sorted(numeros)[-1]}')
print(f'Menor número: {sorted(numeros)[0]}')
'''
num = (randint(0, 10), randint(0, 10), randint(0, 10), 
       randint(0, 10), randint(0, 10))

print('Os valores sorteados foram: ', end= '')
for x in num:
    print(f'{x} ', end= '')
print(f'\nO maior valor sorteado foi: {max(num)} e o menor foi {min(num)}')
