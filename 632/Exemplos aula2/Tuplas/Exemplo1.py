# Definindo uma tupla
# Sao imutaveis, ou seja, não podem ser alteradas depois de criadas
ta = (2,1,)

# Elas podem ser mistas
tb = ('Jonas',1.8,[30,42,100], True)

# Para declar uma tupla com apenas um elemento, é necessário colocar uma virgula no final
tc = (37,)

# Desempacotando uma tupla
x,y = ta
print(f'Valores desempacotados da tupla ta: x = {x}, y = {y}')

# Ler os elementos de uma tupla
print(f'Elemento 0 da tupla tb é: {tb[0]}')

tb = (3,4)

tc = ta + tb
print(f'Tupla {ta} + {tb} = {tc}')

# Apenas tem que lembrar que são imutaveis
# ta[0] = 10 não pode ser executada