from pymongo import MongoClient
from pprint import PrettyPrinter, pprint , PrettyPrinter
client=MongoClient(host='localhost',port=27017)
# print(client)
dbTest=client['test']
people=dbTest['People']
# print(people)
print(dbTest)


people.insert([
                {'name':'Ghobad','family':'Soltani','age':32,'avg':17.87},
                {'name':'Ahmad','family':'Asgari','age':31,'avg':16.87},
                {'name':'Arash','family':'Heidari','age':30,'avg':15.87}
              ])

for doc in people.find():
    print(doc)

for doc in people.find({'name':'Ghonbad'}):
    pprint(doc)

for doc in people.find({'name':'Gobad'}):
    PrettyPrinter(indent=4 , sort=True)
    pprint(doc)

print(people.find().count())

print(people.find().limit(2))

people.update({'family':'Soltani'},{'$set':{'name':'soltan','avg':18}})

people.remove({'name': 'Arash'})


client.close()














