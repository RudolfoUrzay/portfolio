document.getElementById("ignore_fears").addEventListener("click", e=>{
    document.getElementById("text_house_1").innerHTML = "Congratulations you are a Gryffindor";
    document.getElementById("go_div2").style.display = "none";
    document.getElementById("Gryffindor").style.display = "none";
    document.getElementById("ignore_fears").style.display = "none";
    //document.getElementById("btnNope").innerHTML = "Yay!!";
})

document.getElementById("go_div2").addEventListener("click", e=>{
    document.getElementById("div2_houses").style.display = "block";
    document.getElementById("div1_houses").style.display = "none";
})

document.getElementById("button_div2").addEventListener("click", e=>{
    document.getElementById("text_house_2").innerHTML = "Congratulations you are a Slytherin";
    document.getElementById("button_div2_2").style.display = "none";
    document.getElementById("button_div2").style.display = "none";
    //document.getElementById("btnNope").innerHTML = "Yay!!";
})

document.getElementById("go_div3").addEventListener("click", e =>{
    document.getElementById("div3_houses").style.display = "block";
    document.getElementById("div2_houses").style.display = "none";
})