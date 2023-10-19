import requests, json

cnpj = input(f"Informe o CNPJ: ")
consulta = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")

if consulta.status_code == 200:
    print(f"Razão social: {consulta.json()['razao_social']}")
    print(f"Nome fantasia: {consulta.json()['nome_fantasia']}")
    print(f"Municipio: {consulta.json()['municipio']}")
    print(f"Estado: {consulta.json()['uf']}")
else:
    print("ERRO! Cep inválido!")