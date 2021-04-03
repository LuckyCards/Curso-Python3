print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 40":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
nota1 = int(input('Nota de Português: '))
nota2 = int(input('Nota de Matemática: '))
nota3 = int(input('Nota de Geografia: '))
media = (nota1 + nota2 + nota3) / 3

if media < 5:
    print('\033[31mREPROVADO!')
    print(f'Você obteve uma média de {media:.2f}\nVocê foi muito inferior a média esperada.')
elif media > 7:
    print('\033[36mAPROVADO!')
    print(f'Você obteve uma média de {media:.2f}\nParabéns pela nota!')
else:
    print('\033[33mRECUPERAÇÃO!')
    print(f'Você obteve uma média de {media:.2f}\nOutra prova foi marcada para sua recuperação.')
print('\033[m')