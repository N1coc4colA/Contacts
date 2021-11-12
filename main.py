from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') 
def home():
    '''
    ceci est le debut de la page c'est a dire le fichier ooof.html

    '''
    return render_template("ooof.html")

@app.route("/add")
def add():
    '''
    ceci est la page d'ajout c'est a dire le fichier first.html

    '''
    return render_template("first.html")

@app.route("/liste")
def liste():
    '''
    ceci est la page liste c'est a dire le fichier index.html
    '''
    return render_template("index.html")

@app.route("/supr")
def supr():
    '''
    ceci est censer etre le debut de la page suprimer un contact 

    '''
    return ("ptdr y a rien")

if __name__ == "__main__":
    app.run()
