# Lendo um inteiro do teclado
numero = int(input('Digite um numero inteiro: '))

# Lendo um float do teclado
numero_real = float(input('Digite um numero real: '))

# Lendo uma string do teclado
nome = input('Digite seu nome: ')

# O separador padrão do print é o espaço, e ele sempre quebra a linha no final
print('O numero inteiro digitado foi:', numero,"O numero real digitado foi:", numero_real, "O nome digitado foi:", nome)

# Posso usar o formatted
# Podemos limitar o numero de casas decimais do float usando :.2f,
# onde 2 é o numero de casas decimais
print(f'O numero inteiro digitado foi: {numero} \nO numero real digitado foi: {numero_real:.2f} \nO nome digitado foi: {nome}')