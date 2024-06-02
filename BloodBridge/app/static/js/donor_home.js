// accept_request.js

function acceptRequest(id) {
    console.log(id);
    fetch('/accept_request/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Optionally include CSRF token if CSRF protection is enabled
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ id: id })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);  // Log the response message
        // Optionally, perform any other actions upon successful acceptance
    })
    .catch(error => console.error("Error accepting request:", error));
}
