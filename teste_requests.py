# #############################################################################
import requests

# GET #########################################################################

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Obtém os dados da resposta como JSON (se aplicável)
    print(data)
else:
    print("Erro na requisição:", response.status_code)


# POST ########################################################################

url = "https://api.example.com/endpoint"
data = {"chave": "valor"}  # Dados a serem enviados no corpo da requisição

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Requisição POST bem-sucedida!")
else:
    print("Erro na requisição:", response.status_code)
