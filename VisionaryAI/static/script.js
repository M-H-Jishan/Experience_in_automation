document.getElementById('generate_image').addEventListener('click', function () {
    const description = document.getElementById('description').value;

    fetch('/generate_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ description: description })
    })
    .then(response => response.json())
    .then(data => {
        if (data.image_url) {
            document.getElementById('output').innerHTML = `<img src="${data.image_url}" alt="Generated Image">`;
        } else {
            document.getElementById('output').innerHTML = `<p>Error generating image</p>`;
        }
    });
});
