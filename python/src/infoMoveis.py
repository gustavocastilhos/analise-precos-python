import pandas as pd

import numpy as np

dados = pd.read_json('/home/gustavo/Documentos/python/data/dados_hospedagem.json')

#print(dados.head())

dados = pd.json_normalize(dados['info_moveis'])

#print(dados)

colunas = list(dados.columns)

#print(colunas)

dados= dados.explode(colunas[3:])

#print(dados)

dados.reset_index(inplace = True,drop=True)

print(dados.head())

#print(dados.info())

dados['max_hospedes'].astype(np.int64)

dados['max_hospedes']=dados['max_hospedes'].astype(np.int64)

#print(dados.info())

col_numericas = ['quantidade_banheiros', 'quantidade_camas', 'quantidade_quartos']

dados[col_numericas]= dados[col_numericas].astype(np.int64)

dados['avaliacao_geral']= dados['avaliacao_geral'].astype(np.float64)

#print(dados.info())

dados['preco'].apply(lambda x: x.replace('$','').replace(',','').strip())

dados['preco'] = dados['preco'].apply(lambda x: x.replace('$','').replace(',','').strip())

#print(dados['preco'])

dados['preco']= dados['preco'].astype(np.float64)

#rint(dados.info())

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: x.replace('$','').replace(',','').strip())

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].astype(np.float64)

#print(dados.info())

dados['descricao_local'].str.lower()

dados['descricao_local']=dados['descricao_local'].str.lower()

print(dados.head())








