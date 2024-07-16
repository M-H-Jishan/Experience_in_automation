document.getElementById('generate_ad').addEventListener('click', function () {
    const careerPage = document.getElementById('career_page').value;
    const jobDescription = document.getElementById('job_description').value;

    fetch('/generate_ad', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ career_page: careerPage, job_description: jobDescription })
    })
    .then(response => response.json())
    .then(data => {
        if (data.job_ad) {
            document.getElementById('output').innerHTML = `<pre>${data.job_ad}</pre>`;
        } else {
            document.getElementById('output').innerHTML = `<p>Error generating job ad</p>`;
        }
    });
});
