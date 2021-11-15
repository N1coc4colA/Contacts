#!/usr/bin/python
import sys
from flask import Flask, render_template, request, flash, abort
import sqlite3

global must_verbose

app = Flask(__name__)

if ("-v" in sys.argv) or ("--verbose" in sys.argv):
	must_verbose = True
else:
	must_verbose = False

must_debug = False
if ("-dbg" in sys.argv) or ("--debug" in sys.argv):
	must_debug = True

def verbose(s):
	"""
	In verbose mode or not, this can be useful to see what's called.
	"""
	if (must_verbose):
		print(s)

class DB:
	"""
	This class holds all the DB and manages access to it.
	"""
	db = None
	_inst = None

	def instance():
		"""
		Static method to get the static instance of the class.
		"""
		verbose(__name__)
		if (DB._inst == None):
			DB._inst = DB();
		return DB._inst

	def __init__(self):
		verbose(" > DB.__init__")
		self._hasUpdate=False
		self._dbFail=False
		self.db = sqlite3.connect("contacts_db", check_same_thread=False)
		self.cursor = self.db.cursor()
		self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts'")
		#Ensure the table we'll use is already here or create it!
		if (self.cursor.fetchone()[0] != 1):
			verbose(" > Created new table for contacts")
			#Phone as INTEGER type is not enough :/ (don't ask me why)
			self.cursor.execute('''
			CREATE TABLE contacts (
				Id INTEGER PRIMARY KEY,
				Nom TEXT,
				Prenom TEXT,
				Mail TEXT,
				Phone TEXT,
				PType TEXT,
				Postal TEXT
			)
			''')
		self.db.commit()

	def closeDB(self):
		if (self.cursor):
			self.cursor.close()

	def check_fail(self):
		"""
		Will raise an error if an operation on the DB has failed.
		"""
		verbose(" > Check for fail")
		if (self.cursor.rowcount == 0):
			verbose(" > Abort, content was:")
			verbose(self.cursor.fetchall())
			self._dbFail=True
			abort(500)
		else:
			self._dbFail=False

	def htmlifiedList(self):
		"""
		Transform raw SQL data into a beautiful HTML text that can be inserted into a page. (list of contacts)
		"""
		verbose(" > htmlified")
		out = ""
		self.cursor.execute("SELECT * FROM contacts;")
		self.check_fail()
		data = self.cursor.fetchall()
		i = 0
		for e in data:
			out += "<tr class=\"SE\" data-ptype=\""
			out += str(e[5])
			out += "\"><td><input type=\"checkbox\" name=\"selection\" value=\""
			out += str(e[0])
			out += "\"></td><td><a href=\"view?id="
			out += str(e[0])
			out += "\">"
			out += str(e[1])
			out += "</a></td><td><a href=\"view?id="
			out += str(e[0])
			out += "\">"
			out += str(e[2])
			out += "</a></td></tr>"
		return out

	def remove_by_id(self, id):
		"""
		Remove data from the DB by using its ID
		"""
		verbose(" > remove by id")
		#Never try to remove something twice! It will cause an error :/
		self.cursor.execute("SELECT * FROM contacts WHERE Id = ?", [id])
		if (self.cursor.rowcount != 0):
			requete = "DELETE  FROM contacts  WHERE Id = ?;"
			self.cursor.execute(requete, [id])
			self.check_fail()
			self._hasUpdate=True
			self.db.commit()

	def add_contact(self, content):
		"""
		Adds data to the DB
		"""
		verbose(" > add contact")
		#Disables code injection by using "
		content["name"].replace("\"", "")
		content["surname"].replace("\"", "")
		content["phone"].replace("\"", "")
		content["ptype"].replace("\"", "")
		content["mail"].replace("\"", "")
		content["postal"].replace("\"", "")
		requete = "INSERT INTO contacts (Nom, Prenom, Phone, PType, Mail, Postal) VALUES (\"" + content["name"] + "\",\"" + content["surname"] + "\", \"" + content["phone"] + "\", \"" + content["ptype"] + "\", \"" + content["mail"] + "\", \"" + content["postal"] + "\");"
		self.cursor.execute(requete)
		self.check_fail()
		self._hasUpdate=True
		self.db.commit()

	def update_by_id(self, content, id):
		"""
		Updates the DB content by using the ID used
		"""
		verbose(" > upd by id")
		#Disables code injection by using "
		content["name"].replace("\"", "")
		content["surname"].replace("\"", "")
		content["phone"].replace("\"", "")
		content["ptype"].replace("\"", "")
		content["mail"].replace("\"", "")
		content["postal"].replace("\"", "")
		id = str(id)
		id.replace("\"", "")
		self.cursor.execute("UPDATE contacts SET Nom=\"" + content["name"] + "\", Prenom=\"" + content["surname"] + "\", Phone=\"" + content["phone"] + "\", PType=\"" + content["ptype"] + "\", Postal=\"" + content["postal"] + "\" WHERE Id=" + str(id) + ";")
		self.check_fail()
		self._hasUpdate=True
		self.db.commit()

	def get_by_id(self, id):
		"""
		Get a dict of the data that belongs to a contact
		"""
		verbose(" > get by id")
		self.cursor.execute("SELECT * FROM contacts WHERE Id = ?", [id])
		self.check_fail()
		data = self.cursor.fetchone()
		return {"id":data[0], "name":data[1], "surname":data[2], "mail":data[3], "phone":data[4], "type":data[5], "postal":data[6]}

	def hasUpdates(self):
		"""Just retrieves the property and reset it."""
		tmp = self._hasUpdate
		self._hasUpdate=False
		return "1" if (tmp) else "0"

	def isDBError(self):
		tmp=self._dbFail
		self._dbFail=False
		return tmp


def get_initials(name):
	"""
	Generate a string like Asap Arnash -> Aa. Used with view.html
	"""
	v = name.split(" ")
	l = len(v)
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

def get_data():
	"""
	Returns the arguments of the request.
	"""
	return (request.form if (request.form) else request.args)

@app.route('/', methods=["POST", "GET"]) 
def home():
	'''
	Renders the home page
	'''
	#Arguments: selection - ID of the data to remove from the DB
	#"selection" might be here many times depending on the user's selections.
	verbose(" > home")
	data=get_data()
	if (data):
		data=data.getlist('selection')
		for c in data:
			DB.instance().remove_by_id(c)
	return render_template("index.html", data=DB.instance().htmlifiedList())

@app.route("/updates", methods=["GET"])
def look_on_updates():
	"""
	Used from HTML/Js side to look for updates and then make the page reload.
	"""
	return DB.instance().hasUpdates()

@app.route("/data", methods=["GET"])
def retrieve_data():
	"""
	Returns the htmlified content, useful for in-page updates!
	"""
	return DB.instance().htmlifiedList()

@app.route("/add", methods=["POST", "GET"])
def add():
	'''
	Renders the page used to edit or add a contact
	'''
	#Arguments: id - ID of the data to be modified in the DB (
	#         name - New user name
	#        email - New email address
	#        phone - New phone number
	#         type - New phone type number
	verbose(" > add")
	data=get_data()
	#Be careful! Flask is such vicious! calling data["e"] will raise an error if not in the arguments, have to use smthg else.
	if ("e" in data.keys()):
		#Then it is an update as there's an ID
		if ("id" in data.keys()):
			print("Found the ID")
			DB.instance().update_by_id({"name":data["name"], "surname":data["surname"], "phone":data["phone"], "ptype":data["type"], "mail":data["mail"], "postal":data["postal"]}, data["id"])
		else:
			print("Did not found an ID")
			DB.instance().add_contact({"name":data["name"], "surname":data["surname"], "phone":data["phone"], "ptype":data["type"], "mail":data["mail"], "postal":data["postal"]})
		#Then redirect to origin when that's done! (As it's complicated to do into the Js/HTML)
		return render_template("redirect.html")
	#Just fill with the correct data :)
	if ("id" in data.keys()):
		verbose(" > Editing mode")
		infos=DB.instance().get_by_id(data["id"])
		return render_template("add.html", name=infos["name"], surname=infos["surname"], phone=infos["phone"], mail=infos["mail"], postal=infos["postal"], method="Edition d'un", val=("ami" if (infos["type"]=="ami") else ("travail" if (infos["type"]=="travail") else ("famille" if (infos["type"]=="famille") else "ami"))), next="Appliquer", with_id=("<input name=\"id\" value=\"" + data["id"] + "\" type=\"hidden\"></input>"))
	return render_template("add.html", name="", surname="", phone="", mail="", id="", method="Créer un nouveau", val="ami", next="Ajouter", with_id="")

@app.route("/view", methods=["GET"])
def see():
	'''
	Renders the page that shows data about a user
	'''
	#Arguments: id - The ID of the data to be shown from the DB
	verbose(" > see")
	data=get_data()
	infos=DB.instance().get_by_id(data["id"])
	cn=infos["name"] + " " + infos["surname"]
	return render_template("view.html", name=cn, initials=get_initials(cn), ptype=infos["type"], phone=infos["phone"], mail=infos["mail"], postal=infos["postal"], id=infos["id"])

@app.errorhandler(Exception)
def error_handler(error):
	"""
	Shows a beatuiful error page to the user.
	"""
	verbose(" > handle error")
	if (DB.instance().isDBError()):
		return render_template("error.html", err="-1", msg="Internal Database Operation has failed. Try to remove the database file, or restart the app.")
	return render_template("error.html", err=error.code, msg=str(error))

@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering engine or Webkit based browsers, and also to cache the rendered page for 10 minutes.
	"""
	if ("--disable-caching" in sys.argv):
		r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
		r.headers["Pragma"] = "no-cache"
		r.headers["Expires"] = "0"
		r.headers['Cache-Control'] = 'public, max-age=0'
	return r

if __name__ == "__main__":
    app.run(debug=must_debug)

DB.instance().closeDB()
