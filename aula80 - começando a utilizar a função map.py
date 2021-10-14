produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 14},
    {'nome': 'p3', 'preco': 15},
    {'nome': 'p4', 'preco': 16},
    {'nome': 'p5', 'preco': 17},
    {'nome': 'p6', 'preco': 18},
    {'nome': 'p7', 'preco': 19},
    {'nome': 'p8', 'preco': 20},
]

pessoas = [
    {'nome': 'Leonardo', 'idade': 24},
    {'nome': 'Karine', 'idade': 22},
    {'nome': 'Lucas', 'idade': 22},
    {'nome': 'Bino', 'idade': 23},
    {'nome': 'João', 'idade': 23},
]

lista = [1, 2, 3, 4, 5, 6]

# Multiplica todos elementos da lista por 2
nova_lista = map(lambda x: x * 2, lista)
print(nova_lista)  # Retorna um objeto iteravel por isso precisamos converter para lista
print(list(nova_lista))

# Modificando o preço dos produtos do dicionário
def modificar_preco(p):
    p['preco'] *= 1.5
    return p

prod = map(modificar_preco, produtos)
print(list(prod))

# Criando uma lista só com o nome das pessoas
nomes = map(lambda x: x['nome'], pessoas)
print(list(nomes))