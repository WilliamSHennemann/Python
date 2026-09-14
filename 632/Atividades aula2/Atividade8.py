notas = {"Ana": 8.5, "Carlos": 6.0, "Maria": 9.2, "Joao": 4.5, "Pedro": 7.8}
maior_nota = None
menor_nota = None
aluno_maior_nota = ""

for aluno, nota in notas.items():
    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno
    if menor_nota is None or nota < menor_nota:
        menor_nota = nota

aprovados = [aluno for aluno, nota in notas.items() if nota >= 6]
reprovados = [aluno for aluno, nota in notas.items() if nota < 6]
media = sum(notas.values()) / len(notas)

print(f"Media da turma: {media:.2f}")
print(f"Maior nota: {maior_nota:.1f}")
print(f"Menor nota: {menor_nota:.1f}")
print(f"Aluno com maior nota: {aluno_maior_nota}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
