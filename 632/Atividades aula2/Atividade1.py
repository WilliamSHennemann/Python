numeros = [12, 7, 25, 8, 14, 33, 10, 5, 18, 21]
maior = numeros[0]
menor = numeros[0]

for numero in numeros[1:]:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = sum(numeros) / len(numeros)

print(f"Lista: {numeros}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media:.2f}")
