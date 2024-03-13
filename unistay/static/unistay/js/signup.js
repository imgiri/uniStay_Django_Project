 $(document).ready(function() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    

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

    $('#logoutButton').click(function(event) {
        console.log("logout");
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: logoutUserUrl,
            /*data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },*/
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                    /*// Hide logout and profile buttons
                    $('#logoutButton').hide();
                    $('#profileButton').hide();
                    // Show login and signup buttons
                    $('#loginButton').show();
                    $('#signupButton').show();*/
                    
                    $('.logged-out').removeClass('d-none'); // This hides elements
                    $('.logged-in').addClass('d-none'); // This shows elements

                    // Redirect to the homepage after a delay
                    setTimeout(function() {
                        window.location.href = indexUrl;
                    }, 2000);  // Redirect after 2 seconds
                }
            }
        });
    });

    /*$('#writeReviewButton').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: writeReviewButton,  // Update this with the correct path
            method: 'POST',  // or 'POST' depending on your implementation
            success: function(data) {
                console.log('over here')
                // Logic to open the review form or proceed as normal
            },
            error: function(xhr, status, error) {
                if (xhr.status == 403 && xhr.responseJSON.login_required) {
                    $('#loginModal').modal('show');  // Show the login modal
                } else {
                    // Handle other errors
                }
            }
        });
    });*/

});
