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
		self.db = sqlite3.connect("contacts_db")
		self.cursor = self.db.cursor()
		self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts'")
		#Ensure the table we'll use is already here or create it!
		if (self.cursor.fetchone()[0] != 1):
			self.cursor.execute('''
			CREATE TABLE contacts (
				Id INTEGER PRIMARY KEY,
				Nom TEXT,
				Prenom TEXT,
				Mail TEXT,
				Phone INTEGER,
				PType TEXT
			)
			''')
		db.commit()

	def htmlifiedList(self):
		"""
		Transform raw SQL data into a beautiful HTML text that can be inserted into a page. (list of contacts)
		"""
		out = ""
		self.cursor.execute("SELECT (*) FROM ;")
		data = self.cursor.fetchall()
		for e in data:
			out += "<tr><td><input type=\"checkbox\" name=\"selection\" value=\""
			out += str(e[0])
			out += "></td><td><a href=\"view?id="
			out += str(e[0])
			out += "\">"
			out += str(e[1])
			out += "</a></td><td><a href=\"view?id="
			out += str(e[0])
			out += ">"
			out += str(e[2])
			out += "</a></td></tr>"
		return out

	def remove_by_id(id):
   	 	"""
   	 	Remove data from the DB by using its ID
   		"""
		requete = "DELETE  FROM Contacts  WHERE Id = ?;"
		self.cursor.execute(requete, [id])
		self.db.commit()

	def add_contact(content):
		 """
   		 Adds data to the DB
   		 """
		requete = "INSERT INTO contacts (Nom, Prenom, Phone, PType, Mail) VALUES (\"" + content["name"] + "\",\"" + content["surname"] + "\", " + content["phone"] + ", \"" + content["type"] + "\", " + content["mail"] + ");"
		self.cursor.execute(requete)
		self.db.commit()

	def update_by_id(self, content, id):
		"""
		Updates the DB content by using the ID used
		"""
		self.cursor.execute("UPDATE contacts SET Nom=\"" + content["nom"] + "\, Prenom=\"" + content["surname"] + "\", Phone=" + content["phone"] + ", PType=" + content["ptype"] + " WHERE Id=" + id + ");"
		self.db.commit()

	def get_by_id(id):
		"""
		Get a dict of data that belongs to a contact
		"""
		self.cursor.execute("SELECT (*) FROM contacts WHERE Id = ?", id)
		data = self.cursor.fetchone()
		return {"id":data[0], "name":data[1], "surname":data[2], "mail":data[3], "phone":data[4], "type":data[5]}

def get_initials(name):
	"""
	Generate a string like Asap Arnash -> Aa. Used with view.html
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

@app.route('/', methods=["POST", "GET"]) 
def home():
	'''
	Renders the home page
	'''
	#Arguments: selection - ID of the data to remove from the DB
	#Argument might be here many times depending on the user.
	data=request.form.getlist('selection')
	for c in data:
		DB.instance().remove_by_id(c)
	}
	return render_template("index.html", data=DB.instance().htmlifiedList())

@app.route("/add", methods=["POST"])
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
		infos=DB.instance().get_by_id(request["id"])
		return render_template("add.html", name=infos["name"], surname=infos["surname"], phone=infos["phone"], mail=infos["mail"])
	}
	return render_template("add.html", name="", surname="", phone="", mail="")

@app.route("/view", methods=["GET"])
def see():
	'''
	Renders the page that shows data about a user
	'''
	#Arguments: id - The ID of the data to be shown from the DB
	data=request.form
	infos=DB.instance().get_by_id(data["id"])
	cn=infos["name"] + " " + infos["surname"]
	return render_template("view.html", name=cn, initials=get_initales(cn), ptype=infos["type"], phone=infos["phone"], mail=infos["mail"])

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
