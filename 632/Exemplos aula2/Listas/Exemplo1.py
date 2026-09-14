# Para criar uma lista em python
# Aumenta sozinha, não sendo necessário definir o tamanho da lista
# Como o Python não é tipado, as listas podem conter elementos de tipos diferentes
lista = []

#Criando uma lista com elementos
lista = [1, 2, 3, 4, 5]

# Iterando uma lista
print('O tamanho da lista é: ', len(lista))

i = 0
print('\nIterando a lista com while simples')
while i < len(lista):
    print(lista[i], end=' ')
    i += 1

print('\nIterando a lista com for....range')
for i in range(len(lista)):
    print(lista[i], end=' ')

print('\nIterando a lista com for simplificado')
for i in lista:
    print(i, end=' ')

print(f'\nImprimir a lista diretamente no print: {lista}')