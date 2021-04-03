from time import sleep
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 34":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
print('\n\033[32mTABELA DE AUMENTO:\n\033[m')
nome = str(input('\033[4mNome do funcionário:\033[m ')).strip().title()
sal = float(input('\033[4mSalário do funcionário:\033[m '))
if sal <= 1250:
    novoSal = sal + (sal * 15 / 100)
else:
    novoSal = sal + (sal * 10 / 100)
print(f'\n\033[36mOlá {nome}, estamos analisando seus dados. \n\033[32mProcessando...\033[m')
sleep(3)
print(f'\033[37;1mSalário atual: R${sal:.2f} \nSalário novo: R${novoSal:.2f}\033[m')
print('\033[36mObrigado e tenha um bom dia!\033[m')