# Real-Time-Audio-Translation-Web-App-using-OpenAI-Whisper-and-GPT-Models
A Flask-based web app that lets users upload audio in any language and receive translated text. It uses OpenAI's Whisper to transcribe speech to English and GPT-4.1-mini to translate into the target language. Ideal for multilingual communication, education, and accessibility.
---

## 🚀 Features

- Upload audio files (`.mp3`, `.wav`, etc.)
- Transcribe non-English speech to English using OpenAI Whisper
- Translate English text into target language via GPT
- Clean UI with TailwindCSS

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **APIs**: OpenAI Whisper, GPT-4.1-mini
- **Frontend**: HTML (Jinja2 + TailwindCSS)
- **Env Management**: python-dotenv

---
## 📁 Structure
```plaintext
audio-translate-app/
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
├── static/
