from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, cast
from sqlalchemy.orm import backref
from sqlalchemy.dialects.postgresql import INET

from flask_login import LoginManager
import os
import os.path
from .constantes import SECRET_KEY



chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
chemin_db = os.path.join(chemin_actuel, "db_coenotur")



# Nous avons instancié  flask
# initialize the application by instancing flask
app = Flask("Coenotur", template_folder = templates, static_folder = statics)

#grâce à la configuration debug = True, si nous avons une erreur, la page montrera les détails de cette erreur

# configuration of debug = True so that whenever we get an error, details are shown on the landing page

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db_coenotur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

login = LoginManager(app)
# import the different routes
import application.routes



from .routes import accueil, connexion, deconnexion, about