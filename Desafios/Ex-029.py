print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 29":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
velo = int(input('Velocidade do veículo: '))
multa = (velo - 80) * 7 
print(f'\033[1m{"―"*30:^30}\033[m')
print(f'\033[1m{"RADAR DE VELOCIDADE A FRENTE":^30}\033[m')
if velo > 80:
    print(f'\nVocê foi multado em \033[31mR${multa:.2f}\033[m.\n\033[33mMotivo: excedeu os limites de \nvelocidade da pista (80km/h)\033[m\n')
else:
    print(f'\nVocê passou pelo radar com uma \nvelocidade de \033[32m{velo}km/h\033[m.\n')
print(f'\033[1m{"―"*30:^30}\033[m')