import pandas as pd
import matplotlib.pyplot as plt # type: ignore



url = '/home/gustavo/Documentos/python/data/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

emissoes_gases = pd.read_excel(url, sheet_name='GEE Estados')

#print(emissoes_gases)
#print(emissoes_gases.info())
#print(emissoes_gases['Emissão / Remoção / Bunker'].unique())

((emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção'))

(emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])])

(emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021])
(emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()) #verifiando o maixo de todas as colunas
(emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker']== 'Bunker', 'Estado'].unique())

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker']=='Emissão']

emissoes_gases = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker') 

#print(emissoes_gases)

emissoes_gases.loc[:,'Nível 1 - Setor':'Produto'].columns

colunas_info = list(emissoes_gases.loc[:, 'Nível 1 - Setor': 'Produto'].columns)

#print(colunas_info)


emissoes_gases.loc[:, 1970:2021].columns

colunas_emissao= list(emissoes_gases.loc[:, 1970:2021].columns)

#print(colunas_emissao)

(emissoes_gases.melt(id_vars=colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name= 'Emissão'))


emissoes_por_ano = emissoes_gases.melt(id_vars=colunas_info, value_vars=colunas_emissao, var_name='Ano', value_name= 'Emissão')

#print(emissoes_por_ano)

emissoes_por_ano.groupby('Gás')

# print(emissoes_por_ano.groupby('Gás').groups) 


#print(emissoes_por_ano.groupby('Gás').get_group('CO2 (t)'))


emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

emissoes_por_gas=emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending= False)

#print(emissoes_por_gas)

emissoes_por_gas.plot(kind = 'barh', figsize= (10,6));

#plt.show()

(emissoes_por_gas.iloc[0:9])

#print(f'A emissao de CO2 correspoe a {float((emissoes_por_gas.iloc[0:9].sum()/emissoes_por_gas.sum()).iloc[0])*100:.2f} % de emissao total de gases estufa no brasil de 1970 a 2021.')


gas_por_setor= emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor' ])[['Emissão']].sum()

#print(gas_por_setor)

(gas_por_setor.xs('CO2 (t)', level= 0))

gas_por_setor.xs('CO2 (t)', level= 0).max()

gas_por_setor.xs('CO2 (t)', level= 0).idxmax()

#print(gas_por_setor.groupby(level=0).idxmax())

#print(gas_por_setor.groupby(level=0).max())

valor_max= gas_por_setor.groupby(level=0).max().values

tabela_sumarizada= gas_por_setor.groupby(level = 0).idxmax()

tabela_sumarizada.insert(1, 'Quantidade de emissão', valor_max)

#print(tabela_sumarizada)

gas_por_setor.swaplevel(0,1)

gas_por_setor.swaplevel(0,1).groupby(level= 0).idxmax()

emissoes_por_ano.groupby('Ano')[['Emissão']].mean().plot(figsize=(10,6))
emissoes_por_ano.groupby('Ano')[['Emissão']].mean().idxmax
emissoes_por_ano.groupby(['Ano','Gás'])[['Emissão']].mean()

media_emissao_anual= emissoes_por_ano.groupby(['Ano', 'Gás'])[['Emissão']].mean().reset_index()
media_emissao_anual= media_emissao_anual.pivot_table(index='Ano', columns='Gás', values='Emissão')
(media_emissao_anual)

media_emissao_anual.plot(subplots= True, figsize=(10,40))

plt.show()
