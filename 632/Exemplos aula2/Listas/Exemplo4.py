# Removendo elementos de uma lista
la = [1,2,3,4,5,6]

# Remove o elemento da posição 4
del la[4]

print(la)

# Remove o elemento 2 ate 4 da lista
del la[1:4]
print(la)

la = [1,2,3,4,5,6]

# Removendo um elemento pelo elemento, ou seja, o valor do elemento
la.remove(3)

la = [1,2,3,4,5,6]
# Verificando se um elemento esta na lista
if 3 in la:
    print('Apagando o elemento 3 na lista')
    la.remove(3)
    print(la)
else:
    print('O elemento 3 não esta na lista')

# Gerando uma lista aleatoria
import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 20))

print(f'Lista gerada aleatoriamente: {lista}')

# Jeito python para gerar uma lista aleatoria

Lista = [random.randint(1, 20) for i in range(10)]
print(f'Lista gerada aleatoriamente: {Lista}')

# Ordenando uma lista

lista.sort()
print(f'Lista ordenada: {lista}')

lista.sort(reverse=True)
print(f'Lista ordenada em ordem decrescente: {lista}')

Lista = [random.randint(1, 20) for i in range(10)]

# Invertendo uma lista
print(f'Lista gerada aleatoriamente: {Lista}')
Lista.reverse()
print(f'Lista invertida: {Lista}')

lista = [1,2,3,4,5,8,7,32,9,3]

# Contando as ocorrencias de um elemento na lista
print(f'O elemento 3 aparece {lista.count(3)} vezes na lista')