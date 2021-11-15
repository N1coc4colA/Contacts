/*Performs magical HTTP(S) requests!*/
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback(xmlHttp.responseText);
			return;
		//Provide a warning message
		} else if (httpGetAsync.count > 100) {
			httpGetAsync.count = 0;
			if (!httpGetAsync.notified) {
				httpGetAsync.notified = true;
				alert("Seems like the connection to the backend broke. Try to restart the app.");
			}
		} else {
			httpGetAsync.count++;
		}
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function process_newer(content) {
	/*Udates the list's content*/
	document.getElementById("contactsListContainer").firstElementChild.children[1].innerHTML = content;
}

function filter_req(data) {/*Check for updates*/if (data == "1") {httpGetAsync("/data", process_newer);}}

/*Starts loop update*/
function check() {setInterval(function(){httpGetAsync("/updates", filter_req);}, 2000);}

//Setup
httpGetAsync.count = 0;
httpGetAsync.notified = false;
window.addEventListener("load", check);