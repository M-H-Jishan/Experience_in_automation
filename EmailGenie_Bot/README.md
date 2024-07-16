# EmailGenie

EmailGenie is an innovative GPT-powered AI chatbot designed to revolutionize outbound emailing by automating the creation of personalized cold emails. Utilizing OpenAI's advanced technology, EmailGenie streamlines the email creation process, enhancing both efficiency and effectiveness.

## Key Features
- **AI-Driven Personalization:** Employs GPT's AI capabilities to craft human-like, personalized emails, significantly enhancing engagement with recipients.
- **Dynamic Email Templates:** Generates varied email templates based on user profiles, adjusting tone, structure, and content for optimal targeting and better results.

## Project Structure
emailgenie/
├── app.py
├── models.py
├── email_templates.py
├── requirements.txt
├── static/
│   └── index.html
└── templates/
    └── index.html


## Getting Started

### Prerequisites
- Python 3.6+
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/emailgenie.git
    cd emailgenie
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
    - Replace `your_database_url` in `models.py` with your actual database URL.
    - Replace `your_openai_api_key` in `app.py` with your actual OpenAI API key.

5. **Initialize the database:**
    ```bash
    python -c "from models import init_db; init_db()"
    ```

### Running the Application

1. **Start the Flask application:**
    ```bash
    python app.py
    ```

2. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Usage

- **Email Generation Interface:**
    - Enter the user's name, email, and profile data.
    - Click "Generate Email" to create a personalized cold email.

## Contact Information

For any questions, suggestions, or feedback, please contact:

- **Moynul Hasan Jishan**
- **Email:** mh.jishan247@gmail.com
- **LinkedIn:** [Moynul Hasan Jishan](https://www.linkedin.com/in/m-h-jishan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
