from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")


class WidgetsExemple(GridLayout):

    compteur = 1
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    text_input_str = StringProperty("")

    def on_button_click(self):

        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self, widget):

        if widget.state == "normal":
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, widget):
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class ImagesExemple(GridLayout):
    pass


class ImagesSnail(BoxLayout):
    pass
