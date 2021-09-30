"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product
pessoas = ['Leo', 'Karine', 'Lucas', 'Leticia', 'Mirele']
print('COMBINATIONS')
for grupo in combinations(pessoas, 2):
    print(grupo)
print()

print('PERMUTATIONS')
for grupo in permutations(pessoas, 2):
    print(grupo)
print()

print('PRODUCT')
for grupo in product(pessoas, repeat=2):
    print(grupo)