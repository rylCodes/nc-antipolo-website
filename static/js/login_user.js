  // Handle the form submission
  $('#login-form').submit(function(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the form data
    var formData = $(this).serialize();

    // Make an AJAX request to the login_user view
    $.ajax({
      url: '/login_user/',  // Replace with your login URL
      method: 'POST',
      data: formData,
      dataType: 'json',
      success: function(response) {
        // Handle the response
        if (response.status === 'success') {
          // Successful login
          alert('Login successful!');
          // Redirect to a new page or perform any other action
        } else {
          // Failed login
          alert('Login failed: ' + response.msg);
          // Display the error message to the user or perform any other action
        }
      },
      error: function(_, errorThrown) {
        // Handle any error that occurred during the AJAX request
        console.error('AJAX error:', errorThrown);
      }
    });
  });