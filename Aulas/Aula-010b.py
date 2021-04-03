nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media:.1f}')
if media >= 5:
    print('Parabéns! você foi aprovado.')
else:
    print('Uma pena! você terá que fazer a recuperação.')
