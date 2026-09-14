# Copiando listas
la = [1,2,3,4,5,6]
# Se atribuirmos uma lista a outra, as duas apontam para o
# mesmo endereço de memória
#alterando uma, altera as duas
# lb = la

# Realizando uma copia de todos os elementos
lb = la[:]

print(f'Elementos em la: {la}')
print(f'Elementos em lb: {lb}')

lb[2] = 25

print(f'Elementos em la: {la}')
print(f'Elementos em lb: {lb}')

la = [1,2,3,4,5,6,7,8,9]

# Copiando parcialmente
# Realzando uma copia do inicio de la até o indice 5, ou seja, os elementos de 0 a 4
lb = la[:5]

print(f'Elementos em la: {la}')
print(f'Elementos em lb: {lb}')

# Copiando parcialmente
# Realizando uma copia do indice 2 até o final da lista
lb = la[2:]

print(f'Copiadas as posições de 2 até o final da lista: {lb}')

# Realizando do indice 2 até o indice 5
# lembrando que para incluir o 5, precisamos colocar 6, pois o range não é inclusivo
lb = la[2:6]

print(f'Copiadas as posições de 2 até o 5 da lista: {lb}')

# Acessando a ultima posição da lista
print(f'Ultimo elemento da lista: {la[-1]}')