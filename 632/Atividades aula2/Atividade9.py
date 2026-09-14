alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Carlos": [6.0, 5.5, 7.0],
    "Maria": [9.5, 9.0, 10.0],
    "Kaio": [4.0, 5.0, 6.0],
    "Nikole": [7.5, 8.0, 6.5],
    "Murilo": [5.0, 4.5, 6.0],
    "William": [9.0, 8.5, 7.5],
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if nome == "Carlos":
        situacao = "Aprovado" if media >= 6 else "Reprovado"
    else:
        situacao = "Aprovada" if media >= 6 else "Reprovada"
    print(f"{nome} -> {media:.2f} -> {situacao}")
