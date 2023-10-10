import requests, json

consulta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

print(consulta.json()['USDBRL']['bid'])
