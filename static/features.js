/*https://codepen.io/sergiopedercini/pen/RLJYLj/*/
function stringToHslColor(str,s,l) {
	var h=0;
	for (var i=0; i<str.length; i++) {
		h=str.charCodeAt(i)+((h<<5)-h);
	}
	var e = h % 360;
	return 'hsl('+e+','+s+'%,'+l+'%)';
}

function goHome() {window.location.href = "/";}

function loadFeatures() {
//Loaded elements dependent
var clc=document.getElementById("contactsListContainer")
if (clc!=null) {
	/*We can set up the styling*/
	var sh=clc.offsetHeight;
	var d=clc.parentElement;
	if (d!=null) {
		var m=d.parentElement;
		if (m!=null) {
			var mh=m.offsetHeight;
			if (mh>=sh) {
				clc.classList.remove("cLCEnableAnim");
			}
		}
	}
	var btns=document.getElementsByClassName("back-home");
	for (var i=0; i<btns.length; i++) {
		btns.item(i).onclick = goHome;
	}
}

//Value dependent
/* Contact's picture, generate the image color*/
var p=document.getElementById("Profile-Picture");
if (p!=null) {
	var cn=document.getElementById("Contact-Name");
	if (cn!=null) {
		Object.assign(p.style, {"background-color": stringToHslColor(cn.innerHTML, "68", "70")});
	}
}

}

//Search feature for index.html
function updateSearch(data) {
	/*First of all store all the internals*/
	if (data === null) {
		//Used with filter by
		data = updateSearch.text;
		console.log("using old data");
	} else {
		console.log("using new data");
		updateSearch.text = data;
	}
	var ses = document.getElementsByClassName("SE");

	if (data!="") {
		/*Get all elements*/
		for (var i=0; i<ses.length; i++) {
			var it = ses.item(i);
			var t1 = it.children[0].children[0].innerHTML;
			var t2 = it.children[1].children[0].innerHTML;
			if (t1.includes(data) || t2.includes(data)) {
				/*To ensure it is visible*/
				if (updateSearch.filter.text == "") {
					it.classList.remove("hidden");
				} else {
					if (it.dataset.ptype != updateSearch.filter.text) {
						it.classList.add("hidden");
					} else {
						//Ensure visibility
						it.classList.remove("hidden");
					}
				}
			} else {
				it.classList.add("hidden");
			}
		}
	} else if (updateSearch.filter.text == "") {
		/*Just show it all*/
		for (var i = 0; i < ses.length; i++) {
			ses.item(i).classList.remove("hidden");
		}
	} else {
		//Have to filter anyway then
		for (var i = 0; i < ses.length; i++) {
			var it = ses.item(i);
			if (it.dataset.ptype != updateSearch.filter.text) {
				it.classList.add("hidden");
			} else {
				it.classList.remove("hidden");
			}
		}
	}
}

function filterBy(name) {
	filterBy.text = name;
	/*Reload*/
	updateSearch(null);
}

//Setup
updateSearch.text = "";
filterBy.text = "";
updateSearch.filter = filterBy;
window.addEventListener("load", loadFeatures);
