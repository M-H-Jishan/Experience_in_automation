# DepthForge - 2D to 3D Image Conversion

DepthForge is an innovative web application that transforms 2D images into stunning 3D models using advanced AI algorithms. Developed by IntelliBot Labs, this tool opens up a world of possibilities for designers, artists, and 3D enthusiasts.

## Features

- **Easy-to-use Interface**: Simple drag-and-drop functionality for image upload.
- **AI-Powered Conversion**: Utilizes state-of-the-art AI models to generate accurate 3D representations.
- **Real-time Preview**: View your 3D model directly in the browser using Sketchfab's embed feature.
- **Responsive Design**: Fully functional on both desktop and mobile devices.

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python, Flask
- **3D Processing**: Sketchfab API
- **Styling**: Font Awesome for icons, Google Fonts for typography

## Getting Started

### Prerequisites

- Python 3.7+
- pip
- A Sketchfab account with an API token

### Installation

1. Clone the repository.
2. Set up the backend.
3. Configure the Sketchfab API:
- Open `app.py` and replace `'YOUR_SKETCHFAB_API_TOKEN'` with your actual Sketchfab API token.

4. Run the Flask server.
5. Open the frontend:
- Navigate to the `frontend` folder and open `index.html` in your web browser.

## Usage

1. Click on "Choose Image" to select a 2D image from your device.
2. Click "Generate 3D Model" to start the conversion process.
3. Wait for the process to complete. The 3D model will be displayed in the viewer once ready.
4. Interact with the 3D model using your mouse or touchscreen.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
