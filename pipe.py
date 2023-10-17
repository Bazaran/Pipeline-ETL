import pandas as pd

df =pd.read_csv("dados_produtos.csv")
print(f"\n{df}")

df['Total'] = df['Quantidade'] * df['Valor'] #Soma a QTD * Valor
vendas_total = df.groupby("Produto")["Valor"].sum() #Agrupa o Valor dos produtos e soma o total.
print(f"\nValor Total Vendido:\n{vendas_total}")
vendas_total.to_csv("Total_Vendas.csv") #Criação de Um arquivo CSV com os Totais Vendidos.

