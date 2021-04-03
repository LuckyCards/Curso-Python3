num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
subtração = num1 - num2
divisão = num1 / num2
produto = num1 * num2
potência = num1 ** num2
divisãoInt = num1 // num2
restoDivisão = num1 % num2
print('Resultados Felizes :)\n \nVeja os resultados:')
print(f'{"Soma:":.<20} {soma}')
print(f'{"Subtração:":.<20} {subtração}')
print(f'{"Produto:":.<20} {produto}')
print(f'{"Divisão:":.<20} {divisão}')
print(f'{"Divisão Inteira:":.<20} {divisãoInt}')
print(f'{"Resto da Divisão:":.<20} {restoDivisão}')
print(f'{"Potência:":.<20} {potência}')