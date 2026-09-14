aluno = {
    "nome": "Joao",
    "idade": 18,
    "curso": "Informatica",
    "nota": 8.5,
}

for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")

situacao = "aprovado" if aluno["nota"] >= 6 else "reprovado"
print(f"Situacao: {situacao}")
