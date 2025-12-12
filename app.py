from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Crear carpeta uploads en Render si no existe
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    ciudad = request.form.get("ciudad")
    personalizado = request.form.get("personalizado")
    tematica = request.form.get("tematica")

    adjunto = request.files.get("adjunto")
    archivo_final = None

    if adjunto and adjunto.filename != "":
        filename = secure_filename(adjunto.filename)
        archivo_final = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        adjunto.save(archivo_final)

    print("\n--- NUEVO FORMULARIO ---")
    print("Nombre:", nombre)
    print("Correo:", correo)
    print("Ciudad:", ciudad)
    print("Adjunto:", archivo_final)
    print("Personalizado:", personalizado)
    print("Temática:", tematica)
    print("-------------------------\n")

    return "Gracias por tu mensaje. ¡Pronto te contacto!"

# NO colocar app.run() — Render usa Gunicorn
