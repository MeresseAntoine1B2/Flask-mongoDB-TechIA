from tokenize import String
from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField, SubmitField


class Connexion(FlaskForm):
    username = StringField("login")
    password = PasswordField("password")
    submit = SubmitField("Se connecter")


class RegistrationForm(FlaskForm):
    username = StringField('Nom:', [validators.Length(min=4, max=25)])
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Mot de passe:', [
        validators.DataRequired()
    ])
    submit = SubmitField("Créer votre compte")

class Ajout_article(FlaskForm):
    titre = StringField('Titre:', [validators.Length(min=4, max=60)])
    résumé = StringField('Résumé:', [validators.Length(min=4, max=60)])
    texte = StringField('Texte', [validators.Length(min=4, max=60)])
    submit = SubmitField("Créer votre article")

class CommentaireForm(FlaskForm):
    
    commentaire = StringField('commentaire:')
   
    submit = SubmitField("envoyer le commentaire")
    
