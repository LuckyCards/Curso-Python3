from unidecode import unidecode #removedor de acentuações :)
print(f'\033[33m{"—"*30:^30}\033[m')
print(f'\033[36m{"EXERCÍCIO Nº 26":^30}\033[m')
print(f'\033[33m{"—"*30:^30}\033[m')
frase = str(unidecode(input('Digite uma frase: '))).strip().upper()
print(f'Quantas letras A? {frase.count("A")}')
print(f'\033[1mPrimeira\033[m aparição da letra A: {frase.find("A") + 1}')
print(f'\033[1mUltima\033[m aparição da letra A: {frase.rfind("A") + 1}')