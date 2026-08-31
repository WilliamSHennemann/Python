# for (int i = 0; i < 10; i++) {
# o range não é inclusivo, oque significa que ele testa sempre < que
for i in range(10):
    print(i, end=' ')

# A funçaõ range tem tres parametros(inicial, final, passo)
# se omitido o inicial é 0, o final o teste é sempre menor que e o passo é 1 ou seja i+=1
print('\nOutro exemplo')
# for (int i = -10; i < 0; i+=2) {
for i in range(-10, 0, 2):
    print(i, end=' ')
