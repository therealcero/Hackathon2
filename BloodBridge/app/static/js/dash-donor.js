document.addEventListener('DOMContentLoaded', function() {
    // Sample requests data
    const requests = [
        { bank: 'Blood Bank A', message: 'Urgent request for O+ blood type.' },
        { bank: 'Blood Bank B', message: 'Need blood donation for surgery.' },
        { bank: 'Blood Bank C', message: 'Request for AB- blood type.' }
    ];

    const requestsList = document.querySelector('.requests-list');
    const chatMessages = document.querySelector('.chat-messages');

    // Populate requests
    requests.forEach(request => {
        const requestItem = document.createElement('div');
        requestItem.className = 'request-item';
        requestItem.innerHTML = `
            <div class="request-info">
                <h3>${request.bank}</h3>
                <p>${request.message}</p>
            </div>
            <button class="respond-btn">Respond</button>
        `;
        requestsList.appendChild(requestItem);
    });

    // Sample chat history data
    const chatHistory = [
        { sender: 'Blood Bank A', message: 'Thank you for responding.' },
        { sender: 'You', message: "I'm available for donation." }
    ];

    // Simulate chat messages
    chatHistory.forEach(message => {
        const chatMessage = document.createElement('div');
        chatMessage.className = 'chat-message';
        chatMessage.innerHTML = `<strong>${message.sender}:</strong> ${message.message}`;
        chatMessages.appendChild(chatMessage);
    });
});
