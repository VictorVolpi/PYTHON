import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["iPhone 16", "Galaxy A15", "Redmi Note 13", "Moto G84", "POCO X6"],
    "Vendas": [120, 80, 45, 60, 30]
}

df = pd.DataFrame(dados)
print(df)

plt.bar(df["Produto"], df["Vendas"])
plt.title("Vendas por Produto")
plt.show()
