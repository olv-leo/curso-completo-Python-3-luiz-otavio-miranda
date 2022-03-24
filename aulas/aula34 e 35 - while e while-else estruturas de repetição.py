'''
while em Python
'''

# Exemplo geral
x = 0
while x < 4:
    print(x)
    x = x + 1
print('acabou')


# Se eu quiser fazer um while pulando o número 3 por exemplo posso usar o 'continue'
x = 0
while x < 8:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print('acabou')

# Podemos usar também o 'break' para interromper um while
x = 0
while x < 8:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('acabou')

# Podemos também usar um while dentro de outr

x = 0  # coluna


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1
    print('')

print('Acabou')

# Crinado uma calculador com o while

while True:
    print('')
    sair = input('Você deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+, -, / ou *): ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um valor inteiro.')
        continue

    if operador == '+':
        print(int(num_1) + int(num_2))

    elif operador == '-':
        print(int(num_1) - int(num_2))

    elif operador == '*':
        print(int(num_1) * int(num_2))

    elif operador == '/':
        print(int(num_1) / int(num_2))

    else:
        print('Você precisa digitar um operador válido!')


'''
While / Else
contadores
acumuladores
'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
    
print('Isso será executado.')
