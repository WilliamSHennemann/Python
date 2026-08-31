'''
Operadores relacionas
< : Menor que
> : Maior que
<= : Menor ou igual que
>= : Maior ou igual que
== : Igual a
!= : Diferente de
'''

'''
Operadores logicos
E -> && -> and
OU -> || -> or
Não -> ! -> not
'''

a = True
b = False

print(not (a or b))

# Usando o if em python
Numero = int(input('Digite um numero inteiro: '))

if Numero == 0:
    print('O numero digitado é igual a zero')

elif Numero > 0:
    print('O numero digitado é maior que zero')
else:
    print('O numero digitado é menor que zero')