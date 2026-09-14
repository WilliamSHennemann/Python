# Adicionando elementos a uma lista

lista = []

# A função append adiciona elementos ao final da lista
lista.append('a')

# Lendo uma lista do teclado
for i in range(10):
    num = input(f'Digite o {i+1}º elemento da lista: ')
    lista.append(num)

print(f'Elementos da lista: {lista}')

#

la = [1,2,3,4,5,6]
lb = [7,8,9,10]

la.append(lb)

# [1, 2, 3, 4, 5, 6, [7, 8, 9, 10] ]