document.getElementById("cookieBanner").style.display = "block";


document.getElementById("btnNope").addEventListener("click", e=>{
    document.getElementById("cookieBanner").style.display = "none";    
    //document.getElementById("btnYes");
});

document.getElementById("btnYes").addEventListener("click", e=>{
    document.getElementById("cookieTitle").innerHTML = "First Lesson - Don't admit that";
    document.getElementById("cookieText").innerHTML ="But you did! So as a reward, your third year will now feature 30% extra dementor!";
    document.getElementById("btnYes").style.display = "none";
    document.getElementById("btnNope").innerHTML = "Yay!!";
})

document.getElementById("ignore_fears").addEventListener("click", e=>{
    document.getElementById("text_house_1").innerHTML = "Congratulations you are a Gryffindor";
    document.getElementById("go_div2").style.display = "none";
    document.getElementById("Gryffindor").style.display = "none";
    //document.getElementById("btnNope").innerHTML = "Yay!!";
})