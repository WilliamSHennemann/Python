numeros = [12, 7, 25, 8, 14, 33, 10, 5, 18, 21]
pares = []
impares = []
numeros.sort()

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Original: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")

pares2 = [n for n in numeros if n %2==0]
impares2 = [n for n in numeros if n %2!=0]

print(f"Pares: {pares2}")
print(f"Impares: {impares2}")