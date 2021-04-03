print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 65":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
n = int(input('Digite um número: '))
maior = menor = soma = n
contador = 1
choice = 'S'
while choice == 'S':
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    choice = str(input('Deseja continuar? (S/N)')).upper().strip()
print(f'\nNúmeros digitados: {contador}\nMedia: {soma / contador:0.2f}\nMaior: {maior}\nMenor: {menor}')    