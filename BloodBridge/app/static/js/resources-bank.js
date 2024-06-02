document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('resources-form');
    const updateSuccess = document.getElementById('update-success');

    // Load existing data from localStorage if available
    const existingData = JSON.parse(localStorage.getItem('resourcesData')) || {
        bloodIntake: '',
        bloodOutgoing: '',
        bloodRemaining: '',
        totalIntake: '',
        totalOutgoing: '',
        totalRemaining: ''
    };

    // Pre-fill the form with existing data if available
    document.getElementById('blood-intake').value = existingData.bloodIntake;
    document.getElementById('blood-outgoing').value = existingData.bloodOutgoing;
    document.getElementById('blood-remaining').value = existingData.bloodRemaining;
    document.getElementById('total-intake').value = existingData.totalIntake;
    document.getElementById('total-outgoing').value = existingData.totalOutgoing;
    document.getElementById('total-remaining').value = existingData.totalRemaining;

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Save form data to localStorage
        const resourcesData = {
            bloodIntake: document.getElementById('blood-intake').value,
            bloodOutgoing: document.getElementById('blood-outgoing').value,
            bloodRemaining: document.getElementById('blood-remaining').value,
            totalIntake: document.getElementById('total-intake').value,
            totalOutgoing: document.getElementById('total-outgoing').value,
            totalRemaining: document.getElementById('total-remaining').value
        };

        localStorage.setItem('resourcesData', JSON.stringify(resourcesData));

        // Show success message and redirect
        updateSuccess.style.display = 'block';
        setTimeout(() => {
            updateSuccess.style.display = 'none';
            window.location.href = 'resources-bank.html'; // Redirect to resources page after updating
        }, 2000);
    });
});
