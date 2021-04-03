import math
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 17":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
catOp = float(input('Insira o Cateto Oposto: '))
catAdj = float(input('Insira o Cateto Adjacente: '))
hip = math.hypot(catOp, catAdj)
print (f'\nA hipotenusa deste triangulo retangulo equivale a {hip:0.2f}')