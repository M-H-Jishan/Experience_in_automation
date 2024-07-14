import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
import time
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    PERSIST = False
    data_path = r"C:\Users\User\Desktop\Ai_Automation_Agency\chatbot\knowledge_base"

    if PERSIST and os.path.exists("persist"):
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorstoreIndexCreator().vectorstore_wrapper(vectorstore=vectorstore)
    else:
        loader = DirectoryLoader(data_path)
        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []

    @app.route('/chat', methods=['POST'])
    def chat():
        if request.method == 'OPTIONS':
            return '', 204

        try:
            data = request.json
            query = data.get('question', '')
            if not query:
                return jsonify({'error': 'No question provided'}), 400

            # Add a delay of 1 second between requests
            time.sleep(1)

            result = chain({"question": query, "chat_history": chat_history})
            answer = result['answer']
            chat_history.append((query, answer))
            return jsonify({'answer': answer})
        except openai.error.RateLimitError as e:
            logger.error(f"OpenAI API rate limit exceeded: {str(e)}")
            return jsonify({'error': 'API rate limit exceeded. Please try again later.'}), 429
        except Exception as e:
            logger.error(f"An error occurred during chat: {str(e)}")
            return jsonify({'error': 'An internal error occurred'}), 500

except openai.error.RateLimitError as e:
    logger.error(f"OpenAI API rate limit exceeded during setup: {str(e)}")
    print("Error: OpenAI API rate limit exceeded. Please check your plan and billing details.")
except Exception as e:
    logger.error(f"An error occurred during setup: {str(e)}")
    print(f"Error during setup: {str(e)}")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
