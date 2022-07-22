from collections import UserString
from pymongo import MongoClient
from datetime import datetime 

url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client.blog
 
articles = db.article  # une collection 
articles.drop() #nettoyer la base de données 

articles.insert_one (
    { "titre" : "Projet Wa-Tor", 
    "résumé" : "A l'aide de vos connaissances en Python et au logiciel Processing, vous simulerez  la vie et les interactions entre une population de proies et de prédateurs dans une mer de forme torique (forme de donuts)" ,
     "date" :str(datetime.now()), 
     "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " , 
    "commentaires":  [{"user": "user1", "date":str(datetime.now()),"texte": "test commentaire1"},
                        {"user": "user2", "date":str(datetime.now()),"texte": "test commentaire2"},
                        {"user": "user3", "date":str(datetime.now()),"texte": "test commentaire3"}
                        ]}) 
   

articles.insert_one (
 {"titre" : "Logiciel d'Histoires Participatif" , 
 "résumé" : "Le site communautaire Reddit, habitué des défis collaboratifs, a décidé de lancer une nouvelle expérimentation.Cette fois-ci, ils souhaitent regarder ce qui se passe quand on laisse de nombreux internautes écrire une histoire, tous ensemble." ,
  "date" :str(datetime.now()), 
  "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " } )

articles.insert_one ( {"titre" : "Réalisation Blog avec Flask et MongoDB" ,
    "résumé" : "Vous souhaitez réaliser un blog afin de montrer ce que vous avez vu en formation, mais aussi pour partager vos veilles quotidiennes sur le sujet de l'IA, de la data et du développement en général." , 
    "date" :str(datetime.now()), 
    "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " } )


users = db.user # collection users
users.drop()
users.insert_one({ "nom" : "administrateur",
"mdp":"mdp", 
"mail" : "admin@gmail.com" ,
"admin": True })

# afficher la base de données 
# afficher une collection
#curseur = article.find_one({"titre" : "ARTICLE2"})
curseur = article.find({})
print (curseur)

for article in curseur:
    print(article)

