compras = [
    {"cliente": "Ana", "produto": "Mouse", "valor": 50},
    {"cliente": "Bruno", "produto": "Teclado", "valor": 120},
    {"cliente": "Ana", "produto": "Headset", "valor": 150},
    {"cliente": "Carlos", "produto": "Mouse", "valor": 50},
    {"cliente": "Bruno", "produto": "Monitor", "valor": 900},
]
gastos = {}
quantidade_produtos = {}
total_vendas = 0

for compra in compras:
    cliente = compra["cliente"]
    produto = compra["produto"]
    valor = compra["valor"]
    gastos[cliente] = gastos.get(cliente, 0) + valor
    quantidade_produtos[produto] = quantidade_produtos.get(produto, 0) + 1
    total_vendas += valor

maior_gasto = -1
cliente_que_mais_gastou = ""
for cliente, valor in gastos.items():
    if valor > maior_gasto:
        maior_gasto = valor
        cliente_que_mais_gastou = cliente

produto_mais_vendido = ""
maior_quantidade = -1
for produto, quantidade in quantidade_produtos.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        produto_mais_vendido = produto

print(f"Gasto por cliente: {gastos}")
print(f"Quem gastou mais: {cliente_que_mais_gastou} (R$ {maior_gasto:.2f})")
print(f"Valor total das vendas: R$ {total_vendas:.2f}")
print(f"Produto mais frequente: {produto_mais_vendido}")
