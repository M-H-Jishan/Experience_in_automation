document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const sourceLang = document.getElementById('source-lang');
    const targetLang = document.getElementById('target-lang');

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessage('user', message);
            translateMessage(message);
            userInput.value = '';
        }
    }

    function addMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function translateMessage(message) {
        const source = sourceLang.value;
        const target = targetLang.value;

        fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                source_lang: source,
                target_lang: target,
            }),
        })
        .then(response => response.json())
        .then(data => {
            addMessage('bot', data.translation);
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('bot', 'An error occurred while translating. Please try again.');
        });
    }
});