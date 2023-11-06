import requests

# URL da API que você deseja acessar
api_url = 'https://exemplo.com/api/dados'

# Faça a solicitação à API
response = requests.get(api_url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()
else:
    print(f"Erro na solicitação à API. Código de status: {response.status_code}")
    data = None

# Agora, você tem os dados da API em 'data'
