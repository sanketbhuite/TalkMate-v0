
# 🧑‍🏫 TalkMate v0 – AI English Speaking Tutor

TalkMate is a lightweight Flask-based web application that helps users improve their English communication skills. It allows users to talk to an AI tutor, receive real-time responses, and get grammar corrections and tips — all in one go.

---

## 🚀 Features

- 💬 Natural language conversation with AI
- 🛠️ Grammar & spelling correction
- 💡 Instant language improvement tips
- 🌐 Web-based interface (HTML + JS)
- 🔓 No login or database needed (v0)

---

## 📦 Installation Guide

### 1. Clone this repo

```bash
git clone https://github.com/your-username/TalkMate.git
cd TalkMate
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

### 4. Setup OpenRouter (Free GPT Access)

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Sign in with Google or GitHub
3. Go to [https://openrouter.ai/keys](https://openrouter.ai/keys)
4. Generate your API key

### 5. Create a `.env` file in the root directory

```
OPENAI_API_KEY=your_openrouter_api_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1
```

> Replace `your_openrouter_api_key_here` with your actual OpenRouter API key.

### 6. Run the Flask app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🛠️ Tech Stack

- Python + Flask
- HTML + CSS + JS (vanilla)
- OpenAI GPT-3.5 via OpenRouter API
- Web Speech & Text-to-Speech (coming in v1.5)

---

## ✨ What's Next

- [ ] Voice input (speech-to-text)
- [ ] Voice response (text-to-speech)
- [ ] User login & grammar history tracking
- [ ] Real-time streaming & correction while talking

---

## 📄 License

MIT License. Use freely with credit.

---

Built with ❤️ by Sanket Bhuite.
