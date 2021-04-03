from time import sleep
print('\n')
print('\033[33m—'*32)
print('\033[36m  PERGUNTE AO PEIXE v0.2Alpha')
print('\033[33m—'*32, '\033[m\n')
x = str(input('Digite uma palavra: ')).strip().upper()
y = str(input('Digite outra palavra: ')).strip().upper()
print('\n\033[32mPensando...\033[m\n')
sleep(2)
points = 0 #Positivo = X / Negativo = Y

if len(x) != len(y):        #Peixe gosta de palavras grandes
    if len(x) > len(y):
        points = points + 1
    else:
        points = points - 1

if ('PEIXE' in x) == True:    #Peixe gosta de peixes
    points = points + 2
if ('PEIXE' in y) == True:
    points = points - 2
    

if x.count(' ') < y.count(' '):     #Peixe não gosta de espaços
    points = points + 1
elif x.count(' ') > y.count(' '):
    points = points - 1
    
if ('POLVO' in x) == True and ('POLVO' in y) == False:      #Peixe ODEIA polvos
    points = points - 1000
if ('POLVO' in y) == True and ('POLVO' in x) == False:
    points = points + 1000
if ('POLVO' in x) == True and ('POLVO' in y) == True:
    points = 5000
print('\033[33m—'*32)
if points != 5000:
    if points != 0:
        if points > 0: 
            print(f'O peixe escolheu:\033[36m{x.capitalize()}')
        else:
            print(f'O peixe escolheu:\033[36m{y.capitalize()}')
    else:
        print('\033[34mO peixe não sabe :(')
else:
    print('\033[31mO PEIXE DETESTA POLVOS!!!')
print('\033[33m—'*32, '\033[m\n')
print(points)