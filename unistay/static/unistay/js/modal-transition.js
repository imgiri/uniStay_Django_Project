// Wait for the DOM to be fully loaded before executing any jQuery code
$(document).ready(function() {

    // When the signup link is clicked
    $('.signup-link').click(function(event) {
        event.preventDefault(); // Prevent the default action of the link
        $('#loginModal').modal('hide'); // Hide the login modal
        $('#signupModal').modal('show'); // Show the signup modal
    });

    // When the login link is clicked
    $('.login-link').click(function(event) {
        event.preventDefault(); // Prevent the default action of the link
        $('#signupModal').modal('hide'); // Hide the signup modal
        $('#loginModal').modal('show'); // Show the login modal
    });

    // When the signup modal is closed
    $('#signupModal').on('hidden.bs.modal', function (e) {
        $('#loginModal').modal('show'); // Show the login modal
    });

    // When the login modal is closed
    $('#loginModal').on('hidden.bs.modal', function (e) {
        $('#signUpModal').modal('show'); // Show the signup modal
    }); 

});
