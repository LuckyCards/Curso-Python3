print(f'\033[33m{"—"*44:^44}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 33":^44}\033[m')
print(f'\033[33m{"—"*44:^44}\033[m')
print(f'\033[36m{"ESCREVA 3 NÚMEROS E VEJA O MAIOR E O MENOR":^45}\033[m')
n1 = int(input('número: '))
n2 = int(input('número: '))
n3 = int(input('número: '))
    
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n3
if n1>n2 and n1>n3:
    maior = n1
if n2>n3 and n2>n1:
    maior = n2
    
print (f'\nO \033[1;36mmenor\033[m valor digitado foi {menor} \nO \033[1;36mmaior\033[m valor digitado foi {maior}')