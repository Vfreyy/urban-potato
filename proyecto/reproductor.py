import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class ReproductorMusica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Reproductor de Música")
        self.ventana.geometry("400x200")
        pygame.mixer.init()

        self.archivo_actual = ""

        self.boton_cargar = tk.Button(ventana, text="Cargar canción", command=self.cargar_cancion)
        self.boton_cargar.pack(pady=10)

        self.boton_reproducir = tk.Button(ventana, text="Reproducir", command=self.reproducir)
        self.boton_reproducir.pack(pady=10)

        self.boton_pausar = tk.Button(ventana, text="Pausar", command=self.pausar)
        self.boton_pausar.pack(pady=10)

        self.boton_detener = tk.Button(ventana, text="Detener", command=self.detener)
        self.boton_detener.pack(pady=10)

    def cargar_cancion(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
        if archivo:
            self.archivo_actual = archivo

    def reproducir(self):
        if self.archivo_actual:
            try:
                pygame.mixer.music.load(self.archivo_actual)
                pygame.mixer.music.play()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo reproducir la canción:\n{e}")

    def pausar(self):
        pygame.mixer.music.pause()

    def detener(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ReproductorMusica(ventana)
    ventana.mainloop()