"""
Condições IF, ELIF e ELSE
"""

if False:
    print("Verdadeiro.")
elif True:
    print("Agora é verdadeiro.")
else:
    print('Não é verdadeiro.')


'''
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
'''

print(2 == 2)
print(2 == 1)

num_1 = 2
num_2 = '2'
print(num_1 == num_2)  # Tem que ser o mesmo valor e o mesmo tipo

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20  # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar um empréstimo.')
else:
    print(f'{nome} não pode pegar um empréstimo.')


'''
Operadores lógicos
and, or, not, in, not in
'''
# AND
# (Verdadeiro E Verdadeiro) = Verdadeiro | (Verdadeiro E Falso) = Falso

# OR
# (V OU V) = V | (V OU F) = V | (F OU F) = F

# NOT = Inverte a expressão (tradução é não)
a = ''
if not a:
    print('Valor de a vazio')

# IN (tradução como está em)
nome = 'Léo'
if 'o' in nome:
    print('Existe a letra O no seu nome.')

# NOT IN
if 'u' not in nome:
    print('Não existe a letra U no seu nome.')

# EXEMPLO
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválido.')
