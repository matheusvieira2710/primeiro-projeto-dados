import pandas as pd

dados = {
    "produto": ["A", "B", "A", "C"],
    "valor": [100, 200, 150, 300]
}

df = pd.DataFrame(dados)

total = df["valor"].sum()
media = df["valor"].mean()

print("Total:", total)
print("Média:", media)
