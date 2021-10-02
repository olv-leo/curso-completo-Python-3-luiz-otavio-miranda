from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'B'},
]

# A ideia aqui é agrupar os alunos em grupos de acordo com usas notas, para fazer isso vamos usar a função groupby

# A função groupby só funciona com o dicionário ordenado
ordena = lambda x: x['nota']
alunos.sort(key=ordena)

alunos_agrupados = groupby(alunos, ordena)

# A variável 'alunos_agrupados' é um iterador logo quando usada vai se 'esvaziando' é possível contornar isso:
# Usando listas
print(15*'-')
print('USANDO LISTA')
print(15*'-')
for nota, grupo_de_alunos in alunos_agrupados:
    valores = list(grupo_de_alunos)
    quantidade = len(valores)

    print(f'Grupo: {nota} ({quantidade} alunos)')
    for aluno in valores:
        print(f'\t{aluno}')
print()

# Usando tee
print(15*'-')
print('USANDO TEE')
print(15*'-')
from itertools import tee  # tee duplica a variável fornecida
alunos_agrupados = groupby(alunos, ordena)
for nota, grupo_de_alunos in alunos_agrupados:
    v1, v2 = tee(grupo_de_alunos)
    quantidade = len(list(v1))

    print(f'Grupo: {nota} ({quantidade} alunos)')
    for aluno in v2:
        print(f'\t{aluno}')


