'''
Aritimeticos
+ -> soma
- -> subtração
* -> multiplicação
/ -> divisão normal
// -> divisão inteira
% -> resto da divisão
** -> exponenciação
pow(base, expoente) -> exponenciação
'''

n1 = int(input('Digite o primeiro numero : '))
n2 = int(input('Digite o segundo numero : '))

soma = n1 + n2
print(f'A soma de {n1} + {n2} = {soma}')

subtracao = n1 - n2
print(f'A subtração de {n1} - {n2} = {subtracao}')

multiplicacao = n1 * n2
print(f'A multiplicação de {n1} * {n2} = {multiplicacao}')

divisao = n1 / n2
print(f'A divisão de {n1} / {n2} = {divisao}')

divisao_inteira = n1 // n2
print(f'A divisão inteira de {n1} // {n2} = {divisao_inteira}')

resto = n1 % n2
print(f'O resto da divisão de {n1} % {n2} = {resto}')

exponenciacao = n1 ** n2
print(f'A exponenciação de {n1} ^ {n2} = {exponenciacao}')

exponenciacao_pow = pow(n1, n2)
print(f'A exponenciação de {n1} ^ {n2} = {exponenciacao_pow}')


'''
atribuição simplificada
a += b -> a = a + b
a -= b -> a = a - b
a *= b -> a = a * b
a /= b -> a = a / b
a //= b -> a = a // b
a %= b -> a = a % b
'''