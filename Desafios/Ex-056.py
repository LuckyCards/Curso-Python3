print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 56":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')

n = int(input('Pessoas: '))
mediaGrupo = 0
jovensF = 0
idadeIdoso = 0 
nomeidoso = ''

for x in range(0, n):
    print(f'\nPessoa {x+1}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    print('[1]Masculino\n[2]Feminino')
    sexo = int(input('Sexo: '))
    mediaGrupo += idade
    if x == 0:
        idadeIdoso = idade
        nomeidoso = nome
   
    if sexo == 1 and idade > idadeIdoso:
        idadeIdoso = idade
        nomeidoso = nome
    
    if sexo == 2 and idade <= 20:
        jovensF += 1

print(f'\nMédia do grupo: {int(mediaGrupo / n)}\nIdade do idoso: {nomeidoso}\nMulheres abaixo de 20: {jovensF}')
