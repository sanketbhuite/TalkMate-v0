from flask import Flask, render_template, request, jsonify
from utils import get_tutor_reply
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    response = get_tutor_reply(user_msg)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
