document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-btn').addEventListener('click', function() {
        // Sample donor data
        const donors = [
            { name: 'John Doe', age: 30, gender: 'Male' },
            { name: 'Jane Smith', age: 25, gender: 'Female' },
            { name: 'Alice Johnson', age: 22, gender: 'Female' },
            { name: 'Bob Brown', age: 35, gender: 'Male' }
        ];

        const donorList = document.querySelector('.donor-list');
        donorList.innerHTML = ''; // Clear any existing donor data

        donors.forEach(donor => {
            const donorItem = document.createElement('div');
            donorItem.className = 'donor-item';
            donorItem.innerHTML = `
                <div>
                    <strong>Name:</strong> ${donor.name} <br>
                    <strong>Age:</strong> ${donor.age} <br>
                    <strong>Gender:</strong> ${donor.gender}
                </div>
                <button class="request-btn">Send Request</button>
            `;
            donorList.appendChild(donorItem);
        });

        document.querySelector('.results').style.display = 'block'; // Show the results section

        // Add event listener to all "Send Request" buttons
        const requestButtons = document.querySelectorAll('.request-btn');
        requestButtons.forEach(button => {
            button.addEventListener('click', function() {
                button.textContent = 'Request Sent'; // Change button text
                button.disabled = true; // Disable button
                button.classList.add('sent'); // Add "sent" class
            });
        });
    });
});
