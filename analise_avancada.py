import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Mouse", "Teclado", "Monitor", "Monitor", "Notebook", "Mouse"],
    "valor": [3500, 50, 120, 4000, 60, 100, 900, 850, 3700, 55],
    "quantidade": [1, 3, 2, 1, 2, 1, 1, 1, 1, 2]
}

df = pd.DataFrame(dados)

# faturamento total
faturamento = df["valor"].sum()

# ticket médio
ticket_medio = df["valor"].mean()

# produto mais vendido em quantidade
mais_vendido_qtd = df.groupby("produto")["quantidade"].sum().idxmax()

# produto que mais fatura
mais_fatura = df.groupby("produto")["valor"].sum().idxmax()

print("Faturamento total:", faturamento)
print("Ticket médio:", ticket_medio)
print("Mais vendido (quantidade):", mais_vendido_qtd)
print("Produto que mais fatura:", mais_fatura)
