import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Mouse", "Teclado", "Monitor", "Monitor", "Notebook", "Mouse"],
    "valor": [3500, 50, 120, 4000, 60, 100, 900, 850, 3700, 55]
}

df = pd.DataFrame(dados)

# soma por produto
vendas = df.groupby("produto")["valor"].sum()

# gráfico
vendas.plot(kind="bar")

plt.title("Total de vendas por produto")
plt.ylabel("Valor")
plt.xlabel("Produto")

plt.show()
