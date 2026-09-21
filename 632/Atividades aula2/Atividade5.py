ponto = input('Digite uma codenada: ')
x, y = map(int, ponto.split(','))

if x == 0 and y == 0:
    local = "origem"
elif x == 0:
    local = "eixo Y"
elif y == 0:
    local = "eixo X"
elif x > 0 and y > 0:
    local = "1o quadrante"
elif x < 0 and y > 0: # x < 0 < y
    local = "2o quadrante"
elif x < 0 and y < 0:
    local = "3o quadrante"
else:
    local = "4o quadrante"

print(f"O ponto {ponto} esta no {local}.")
