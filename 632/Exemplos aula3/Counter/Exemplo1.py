from collections import Counter

c1 = Counter('Banana')

print(c1)

c1.update('Abacaxi')

print(c1)

c3 = Counter(a=3, b=2, c=1)
c4 = Counter(a=2, b=1)

c5 = c3 + c4
print(c5)

c6 = c3 - c4
print(c6)
# Counter({'a': 1, 'b': 1, 'c': 1})

# Como as quantidades acabam sendo negativas o Counter acaba vazio
c7 = c4 - c3
print(c7)
# Counter()

# Permite obter as chaves mais comuns do Counter
print(c3.most_common(2))

# Caso queira ignorar letras maiusculas toems que usar o lower() na String
c1.update('ANA'.lower())
print(c1)