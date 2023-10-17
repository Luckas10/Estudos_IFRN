import requests, json

cep = input(f"Informe o CEP: ")
consulta = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")

if consulta.status_code == 200:
    print(f"Rua: {consulta.json()['street']}")
    print(f"Bairro: {consulta.json()['neighborhood']}")
    print(f"Cidade: {consulta.json()['city']}")
    print(f"Estado: {consulta.json()['state']}")
else:
    print("ERRO! Cep inválido!")