num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    cont += 1
    if soma > 500 or cont == 10:
        break
print(cont, soma)