'''
count - Itertools
O contador infinito build-in do Python
'''

from itertools import count

contador = count()  #Nesse caso temos um contador infinito

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

# Usando o count e a função zip é possivel fazer a mesma coisa que fizemos usando o ennumerate
contador = count(start = 10, step = 10)
nomes = ['Leonardo', 'Karine', 'Lucas', 'Shewps']

print(list(zip(contador, nomes)))
