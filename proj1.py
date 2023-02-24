import os
import pandas as pd
import plotly.express as px

tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("Vendas")
for arquivo in lista_arquivos:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"Vendas/{arquivo}")
        tabela_total = tabela_total.append(tabela)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_loja = tabela_total.groupby('Loja').sum()
tabela_total = tabela_total.groupby('Produto').sum()
tabela_total = tabela_total[['Quantidade Vendida', 'Faturamento']].sort_values(by='Faturamento', ascending=False)
tabela_loja = tabela_loja[['Faturamento']].sort_values(by='Faturamento', ascending=False)
grafico = px.bar(tabela_loja, x=tabela_loja.index, y='Faturamento')
grafico.show()
