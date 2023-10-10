import json

minha_agenda = {"nome": "Chico", "idade":25}

arq = open("Agenda.json", "w")
json.dump(minha_agenda, arq)

