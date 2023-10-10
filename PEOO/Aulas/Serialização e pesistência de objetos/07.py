import json

arq = open("Agenda.json", "r")

agenda = json.load(arq)

print(agenda)
