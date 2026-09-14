candidatos = {"Ana": 0, "Carlos": 0, "Maria": 0}

print("Candidatos: Ana, Carlos e Maria")
while True:
    voto = input("Digite o candidato ou 'fim': ")
    if voto.lower() == "fim":
        break
    if voto in candidatos:
        candidatos[voto] += 1
    else:
        print("Candidato invalido.")

maior_votos = -1
vencedor = ""
for candidato, votos in candidatos.items():
    print(f"{candidato}: {votos} votos")
    if votos > maior_votos:
        maior_votos = votos
        vencedor = candidato

print(f"Vencedor: {vencedor}")
