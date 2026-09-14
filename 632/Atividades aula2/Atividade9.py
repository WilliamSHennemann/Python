alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.0, 5.5, 7.0],
    "Maria": [9.5, 9.0, 10.0],
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if nome == "Carlos":
        situacao = "Aprovado" if media >= 6 else "Reprovado"
    else:
        situacao = "Aprovada" if media >= 6 else "Reprovada"
    print(f"{nome} -> {media:.2f} -> {situacao}")
