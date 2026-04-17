import sqlalchemy
import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')


#Código omitido

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'


dados = pd.read_csv(url)

#print(dados.head())
#print(dados.columns)


dados.to_sql('clientes', engine, index=False)

inspector= inspect(engine)

#print(inspector.get_table_names())

query = 'SELECT * FROM clientes WHERE Categoria_de_renda = "Empregado" '


empregados = pd.read_sql(query, engine) #lendo uma tabela consulta

#print(empregados)

empregados.to_sql('empregados', con = engine, index= False) #salvando tabela empregados


pd.read_sql_table('empregados', engine) #lendo uma tabela completa


query = 'SELECT * FROM clientes' 

pd.read_sql(query, engine) 

#query = 'DELETE FROM clientes WHERE ID_Cliente=5008804'             # O erro ocorre porque você está tentando executar uma consulta SQL de exclusão 
 ##with engine.connect() as conn:                             #(DELETE FROM Clientes WHERE ID_Cliente=5008804) usando conn.execute(query), mas query é uma string,
           #conn.execute(query)                                               #  e o SQLAlchemy espera um objeto text() 
                                                                                   #para executar comandos SQL diretamente.                                                                        
query = text('DELETE FROM Clientes WHERE ID_Cliente=5008804')

with engine.connect() as conn:
    conn.execute(query)
    conn.commit()  # Necessário para confirmar a alteração no banco de dados

query = text('UPDATE clientes SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808')
with engine.connect() as conn:
    conn.execute(query)
    conn.commit()

print(pd.read_sql_table('clientes', engine))

