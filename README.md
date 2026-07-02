# Experience in Automation

A portfolio of 12 AI-powered automation projects showcasing practical applications of OpenAI, LangChain, computer vision, NLP, and ML in real-world scenarios.

## Projects

| # | Project | Description | Tech Stack |
|---|---------|-------------|------------|
| 1 | [AdGenPro](./AdGenPro) | AI-powered job advertisement generator | Flask, OpenAI GPT |
| 2 | [VisionaryAI](./VisionaryAI) | Text-to-image generator | Flask, OpenAI DALL-E |
| 3 | [LangSwitch](./LangSwitch) | AI-powered language translator | Flask, OpenAI GPT |
| 4 | [IntelliQuery_Bot](./IntelliQuery_Bot) | Intelligent query chatbot with user profiles | Flask, OpenAI, SQLAlchemy |
| 5 | [EmailGenie_Bot](./EmailGenie_Bot) | Personalized email generator | Flask, OpenAI, SQLAlchemy |
| 6 | [Customer Service Chatbot](./customer%20service%20chatbot) | RAG-based customer support with knowledge base | Flask, LangChain, OpenAI |
| 7 | [AI Trading Agent](./Ai_Tading_Agent) | Sentiment-based ML trading agent | Lumibot, Alpaca, FinBERT |
| 8 | [AI-powered Sales Assistant](./AI-powered%20Sales%20Assistant) | Lead generation + email automation + meeting scheduling | scikit-learn, Google Calendar API |
| 9 | [DepthForge](./DepthForge) | 2D image to 3D model converter | Flask, Sketchfab API |
| 10 | [Gift Idea Generator](./gift-idea-generator) | Personalized gift recommendation engine | Flask, OpenAI GPT |
| 11 | [Grocery Chatbot](./grocery_chatbot) | NLP grocery shopping assistant with cart & checkout | Flask, NLP, SQLite |
| 12 | [AI PowerPoint Generator](./ai-powerpoint-generator) | Automated presentation generator | Streamlit, OpenAI, python-pptx |

## Quick Start

Each project is self-contained. Navigate to a project directory and follow its README:

```bash
cd <project-name>
cp .env.example .env  # Add your API keys
pip install -r requirements.txt
python app.py  # or python main.py / streamlit run run.py
```

## Requirements

- Python 3.10+
- OpenAI API key (for AI projects)
- Alpaca API key (for trading agent)
- Sketchfab API token (for DepthForge)

## Docker

Most projects include a Dockerfile for containerized deployment:

```bash
cd <project-name>
docker build -t <project-name> .
docker run -p 5000:5000 --env-file .env <project-name>
```

## License

MIT
