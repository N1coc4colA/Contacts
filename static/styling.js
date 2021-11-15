/*https://codepen.io/sergiopedercini/pen/RLJYLj/*/
function stringToHslColor(str,s,l) {var h=0; for (var i=0; i<str.length; i++) {h=str.charCodeAt(i)+((h<<5)-h);} var e = h % 360; return 'hsl('+e+','+s+'%,'+l+'%)';}

function goHome() {window.location.href = "/";}

function loadFeatures() {
//Loaded elements dependent
var clc=document.getElementById("contactsListContainer")
if (clc!=null) {/*We can set up the styling*/ var sh=clc.offsetHeight; var d=clc.parentElement; if (d!=null) {var m=d.parentElement; if (m!=null) {var mh=m.offsetHeight; if (mh>=sh) {clc.classList.remove("cLCEnableAnim");}}}
var btns=document.getElementsByClassName("back-home");
for (var i=0; i<btns.length; i++) {btns.item(i).onclick = goHome;}
}

//Value dependent
var p=document.getElementById("Profile-Picture");
if (p!=null) {var cn=document.getElementById("Contact-Name"); if (cn!=null) {Object.assign(p.style, {"background-color": stringToHslColor(cn.innerHTML, "68", "70")});}}
}
window.addEventListener("load", loadFeatures);

//Search feature for index.html
function updateSearch(data) {var ses=document.getElementsByClassName("SE"); if (data!="") {/*Get all elements*/for (var i=0; i<ses.length; i++) {var it = ses.item(i); if (it.innerHTML.includes(data)) {/*To ensure it is visible*/it.parentElement.parentElement.classList.remove("hidden");} else {it.parentElement.parentElement.classList.add("hidden");}}} else {/*Just show it all*/for (var i = 0; i < ses.length; i++) {ses.item(i).parentElement.parentElement.classList.remove("hidden");}}}