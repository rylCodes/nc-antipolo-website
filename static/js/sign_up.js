const form = document.getElementById('signupForm');
const passwordInput = document.getElementById('password');

form.addEventListener('submit', (event) => {
  if (!isPasswordValid(passwordInput.value)) {
    event.preventDefault(); // Prevent form submission
    displayPasswordError();
  }
});

function isPasswordValid(password) {
  // Use a regular expression to validate the password format
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  return passwordRegex.test(password);
}

function displayPasswordError() {
  // Display an error message to the user
  const errorContainer = document.getElementById('passwordError');
  errorContainer.innerText = 'Password should be at least 8 characters long with 1 uppercase letter, 1 lowercase letter, 1 special character, and 1 number.';
  errorContainer.classList.add("text-center", "text-sm", "text-red-600", "my-4");
}
