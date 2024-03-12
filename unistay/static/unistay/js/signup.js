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
});
