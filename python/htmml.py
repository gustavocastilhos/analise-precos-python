import pandas as pd 


dados_html =  pd.read_html('/home/gustavo/Documentos/python/wiki.html')

print(dados_html)


print(len(dados_html))

top_filmes = dados_html[1]

print(top_filmes)


top_filmes.to_html('top_filmes.html') #salvando em html

top_filmes.to_csv('top_filmes_csv.csv', index=False) #salvando em csv

print(pd.read_csv('/home/gustavo/Documentos/python/top_filmes_csv.csv')) #verifando

