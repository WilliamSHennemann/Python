numeros = [12, 7, 25, 8, 14, 33, 10, 5, 18, 21]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Original: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
