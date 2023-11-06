# main.py
from api_requests import get_data
from data_cleaning import clean_data
from database_insert import insert_data

data = get_data()  # Chame a função que faz a solicitação à API
cleaned_data = clean_data(data)  # Chame a função de limpeza
insert_data(cleaned_data)  # Insira os dados limpos no banco de dados
#crud<--