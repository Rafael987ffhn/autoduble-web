from flask import Flask, render_template, request, send_from_directory
import os
import moviepy.editor as mp
import whisper
from gtts import gTTS
from googletrans import Translator
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

translator = Translator()

def traduzir_texto(texto, destino):
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video = request.files["video"]
        idioma = request.form["idioma"]
        traduzir = "traduzir" in request.form
        filename = str(uuid.uuid4()) + ".mp4"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(filepath)

        audio_path = filepath.replace(".mp4", "_audio.wav")
        video_clip = mp.VideoFileClip(filepath)
        video_clip.audio.write_audiofile(audio_path)

        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        texto = result["text"]

        if traduzir:
            texto = traduzir_texto(texto, idioma)

        tts = gTTS(text=texto, lang=idioma)
        dubbed_audio_path = filepath.replace(".mp4", "_dubbed.mp3")
        tts.save(dubbed_audio_path)

        dubbed_audio = mp.AudioFileClip(dubbed_audio_path)
        final_video = video_clip.set_audio(dubbed_audio)

        output_filename = filename.replace(".mp4", f"_dublado_{idioma}.mp4")
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        final_video.write_videofile(output_path)

        return send_from_directory(app.config['OUTPUT_FOLDER'], output_filename, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    app.run(debug=True)
