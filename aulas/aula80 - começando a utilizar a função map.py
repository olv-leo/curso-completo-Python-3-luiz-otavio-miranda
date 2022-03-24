from dados_secao3 import produtos, pessoas, lista

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
