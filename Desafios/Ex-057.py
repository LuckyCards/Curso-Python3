print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 57":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')

sexo = str(input('Digite seu sexo (M/F): ')).upper().strip() [0]
while sexo not in 'MF':
    sexo = str(input('Por favor, informe seu sexo corretamente (M/F): ')).upper().strip() [0]
        
if sexo == 'M':
    print(f'Seu sexo é: Masculino!')
else:
    print(f'Seu sexo é: Feminino!')