from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
n = count = 0
pc = randint(0, 10)
while True:
    n = int(input('Diga um valor: '))
    i = input('Par ou Ímpar? [P/I] ').strip().upper()
    pc = randint(0, 10)
    s = n + pc
    if i == 'P':
        if s % 2 == 0:
            print('-' * 40)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} deu PAR')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-=' * 20)
            count += 1
        else:
            print(f'Você jogou {n} e o computador {pc}. Total de {s} deu ÍMPAR')
            print('Você PERDEU!')
            print('=-=' * 20)
            print(f'GAMER OVER! Você venceu {count} vezes')
            break
    elif i == 'I':
        if not s % 2 == 0:
            print('-' * 40)
            print(f'Você jogou {n} e o computador {pc}. Total de {s} deu ÍMPAR')
            print('-' * 40)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-='*20)
            count += 1
        else:
            print(f'Você jogou {n} e o computador {pc}. Total de {s} deu PAR')
            print('Você PERDEU!')
            print('=-=' * 20)
            print(f'GAMER OVER! Você venceu {count} vezes')
            break