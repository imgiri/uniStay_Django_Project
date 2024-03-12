$(document).ready(function() {
   
    $('.signup-link').click(function(event) {
        event.preventDefault();
        $('#loginModal').modal('hide');
        $('#signupModal').modal('show');
    });

    $('.login-link').click(function(event) {
        event.preventDefault();
        $('#signupModal').modal('hide');
        $('#loginModal').modal('show');
    });

    $('#signupModal').on('hidden.bs.modal', function (e) {
        $('#loginModal').modal('show');
    });

    $('#loginModal').on('hidden.bs.modal', function (e) {
        $('#signUpModal').modal('show');
    }); 

});
