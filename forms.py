
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields import *
from wtforms.fields.html5 import *
from wtforms.validators import DataRequired, Length
from wtfpeewee.orm import model_form
from models import User

SimpleConnexionForm = model_form(User)

# Formuaire de connexion
class ConnexionForm(FlaskForm):
    email = EmailField('Email', validators=[
        DataRequired(), Length(min=3, max=50)
    ])
    password = PasswordField('Mot de passe', validators=[
        DataRequired(), Length(min=3, max=50)
    ])

# Formulaire d'inscription
class InscriptionForm(FlaskForm):
    surname = StringField('Nom', validators=[
        DataRequired(), Length(min=3, max=20)
    ])
    name = StringField('Prénom', validators=[
        DataRequired(), Length(min=3, max=20)
    ])
    email = EmailField('Email', validators=[
        DataRequired(), Length(min=3, max=50)
    ])
    password = PasswordField('Mot de passe', validators=[
        DataRequired(), Length(min=3, max=50)
    ])

# Formulaire d'ajout d'un flux
class FluxForm(FlaskForm):
    link = StringField('Lien', validators=[
        DataRequired(), Length(min=3, max=200)
    ])