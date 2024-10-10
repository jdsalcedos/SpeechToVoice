import tkinter as tk
from constants import *
from gtts import gTTS

import os


def processText(texto):

    tts = gTTS(text=texto, lang="es")

    archivo_audio = "salida.mp3"

    tts.save(archivo_audio)

    os.system(f"start {archivo_audio}")


def mainWindow():
    window = tk.Tk()
    window.title("Text to Voice")
    window.resizable = False
    window.config(bg="lightgrey")

    window.geometry(SIZE_WINDOW)

    introducedText = tk.Text(window, height=20, width=55)
    introducedText.pack(pady=20)

    def text_register_click():
        text = introducedText.get("1.0", tk.END).strip()
        processText(text)

    def clear_text_click():
        introducedText.delete("1.0", tk.END)

    registerBtn = tk.Button(
        window,
        text="Convertir a Voz",
        command=text_register_click,
    )
    registerBtn.pack(pady=10)

    clearBtn = tk.Button(window, text="Limpiar", command=clear_text_click)
    clearBtn.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    mainWindow()
