print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 4":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
word = input('Insira um texto: ').strip()
print(type(word))
print(f'É uma letra? {word.isalpha()}')     #com format
print(f'É um número? {word.isnumeric()}')   #com format
print('Está em maiúsculo?',word.isupper())  #sem format
print('Está minúsculo?', word.islower())    #sem format
