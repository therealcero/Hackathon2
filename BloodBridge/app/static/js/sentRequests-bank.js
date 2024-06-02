document.addEventListener('DOMContentLoaded', () => {
    const requestsList = document.getElementById('requests-list');

    // Dummy data for testing purposes
    const requests = [
        { name: 'John Doe', bloodType: 'A+', status: 'Pending' },
        { name: 'Jane Smith', bloodType: 'O-', status: 'Pending' },
        { name: 'Alice Johnson', bloodType: 'B+', status: 'Accepted' },
    ];

    requests.forEach(request => {
        const requestItem = document.createElement('div');
        requestItem.className = 'request-item';
        
        const requestInfo = document.createElement('div');
        requestInfo.innerHTML = `
            <p>Name: ${request.name}</p>
            <p>Blood Type: ${request.bloodType}</p>
            <p>Status: ${request.status}</p>
        `;

        const withdrawButton = document.createElement('button');
        withdrawButton.textContent = 'Withdraw Request';
        withdrawButton.onclick = () => {
            requestItem.remove();
            alert(`Request to ${request.name} withdrawn.`);
        };

        requestItem.appendChild(requestInfo);
        requestItem.appendChild(withdrawButton);
        requestsList.appendChild(requestItem);
    });
});
