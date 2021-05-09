valores = []
maior = menor = 0
for x in range(5):
    valores.append(int(input(f"Digite o valor {x}: ")))
    if x == 0:
        maior = menor = valores[x]
    else:
        if valores[x] > maior:
            maior = valores[x]
        if valores[x] < menor:
            menor = valores[x]
            
print(f"Você digitou os valores: {valores}")
print(f"\no menor valor foi {menor} na posição", end='')
for pos, x in enumerate(valores):
    if x == menor:
       print(f"{pos}...", end='')
print(f"\no maior valor foi {maior} na posição", end='')
for pos, x in enumerate(valores):
    if x == maior:
       print(f"{pos}...", end='')

