/*Performs magical HTTP(S) requests!*/
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function process_newer(content) {/*Udates the list's content*/var src=document.getElementById("contactsListContainer"); src.firstElementChild.innerHTML = content;}

function filter_req(data) {/*Check for updates*/if (data == "1") {httpGetAsync("/data", process_newer);}}

/*Starts loop update*/
function check() {setInterval(function(){httpGetAsync("/updates", filter_req);}, 2000);}

window.addEventListener("load", check);