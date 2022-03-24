nome = 'Léo'
idade = 24
altura  = 1.77
peso = 85
e_maior = idade > 18
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}') #.2f é para exibir duas casas do número float
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n= nome, i= idade, im= imc))

'''
DESAFIO
'''

nome = 'Leonardo'
idade = 25
ano_atual = 2021
ano_nascimento = ano_atual - idade
altura = 1.78
peso = 85
imc = peso / altura**2

print(f"{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_nascimento}")
