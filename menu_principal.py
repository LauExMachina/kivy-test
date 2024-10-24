from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_file("menu_principal.kv")

intro_sound = SoundLoader.load("sons/intro.ogg")


class MenuPrincipal(BoxLayout):

    bubble_sound = SoundLoader.load("sons/bubble.ogg")  # ici car aura le temps d'être chargé

    enter_once = False  # Attribut pour suivre si on_enter a déjà été appel

    def __int__(self, **kwargs):
        super().__init__(**kwargs)

    def bubble(self):
        self.bubble_sound.play()
        self.bubble_sound.volume = 0.4
        intro_sound.stop()

    def on_enter_once(self):
        if not self.enter_once:
            intro_sound.play()
            self.enter_once = True  # Marquer que on_enter a été appelé





