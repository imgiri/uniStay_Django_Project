console.log("js loaded"); // Log a message indicating that the JavaScript file has been loaded

// Get the elements with the IDs "ptbutton-l" and "ptbutton-r"
let ptL = document.getElementById("ptbutton-l");
let ptR = document.getElementById("ptbutton-r");

// If the element with ID "ptbutton-l" exists
if (ptL != null) {
    // Add event listener to "ptbutton-l" for click event, calling the function disableChangerL
    ptL.addEventListener("click", disableChangerL);
    // Add event listener to "ptbutton-r" for click event, calling the function disableChangerR
    ptR.addEventListener("click", disableChangerR);
}

// Function to disable the changer on the right side
function disableChangerR() {
    // Add class "deselected" to ptL element
    ptL.classList.add("deselected");
    // Remove class "deselected" from ptR element
    ptR.classList.remove("deselected")
}

// Function to disable the changer on the left side
function disableChangerL() {
    // Remove class "deselected" from ptL element
    ptL.classList.remove("deselected");
    // Add class "deselected" to ptR element
    ptR.classList.add("deselected")
}
