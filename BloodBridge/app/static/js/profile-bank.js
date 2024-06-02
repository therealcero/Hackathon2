document.addEventListener('DOMContentLoaded', () => {
    // Dummy data for testing purposes
    const profileData = {
        bankName: "Blood Bank XYZ",
        registrationNumber: "123456",
        address: "1234 Elm Street, Some City",
        contact: "+1234567890",
        email: "example@bloodbank.com",
        requestsSent: 10,
        donorsAccepted: 5
    };

    // Populate the profile data
    document.getElementById('bank-name').textContent = profileData.bankName;
    document.getElementById('registration-number').textContent = profileData.registrationNumber;
    document.getElementById('address').textContent = profileData.address;
    document.getElementById('contact').textContent = profileData.contact;
    document.getElementById('email').textContent = profileData.email;
    document.getElementById('requests-sent').textContent = profileData.requestsSent;
    document.getElementById('donors-accepted').textContent = profileData.donorsAccepted;

    // Handle logout button click
    document.getElementById('logout-btn').addEventListener('click', () => {
        // Implement the actual logout logic here
        alert('Logged out!');
    });
});
