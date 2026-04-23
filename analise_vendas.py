import pandas as pd

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Mouse", "Teclado", "Monitor", "Monitor", "Notebook", "Mouse"],
    "valor": [3500, 50, 120, 4000, 60, 100, 900, 850, 3700, 55]
}

df = pd.DataFrame(dados)

total = df["valor"].sum()
media = df["valor"].mean()
mais_vendido = df["produto"].value_counts().idxmax()

print("Total de vendas:", total)
print("Média de valor:", media)
print("Produto mais vendido:", mais_vendido)
