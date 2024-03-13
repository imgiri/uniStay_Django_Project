console.log("js loaded");
let ptL = document.getElementById("ptbutton-l");
let ptR = document.getElementById("ptbutton-r");

if (ptL != null) {
    ptL.addEventListener("click", disableChangerL);
    ptR.addEventListener("click", disableChangerR);
}




function disableChangerR() {
    ptL.classList.add("deselected");
    ptR.classList.remove("deselected")
}
function disableChangerL() {
    ptL.classList.remove("deselected");
    ptR.classList.add("deselected")
}


