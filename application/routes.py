#
from flask import render_template, request, flash, redirect, url_for
# Nous avons ici importé url_for pour créer des URL qui renvoient à nos fonctions et à nos pages HTML
# Import url_for in order to create URLS sending back functions for the HTML pages
from .main import app
import random
from datetime import datetime
from sqlalchemy import or_, and_
from .modeles.utilisateurs import User
from .constantes import RESULTS_PER_PAGE
from flask_login import login_user, current_user, logout_user


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


@app.route("/register", methods=["GET", "POST"])
def inscription():
    """ Route gérant les inscriptions
    """
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect(url_for("accueil"))
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect(url_for("accueil"))
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect(url_for("accueil"))
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")
    return render_template("pages/connexion.html")


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect(url_for("accueil"))
