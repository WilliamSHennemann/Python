numeros = [4, 7, 4, 2, 9, 7, 1, 2, 9, 5, 4]
sem_repetidos = []

for numero in numeros:
    if numero not in sem_repetidos:
        sem_repetidos.append(numero)

print(f"Resultado: {sem_repetidos}")
