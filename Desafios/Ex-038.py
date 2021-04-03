print(f'\033[33m{"—"*30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 39":^30}\033[m')
print(f'\033[33m{"—"*30}\033[m')
print('Digite dois números e veja o maior!')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O número {n1} é o maior.')
elif n2 > n1:
    print(f'O número {n2} é o maior.')
elif n1 == n2:
    print(f'Não existe número maior, ambos são iguais.')