import logging
import os
import sys

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string

from config import PORT, DEBUG

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
chatbot = None


def get_chatbot():
    global chatbot
    if chatbot is None:
        from chatbot.bot import GroceryStoreChatbot
        chatbot = GroceryStoreChatbot()
    return chatbot

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head><title>Grocery Chatbot</title></head>
<body>
  <h1>Grocery Store Chatbot</h1>
  <div id="chat" style="height:300px;overflow-y:scroll;border:1px solid #ccc;padding:10px;"></div>
  <input type="text" id="msg" placeholder="Type your message..." style="width:80%;">
  <button onclick="send()">Send</button>
  <script>
    async function send() {
      const m = document.getElementById('msg').value;
      document.getElementById('chat').innerHTML += '<p><b>You:</b> ' + m + '</p>';
      document.getElementById('msg').value = '';
      const res = await fetch('/chat', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:m})});
      const data = await res.json();
      document.getElementById('chat').innerHTML += '<p><b>Bot:</b> ' + data.response + '</p>';
      document.getElementById('chat').scrollTop = 9999;
    }
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(INDEX_HTML)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = get_chatbot().respond(message)
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return jsonify({"error": "Failed to process message"}), 500


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
