from flask import Flask, request, jsonify
import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [r"bonjour|salut|coucou", ["Salut ! Comment puis-je vous aider ?"]],
    [r"comment (ça va|allez-vous)", ["Je vais bien, merci. Et vous ?"]],
    [r"quel est ton nom ?", ["Je m'appelle ChatbotLydie. Et toi ?"]],
    [r"quit", ["Au revoir, passez une bonne journée !"]]
]

chat = Chat(pairs, reflections)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    message = request.json.get("message")
    response = chat.respond(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
