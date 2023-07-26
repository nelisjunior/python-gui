import pyodbc

# Configurações de conexão com o banco de dados SQL Server
server_name = 'E1021-D0W\MSSQLSERVER_DEV'
database_name = 'BGSINTESE.dbo'
user_name = 'sa'
password = 'Curso-Alura-ETL2023'

# String de conexão
connection_string = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={user_name};PWD={password}'

# Conexão com o banco de dados SQL Server
con = pyodbc.connect(connection_string)

# Define o cursor para executar comandos SQL
cursor = con.cursor()

# Exemplo de consulta para selecionar todos os dados de uma tabela chamada 'tabela_exemplo'
cursor.execute('SELECT * FROM tabela_exemplo')

# Obtém os resultados da consulta
dados = cursor.fetchall()

# Fecha a conexão com o banco de dados
con.close()

# Exibe os dados obtidos
for linha in dados:
    print(linha)
