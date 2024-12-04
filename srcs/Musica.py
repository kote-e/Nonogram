import pygame

class Musica:
    def __init__(self, ruta_musica, volumen=0.5):
        pygame.mixer.init()
        self.ruta_musica = ruta_musica
        self.volumen = volumen

    def reproducir_musica(self, loop=-1):
        try:
            pygame.mixer.music.load(self.ruta_musica)
            pygame.mixer.music.set_volume(self.volumen)
            pygame.mixer.music.play(loop)
        except pygame.error as e:
            print(f"Error al cargar la música: {e}")

    def detener_musica(self):
        pygame.mixer.music.stop()

    def pausar_musica(self):
        pygame.mixer.music.pause()

    def reanudar_musica(self):
        pygame.mixer.music.unpause()