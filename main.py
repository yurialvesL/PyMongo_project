import pymongo as pym



client = pym.MongoClient("localhost:27017")

lista = client.list_database_names()

db = client["Pytask"]
col = db["tarefas"]

mydoc = col.find()

for chave in mydoc:
    print(chave)
