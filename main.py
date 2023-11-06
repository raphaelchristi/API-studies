import requests
import pandas as pd
from io import StringIO
from chave import chave_api
# No yahoo finance podemos encontrar o symbol de cada empresas 
# Fazer um programa que se conecte ao main.py para obter a data de um único dado symbol
# Usado por exemplo beautiful soup
# Ou ate mesmo uma api para alimentar o SYMBOL
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=MRVL&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
print(tabela)