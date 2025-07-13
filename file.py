from flask import Flask, request, render_template
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    target_language = request.form.get("language")
    audio = request.files.get("audioFile")

    if not audio:
        return "No audio file uploaded.", 400

    # Save uploaded audio file
    filename = audio.filename
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    audio.save(filepath)
    

    # Step 1: Translate speech to English using Whisper v1 API syntax
    with open(filepath, "rb") as audio_file:
        whisper_response = openai.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )
        english_text = whisper_response.text

    # Step 2: Translate English to target language (if needed)
    if target_language.lower() != "english":
        prompt = f"Translate the following sentence to {target_language}:\n\n{english_text}"
        response = openai.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a professional translator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=256,
        )
        final_translation = response.choices[0].message.content
    else:
        final_translation = english_text

    return render_template("index.html", result_text=final_translation, uploaded_file=filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
 