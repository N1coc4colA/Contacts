from flask import Flask, render_template

app = Flask(__name__)

def htmlify(cursor):
	"""
	Transform raw SQL data into a beautiful HTML text that can be inserted into a page.
	"""
	out = ""
	return out

@app.route('/') 
def home():
	'''
    Renders the home page

    '''
	#Arguments: selection - ID of the data ro remove from the DB
    return render_template("index.html")

@app.route("/add")
def add():
    '''
    Renders the page used to edit or add a contact

    '''
	#Arguments: id - ID of the data to be modified in the DB (
	#         name - New user name
	#        email - New email address
	#        phone - New phone number
	#         type - New phone type number
    return render_template("add.html")

@app.route("/view")
def suppr():
    '''
    Renders the page that shows data about a user

    '''
	#Arguments: id - The ID of the data to be shown from the DB
    return ("view.html")

if __name__ == "__main__":
    app.run()
