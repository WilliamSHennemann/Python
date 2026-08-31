cont = 0

while cont < 10:
    print(cont, end=' ')
    cont += 1

numero = int(input('Digite um numero entre 1 e 10: '))

while numero < 1 or numero > 10:
    numero = int(input('Digite um numero entre 1 e 10: '))

cont = 1
while cont <= 10:
    print(f'{numero} x {cont} = {numero*cont}')
    cont += 1