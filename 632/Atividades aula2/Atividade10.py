candidatos = {"Ana": 0, "Carlos": 0, "Maria": 0, "Kaio": 0, "Nikole": 0, "Murilo": 0, "William": 999}

print("Candidatos a presidente: Ana, Carlos, Maria, Kaio, Nikole, Murilo e William")
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
