import pandas as pd
import matplotlib.pyplot as plt



url = url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

#print(pd.read_csv(url))
(pd.read_csv(url, sep = ';'))

dados = (pd.read_csv(url, sep = ';'))

#print(dados.head(10)) #10 primeiras linhas
#print(dados.tail()) #ultimas linhas
#print(dados.shape)
#print(dados.columns)
#print(dados.info())
#print(dados['Bairro'])
#print(dados[['Quartos','Valor']])

#print(dados.head())

media = (dados['Valor'].mean()) #media total da coluna valor

#print(dados.groupby('Tipo').mean(numeric_only=True))#agrupando com, base em uma coluna especifica #numeric only é pra ele ser aplicado apenas as colunas numericas

valor = dados.groupby('Tipo')['Valor'].mean() #tirei a numericc only, pq ja estou especificando a coluna que quero vizualizar

valorOrdem = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')  #vizualizando em ordem 

valorOrdem.plot(kind='barh', figsize=(14, 10), color =  'purple')

#plt.show()

#print(dados.Tipo.unique())

imoveis_comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

#print(dados.query('@imoveis_comerciais in Tipo') )

df = (dados.query('@imoveis_comerciais not in Tipo') )

#print(df.head)

             #> mudei agr pra apenas os imoveis
valorOrdem = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')  #vizualizando em ordem 

valorOrdem.plot(kind='barh', figsize=(14, 10), color =  'purple')

#plt.show()
#print(df.Tipo.unique())

(df.Tipo.value_counts()) #contando a quantidade de cada imovel
(df.Tipo.value_counts( normalize= True)) #contando em porcentagem
(df.Tipo.value_counts( normalize= True).to_frame()) #melhorando vizualização
(df.Tipo.value_counts(normalize= True).to_frame().sort_values('Tipo')) #oradenando do menor pro maior

dfPercentual = (df.Tipo.value_counts(normalize= True).to_frame().sort_values(by='Tipo'))
 

dfPercentual.plot(kind='bar', figsize=(14, 10), color ='green', edgecolor='black',
                        xlabel = 'Tipos', ylabel = 'Percentual')

#plt.show()


df.query('Tipo ==  "Apartamento"')

df = df.query('Tipo== "Apartamento"')

#print(df.head())

#print(df.isnull())

#print(df.isnull().sum()) 

df = (df.fillna(0))

#print(df)
#print(df.isnull().sum()) 

#df.query('Valor== 0 | Condominio==0')

(df.query('Valor== 0 | Condominio==0').index)

registrosAremover= df.query('Valor== 0 | Condominio==0').index

df.drop(registrosAremover, axis=0, inplace= True) 

#print(df.head())
#print(df.Tipo.unique)

(df.drop('Tipo', axis=1 , inplace=True))

#print(df.head())

#print(df['Quartos']== 1)

selecao1=(df['Quartos']== 1)
df[selecao1]

selecao2 = df['Valor'] < 1200
df[selecao2]

selecaoFinal = (selecao2) & (selecao1)
df[selecaoFinal]

#print(df[selecaoFinal])

df1=df[selecaoFinal]

selecao = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)

#print(df[selecao])

df2=df[selecao]

#df.to_csv('dados_apartamento.csv') #salvando arquivo

#print(pd.read_csv('dados_apartamento.csv'))#verificando arquivo ;;; unnamed encontrado

df.to_csv('dados_apartamento.csv', index= False, sep=';') #arrumando arquivo + separando ele em ;

#print(pd.read_csv('dados_apartamento.csv' , sep=';'))
dados['Valor_por_mes']= dados['Valor'] + dados['Condominio']


dados['Valor_por_ano'] = dados['Valor_por_mes'] *12 + dados['IPTU'] 

#print(dados.head())

dados['Descricao'] = dados['Tipo']+ ' em ' + dados['Bairro']

#print(dados.head())

dados['Descricao'] = dados['Tipo']+ ' em ' + dados['Bairro']+ ' com ' + dados['Quartos'].astype(str) + ' quarto(s) e ' + dados['Vagas'].astype(str) + ' Vaga(s) de garagem'

#print(dados.head())


dados['Possui_Suite'] = dados['Suites'].apply(lambda x: 'Sim' if x > 0 else 'Não')

#print(dados.head())

dados.to_csv('dados_completos.csv', index= False, sep=';')

#print(pd.read_csv('dados_completos.csv', sep=';'))