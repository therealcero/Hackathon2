document.addEventListener('DOMContentLoaded', function() {
    const registrationForm = document.getElementById('registration-form');
    const registrationSuccess = document.getElementById('registration-success');

    registrationForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Simulate registration success
        registrationSuccess.style.display = 'block';

        // Redirect to resources page after a delay (3 seconds)
        setTimeout(function() {
            window.location.href = 'resources.html';
        }, 3000);
    });
});
