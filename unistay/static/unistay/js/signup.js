 $(document).ready(function() {
    $('#signupForm').submit(function(e) {
        e.preventDefault();

        $.ajax({
        type: 'POST',
        url: registerUrl,
        data: $(this).serialize(),
        success: function(response) {
            if(response.status === 'success') {
            //Close the modal and clear the form or redirect the user
            $('#signupModal').modal('hide');
            // clear the form fields
            $('#signupForm')[0].reset();
            alert('Signup success: ' + response);
            //redirect the user
            window.location.href = loginUrl;
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

    $('#loginForm').submit(function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: loginModalUrl, // Update with the correct URL path
            data: {
                email: $('#loginForm input[name="email"]').val(),
                password: $('#loginForm input[name="password"]').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    // Login success
                    // Redirect or close modal and update UI as needed
                    $('#loginModal').modal('hide');
                    console.log('success');
                    $('.logged-out').addClass('d-none'); // This hides elements
                    $('.logged-in').removeClass('d-none'); // This shows elements
                } else {
                    // Login failed
                    // Display error message to the user
                    alert(response.error);
                }
            },
            error: function(xhr, errmsg, err) {
                // handle error
                alert('Error: ' + errmsg);
            }
        });
    });
});
