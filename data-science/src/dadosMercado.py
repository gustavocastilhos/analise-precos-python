import pandas as pd

url= 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'

dados_mercado = pd.read_csv(url)

#dados_mercado = pd.read_csv(url, sep=';') para arquivos separados por ponto e virgula(;)
#print(dados_mercado.head())

dados_selecao= pd.read_csv(url, usecols=[0,1,4])

#print(dados_selecao)

dados_selecao.to_csv('clientes_mercado.csv', index= False)

#print(pd.read_csv('/home/gustavo/Documentos/python/clientes_mercado.csv'))

url2= 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados_selecao2= pd.read_excel(url2)

#print(dados_selecao2.head())

#print((pd.ExcelFile(url2).sheet_names))#verificando quantidade de paginas e nomes

percapita = pd.read_excel(url2, sheet_name= 'emissoes_percapita')
#print(percapita.head())

fontes = pd.read_excel(url2, sheet_name= 'fontes')
#print(fontes.head())

intervalo = pd.read_excel(url2, sheet_name='emissoes_percapita', usecols= 'A:D', nrows=10)

#print(intervalo)

percapita.to_excel('co2_percapita.xlsx', index= False)
                   