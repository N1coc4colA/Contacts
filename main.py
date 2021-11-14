from flask import Flask, render_template
import sqlite3

class DB:
	db = None
	_inst = None

	def instance():
		if (DB._inst == None):
			DB._inst = DB();
		return DB._inst

	def __init__(self):
		self.db = sqlite3.connect("livres_db")
		self.cursor = self.db.cursor()

app = Flask(__name__)

def htmlify(cursor):
	"""
	Transform raw SQL data into a beautiful HTML text that can be inserted into a page.

	"""
	out = ""
	return out

def remove_by_id(id):
    """
    Remove data from the DB by using its ID

    """

def get_initials(name):
	"""
	Generate a string like Asap Arnash -> Aa
	"""
	v = name.split(" ")
	out = ""
	if (l == 0):
		out = "?"
	if (l >= 2):
		if (len(v[1]) == 0):
			out = v[0][0]
		else:
			out = v[0][0] + v[1][0]
	else:
		out=v[0][0]
		if (len(v[0]) != 0):
			out += v[0][1]
	return out

def get_by_id(ID):
	"""
	"""

@app.route('/', methods=["POST"]) 
def home():
	'''
    Renders the home page

    '''
	#Arguments: selection - ID of the data to remove from the DB
	data=request.form
	if (data["selection"]) {
			remove_by_id(int(data["selection"]))
	}
	return render_template("index.html", data=get_list())

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
	data=request.form
    if (request["id"]) {
		infos=get_by_id(int(request["id"]))
		return render_template("add.html", nom=infos["name"], phone=infos["phone"], mail=infos["mail"])
    }
    return render_template("add.html", nom="", phone="", mail="")

@app.route("/view")
def see():
    '''
    Renders the page that shows data about a user

    '''
	#Arguments: id - The ID of the data to be shown from the DB
	data=request.form
	infos = get_by_id(data["id"])
    return render_template("view.html", name=infos["name"], initials=get_initales(infos["name"]), ptype=infos["type"], phone=infos["phone"], mail=infos["mail"])

if __name__ == "__main__":
    app.run()