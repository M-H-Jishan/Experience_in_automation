# AdGenPro

AdGenPro is an AI-powered tool designed to assist recruiters in crafting effective job advertisements. Leveraging the advanced capabilities of ChatGPT, AdGenPro transforms a brief job description and information from a company's career page into comprehensive job ads that are ready to be published on LinkedIn and other job recruiting sites.

## Key Features
- **AI-Driven Job Ad Creation:** Utilizes ChatGPT to generate detailed and engaging job ads based on minimal input, ensuring high-quality content that attracts top talent.
- **Streamlined Workflow:** Simplifies the job ad creation process for recruiters, saving time and effort while maintaining consistency and professionalism.
- **Multi-Platform Compatibility:** Produces job ads that are optimized for various recruiting platforms, including LinkedIn and other job boards, ensuring wide reach and visibility.

## Project Structure
AdGenPro/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md


## Getting Started

### Prerequisites
- Python 3.6+
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/AdGenPro.git
    cd jAdGenPro
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your environment:**
    - Replace `your_openai_api_key` in `app.py` with your actual OpenAI API key.

### Running the Application

1. **Start the Flask application:**
    ```bash
    python app.py
    ```

2. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Usage

- **Job Ad Generation Interface:**
    - Enter the company's career page details and the job description.
    - Click "Generate Job Ad" to create a personalized and engaging job ad.

## Contact Information

For any questions, suggestions, or feedback, please contact:

- **Moynul Hasan Jishan**
- **Email:** mh.jishan247@gmail.com
- **LinkedIn:** [Moynul Hasan Jishan](https://www.linkedin.com/in/m-h-jishan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
