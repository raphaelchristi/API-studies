import psycopg2

# Conecte-se ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname='seu_banco_de_dados',
    user='seu_usuario',
    password='sua_senha',
    host='localhost'  # Ou o endereço do servidor PostgreSQL
)
# Crie um cursor
cur = conn.cursor()

# Suponhamos que 'df' seja o DataFrame com os dados limpos
# Use 'to_sql' do pandas para inserir dados diretamente no banco de dados
df.to_sql('tabela_destino', conn, if_exists='replace', index=False)

# Commit e feche a conexão
conn.commit()
conn.close()
