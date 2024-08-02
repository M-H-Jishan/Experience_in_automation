document.addEventListener('DOMContentLoaded', () => {
    const uploadButton = document.getElementById('upload-button');
    const fileInput = document.getElementById('image-upload');
    const modelContainer = document.getElementById('model-container');

    fileInput.addEventListener('change', () => {
        const fileName = fileInput.files[0]?.name;
        if (fileName) {
            document.querySelector('.custom-file-upload').textContent = fileName;
        }
    });

    uploadButton.addEventListener('click', () => {
        const file = fileInput.files[0];
        if (file) {
            uploadButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
            uploadButton.disabled = true;

            const formData = new FormData();
            formData.append('file', file);

            fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.uid) {
                    displaySketchfabModel(data.uid);
                } else {
                    alert('Failed to generate 3D model. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while generating the 3D model.');
            })
            .finally(() => {
                uploadButton.innerHTML = '<i class="fas fa-cog"></i> Generate 3D Model';
                uploadButton.disabled = false;
            });
        } else {
            alert('Please select an image first.');
        }
    });

    function displaySketchfabModel(uid) {
        modelContainer.innerHTML = `
            <iframe src="https://sketchfab.com/models/${uid}/embed" 
                    width="100%" 
                    height="400" 
                    allow="autoplay; fullscreen; vr" 
                    mozallowfullscreen="true" 
                    webkitallowfullscreen="true">
            </iframe>
        `;
    }

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});