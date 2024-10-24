from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("appli_sound.kv")


class SoundsLab(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.waterfall_sound_obj = SoundLoader.load("sons/waterfall.ogg")
        self.birds_sound_obj = SoundLoader.load("sons/plain_birds.ogg")
        self.ambiance_sound_obj = SoundLoader.load("sons/sea_of_ice.ogg")

    def birds_sound(self, widget):
        self.toggle_sound(widget, self.birds_sound_obj, 0.3)

    def waterfall_sound(self, widget):
        self.toggle_sound(widget, self.waterfall_sound_obj, 0.3)

    def ambiance_sound(self, widget):
        self.toggle_sound(widget, self.ambiance_sound_obj, 0.3)

    def toggle_sound(self, widget,  sound_obj, volume):
        if widget.state == "normal":
            sound_obj.stop()
        else:
            sound_obj.volume = volume
            sound_obj.loop = True
            sound_obj.play()
