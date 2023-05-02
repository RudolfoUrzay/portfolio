document.getElementById("staff").addEventListener("click", e=>{

    const xhttp = new XMLHttpRequest();

    xhttp.addEventListener("load", e => {

        const modules = JSON.parse(e.target.responseText);
        
        let output = "";

	    modules.forEach(position => {
		    output += "<p><strong>Name: </strong>" + subjects.name + ",<strong> Position: </strong>" + subjects.position + "</p>";
	    });

        document.getElementById("result").innerHTML = e.target.responseText
    });

    xhttp.open("GET", "js/staff.json");
    xhttp.send();


});

document.getElementById("subjects").addEventListener("click", e=>{

    const xhttp = new XMLHttpRequest();

    xhttp.addEventListener("load", e => {

        const modules = JSON.parse(e.target.responseText);
        
        let output = "";

	    modules.forEach(position => {
		    output += "<p><strong>Name: </strong>" + subjects.name + ",<strong> Position: </strong>" + subjects.position + "</p>";
	    });

        document.getElementById("result").innerHTML = e.target.responseText
    });

    xhttp.open("GET", "js/subjects.json");
    xhttp.send();


});