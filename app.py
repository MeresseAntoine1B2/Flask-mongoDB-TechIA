from flask import Flask, render_template, redirect, url_for, request, session
from formulaires import Connexion, RegistrationForm, Ajout_article
from formulaires import Connexion, RegistrationForm,CommentaireForm
from pymongo import MongoClient
from wtforms import Form, BooleanField, StringField, validators, EmailField, SubmitField
from datetime import datetime 


app = Flask(__name__)
url = "mongodb://localhost:27017"
client = MongoClient(url)

app.config['SECRET_KEY'] = 'Secret'


db = client.blog
articles = db.article  # une collection article
users = db.user
admins = db.admin    


@app.route("/", methods = ['GET','POST'])
def accueil():
    try:
        login = session["username"]
    except:
        login = None

    return render_template("accueil.html", articles = articles.find(), login=login)

@app.route('/article/<titre>',methods = ['GET','POST'])
def article(titre): 
    form =CommentaireForm()
    if form.validate_on_submit():
        new_commentaire = {
            "user" : session["username"],
            "date" : str(datetime.now()),
            "texte": form.data["commentaire"],
            }
        article_page = articles.find_one({"titre":titre})
        article_page["commentaires"].append(new_commentaire)
        articles.update_one({"titre":titre},{"$set":{"commentaires":article_page["commentaires"]}})

    return render_template("article.html", form=form, article=articles.find_one({"titre":titre}))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = Connexion()
    if form.validate_on_submit(): #si login et mdp sont input au bon format 
        user = users.find_one({"nom" : form.data["username"],"mdp" : form.data["password"]}) #variable user qui tente de se connecter 
        if user is not None: # si l'utilisateur est dans la bdd 
            session["username"] = form.data["username"] # alors il se connecte 

            return redirect(url_for("accueil")) # on le redirige vers l'accueil 
        else: 
            return redirect(url_for("register")) #sinon on lui demande de créer un compte
    return render_template("login.html", form=form) # si le login et mdp sont input au mauvais format alors la page login se refresh 


@app.route('/admin', methods = ['GET', 'POST']) # FONCTION ADMIN DANS LOGIN ET APP ROUTE ADMIN A PART
def admin():
    form = Ajout_article()

    if session["username"] is not None: #si la session est active 
        utilisateur = users.find_one({"nom": session["username"]}) #variable utilisateur
        if utilisateur["admin"]: 
            if form.validate_on_submit():
                new_article = {
                    "titre" : form.data["titre"],
                    "résumé": form.data["résumé"],
                    "texte": form.data["texte"]
                }
                articles.insert_one(new_article)
            return render_template("admin.html", form=form)
        return render_template("accueil.html")
    return render_template("login.html")
        

@app.route('/admin/valider_comment/<nom>/<num_comm>')
def valider_comment(nom,num_comm):
    if session["username"] is not None:
        utilisateur = users.find_one({"nom": session["username"]})
        if utilisateur["admin"]: 
            article_selectionne = articles.find_one({"titre" : nom})
            liste_comm = article_selectionne["commentaires"]
            liste_comm[int(num_comm)]["validé"] = True  #.pop pour supprimer
            article.update_one({"titre" : nom},{"$set" : {"commentaires" : article["commentaire"]}})
    
    

#maj kamel

@app.route('/register', methods=['GET', 'POST']) #get = utilisateur qui récupere  #post = utilisateur qui envoie 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = {
            "nom" : form.data["username"],
            "mdp" : form.data["password"],
            "mail" : form.data["email"],
            "admin" : False
        }
        if users.find_one({"nom" : form.data["username"]}) is None and users.find_one({"mail" : form.data["email"]}) is None :
            users.insert_one(new_user)
            return redirect(url_for("login"))
        else:   
            return render_template('register.html', form=form)
    return render_template('register.html', form=form)
