 
$(document).ready(function() {
    $('#signupForm').submit(function(e) {
        e.preventDefault();

        $.ajax({
        type: 'POST',
        url: '{% url "register" %}',  // Ensure you have a URL named 'register' in your urls.py
        data: $(this).serialize(),
        success: function(response) {
            if(response.status === 'success') {
            //Close the modal and clear the form or redirect the user
            $('#signupModal').modal('hide');
            // Optionally, clear the form fields
            $('#signupForm')[0].reset();
            alert('Signup success: ' + response);
            // If you want to redirect the user
            window.location.href = "{% url 'personal_login' %}";
            } else {
            // Handle failure
            alert('Signup failed: ' + response.error);
            }
        },
        error: function(xhr, errmsg, err) {
            alert('Ajax error: ' + errmsg);
        }
        });
    });
});
