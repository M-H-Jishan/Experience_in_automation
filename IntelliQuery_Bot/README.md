# IntelliQuery Bot

IntelliQuery Bot is an advanced AI-powered database chatbot designed to revolutionize real-time data retrieval and user assistance. Leveraging the capabilities of GPT and OpenAI technologies, IntelliQuery Bot provides intelligent and efficient interaction with complex databases, ensuring users receive prompt and accurate information.

## Key Features
- **AI-Driven Data Interaction:** Utilizes GPT and OpenAI models to query complex databases, delivering fast and precise access to information.
- **User-Friendly Interface:** Features an intuitive, natural language chat interface, making database interaction simple and enhancing accessibility for users.
- **Advanced Response Algorithms:** Incorporates sophisticated algorithms to provide contextual and relevant responses to a wide range of user queries.
- **Seamless Database Integration:** Connects flawlessly with existing database systems for real-time data updates and retrieval, improving overall efficiency.

## Project Structure
intelliquery-bot/
├── app.py
├── models.py
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
    git clone https://github.com/yourusername/intelliquery-bot.git
    cd intelliquery-bot
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

- **Chat Interface:**
    - Type your message in the input box and press Enter.
    - The chatbot will respond to your queries in real-time.

- **Add User:**
    - To add a user, send a POST request to `/add_user` with JSON payload containing `name`, `email`, and `service_description`.

## Contact Information

For any questions, suggestions, or feedback, please contact:

- **Moynul Hasan Jishan**
- **Email:** mh.jishan247@gmail.com
- **LinkedIn:** [Moynul Hasan Jishan](https://www.linkedin.com/in/m-h-jishan)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
