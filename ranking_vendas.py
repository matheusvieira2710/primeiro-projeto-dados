import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Mouse", "Teclado", "Monitor", "Monitor", "Notebook", "Mouse"],
    "valor": [3500, 50, 120, 4000, 60, 100, 900, 850, 3700, 55]
}

df = pd.DataFrame(dados)

# soma por produto
vendas = df.groupby("produto")["valor"].sum()

# ordenar do maior para o menor
ranking = vendas.sort_values(ascending=False)

print("Ranking de vendas:")
print(ranking)
