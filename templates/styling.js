/*https://codepen.io/sergiopedercini/pen/RLJYLj/*/
function stringToHslColor(str,s,l) {var h=0; for (var i=0; i<str.length; i++) {h=str.charCodeAt(i)+((h<<5)-h);} var e = h % 360; return 'hsl('+e+','+s+'%,'+l+'%)';}

function loadStyles() {
//Loaded elements dependent
var clc=document.getElementById("contactsListContainer")
if (clc!=null) {/*We can set up the styling*/ var sh=clc.offsetHeight; var d=clc.parentElement; if (d!=null) {var m = d.parentElement; if (m!=null)  {
var mh=m.offsetHeight; if (mh<=sh) {clc.classList.remove("cLCEnableAnim");}}}}

//Value dependent
var p=document.getElementById("Profile-Picture");
if (p!=null) {console.log("Found a picture");var cn=document.getElementById("Contact-Name"); if (cn!=null) {console.log("Found the name"); Object.assign(p.style, {"background-color": stringToHslColor(cn.innerHTML, "68", "70")});}}
}
window.addEventListener("load", loadStyles);

var btns=document.getElementsByClassName("back-home");
for (var i = 0; i < btns.length; i++) {
   btns.item(i).href = "index.html"; 
}