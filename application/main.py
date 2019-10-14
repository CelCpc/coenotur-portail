
from flask import Flask, request
# Nous avons ensuite importé SQLAlchemy afin de pouvoir travailler sur notre base de données via notre application Python.
# We imported SQLAlchemy to work on our database via the Python application

from flask_sqlalchemy import SQLAlchemy


import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")


# Nous avons instancié  flask
# initialize the application by instancing flask

app = Flask("Coenotur", template_folder=templates, static_folder=statics)

#grâce à la configuration debug = True, si nous avons une erreur, la page montrera les détails de cette erreur

# configuration of debug = True so that whenever we get an error, details are shown on the landing page

app.config['DEBUG'] = True
# La seule configuration dont nous avons eu besoin était la Database_URI.
# Nous avons configuré notre base de données en indiquant le chemin vers notre
# database qui s'intitule "".

# The only configuration we needed here was Database_URI
# we configured our database by pointing out the path leading to our database
# entitled ""


# Nous avons instancié flask-SQLAlchemy par la commande suivante :

# intialize the database and instancing flask-SQLAlchemy by the following command :

# A partir de ces quelques manipulations, nous avons pu créer notre base de données.

# After some manipulations we were able to create our database


# La ligne de code suivante nous a permis de remplir notre base de données à partir d'une base vide.


# import the different routes
import application.routes