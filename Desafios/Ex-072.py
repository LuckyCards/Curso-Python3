print(f'\033[32m{"—"*31:^31}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 72":^31}\033[m')
print(f'\033[32m{"—"*31:^31}\033[m')

numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    n = int(input('Inválido. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numExtenso[n]}')