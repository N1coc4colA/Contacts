var clc = document.getElementById("contactsListContainer")

if (clc != null) {
	console.log("Baby is OK");
	//We can set up the styling
	var s_height = clc.offsetHeight;
	var dad = clc.parentElement;
	if (dad != null) {
		console.log("Dad is OK");
		var mom = dad.parentElement;
		if (mom != null)  {
			console.log("Mom is OK");
			var m_height = mom.offsetHeight;
			if (m_height <= s_height) {
				console.log("Mom equals to ", m_height);
				console.log("Baby equals to ", s_height);
				clc.classList.remove("cLCEnableAnim");
			}
		}
	}
}