import os
import pandas as pd
#Lendo o arquivo da empresa A
arquivos = os.listdir('Compras')
licitacao = pd.read_excel('Compras/Empresa A.xlsx')
licitacao = licitacao.rename(columns={'Total' : 'Empresa A'})
del licitacao['Valor Unitário']
#Lendo os dados de todas as empresa e unindo no mesmo dataframe
empresas = arquivos[1:]
for empresa in empresas:
    file = 'Compras/'+empresa
    proposta = pd.read_excel(file)
    licitacao[empresa[:-5]] = proposta['Total'].copy()
for coluna in licitacao.columns[3:]:
    total = licitacao[coluna].sum()
    print('{} : R$ {}'.format(coluna, total))

#Valor otimo ( Mneor valor para cada item)
licitacao['Mínimo'] = licitacao.drop(['Item', 'Descrição do Item', 'Quantidade'], axis=1).min(axis=1)
Minimo = licitacao['Mínimo'].sum()

#Desvio de cada item para todas as empresas
for empresa in licitacao.columns[3:-1]:
    desvio = licitacao[['Item', 'Descrição do Item', empresa, 'Mínimo']]
    desvio['Delta'] = desvio[empresa]-desvio['Mínimo']
    desvio.to_excel('Compras/Desvio -'+ empresa +'.xlsx', index=False)