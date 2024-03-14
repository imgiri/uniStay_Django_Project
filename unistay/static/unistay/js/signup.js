 $(document).ready(function() {
    // Set up default options for AJAX requests
    $.ajaxSetup({
        // Before sending the request, check if it's not a cross-domain request
        beforeSend: function(xhr, settings) {
            if (!this.crossDomain) {
                // Set X-CSRFToken header with the value of the CSRF token retrieved from the cookie
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    // Function to retrieve a cookie by name
    function getCookie(name) {
        var cookieValue = null;
        // Check if cookies are present and not empty
        if (document.cookie && document.cookie !== '') {
            // Split cookies string into individual cookies
            var cookies = document.cookie.split(';');
            // Loop through each cookie
            for (var i = 0; i < cookies.length; i++) {
                // Trim any whitespace from the cookie string
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
            
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                    
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

});
