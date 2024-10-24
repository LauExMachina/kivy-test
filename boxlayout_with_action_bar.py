from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

pop_sound = SoundLoader.load("sons/pop.ogg")

Builder.load_file("boxlayout_with_action_bar.kv")


class BoxLayoutWithActionBar(BoxLayout):

    title = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def sound_pop(self):
        pop_sound.play()
