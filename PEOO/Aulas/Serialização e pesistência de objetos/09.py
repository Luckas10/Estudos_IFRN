import requests
import json

resposta = requests.get("https://api.github.com")

print(resposta.json()["emojis_url"])