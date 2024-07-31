document.getElementById('user-input-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        age: document.getElementById('age').value,
        gender: document.getElementById('gender').value,
        relation: document.getElementById('relation').value,
        interests: document.getElementById('interests').value,
        budget: document.getElementById('budget').value,
        occasion: document.getElementById('occasion').value
    };

    document.getElementById('loading').style.display = 'flex';

    fetch('http://localhost:5000/generate_gifts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        displayRecommendations(data);
        document.getElementById('loading').style.display = 'none';
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('loading').style.display = 'none';
        alert('An error occurred while generating gift ideas. Please try again.');
    });
});

function displayRecommendations(gifts) {
    const container = document.getElementById('recommendations-container');
    container.innerHTML = '';

    for (const [key, gift] of Object.entries(gifts)) {
        const giftElement = document.createElement('div');
        giftElement.className = 'gift-recommendation';
        giftElement.innerHTML = `
            <h3>${gift.name}</h3>
            <p><strong>Description:</strong> ${gift.description}</p>
            <p><strong>Why it's suitable:</strong> ${gift.reason}</p>
            <h4>Related Products:</h4>
            <ul>
                ${gift.related_products.map(product => `
                    <li>
                        <a href="${product.url}" target="_blank">${product.name}</a> - $${product.price.toFixed(2)}
                    </li>
                `).join('')}
            </ul>
        `;
        container.appendChild(giftElement);
    }

    document.getElementById('gift-recommendations').style.display = 'block';
    document.getElementById('gift-recommendations').scrollIntoView({ behavior: 'smooth' });
}