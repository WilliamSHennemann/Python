import random

numeros = [random.randint(1, 100) for i in range(10)]

numeros.sort()
maior = numeros[-1]
menor = numeros[0]

media = sum(numeros) / len(numeros)

print(f"Lista: {numeros}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media:.2f}")
