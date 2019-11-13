#
from flask import render_template, request, url_for
# Nous avons ici importé url_for pour créer des URL qui renvoient à nos fonctions et à nos pages HTML
# Import url_for in order to create URLS sending back functions for the HTML pages
from .main import app
import random
from datetime import datetime


@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.context_processor
def inject_now():
    return {'now' : datetime.now()}


# Use the render_template function so that it follows the template's path and the arguments

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/contact")
def contact():
    return render_template('pages/contact.html')



@app.route("/equipe")
def equipe():
    return render_template('pages/equipe.html')
