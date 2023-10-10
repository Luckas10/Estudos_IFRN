import requests

mensagemWeb = requests.get("https://www.ricardokleber.com.br/mensagem.json")

print(mensagemWeb)

print(mensagemWeb.status_code)

print(type(mensagemWeb.text))
print(type(mensagemWeb.json()))

print(mensagemWeb.text)
print(mensagemWeb.json())