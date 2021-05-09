n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
nums = (n1, n2, n3, n4)
if 9 in nums:
    print(f'O valor 9 aparece {nums.count(9)}x')
if 3 in nums:
    print(f'O número 3 aparece na {nums.index(3) + 1}ª posição')
else:
    print('Não foi encontrado valor 3 nesta listagem.')
print('Os números pares são: ', end='')
for x in nums:
    if x % 2 == 0:
        print(f'{x} ', end= '')