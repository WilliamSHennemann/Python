# Para definir como conjuntos usamos chaves, assim como nos dicionarios
c1 = {1,2,3,4,5,6,1}

# Conjuntos não permitem repetição
print(c1)

lista = [5,9,7,8,12,3]

print(lista)

# set converte uma lista em um conjunto
# mesmo que a lista esteja desordenada, no conjunto ela vai estar em ordem crescente
c2 = set(lista)

print(c2)

c3 = {1,2,3,4,5,6}
c4 = {4,5,6,7,8,9}

# permite adicionar elementos aso conjuntos
c3.add(7)

print(c3)

# permite remover um elemento, caso ele não exista gera erro
c3.remove(7)

# permite remover um elemento, caso ele não exista o comando é ignorado
c3.discard(10)

print(c3)

c3 = {1,2,3,4,5,6}
c4 = {4,5,6,7,8,9}

# Podemos realizar a união de dois conjuntos
# Poddemos usar a palacra union ou um |
# c5 = c3 | c4
c5 = c3.union(c4)

print(f'{c3} U {c4} = {c5}')

# Podemos realizar a intersecçõ dos conjuntos(separa os elementos comuns aos dois)
# Podemos usar a palavra intersection ou &
# c6 = c3 & c4
c6 = c3.intersection(c4)

print(f'{c3} * {c4} = {c6}')

# Realixando a diferença entre dois conjuntos
# c7 = c3 - c4
c7 = c3.difference(c4)

print(f'{c3} - {c4} = {c7}')

# Realizando a diferença simetrica entre os dois
# Podemos usar diferença de 
# Podemos usar symmetric_difference ou ^
c8 = c3.symmetric_difference(c4)

print(f'{c3} \u2229 {c4} = {c8}')

