from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("layout_exemples.kv")


class BoxLayoutExemple(BoxLayout):
    pass


class AnchorLayoutExemple(AnchorLayout):
    pass


class StackLayoutExemple(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"

        for i in range(0, 50):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(55), dp(55)))
            self.add_widget(b)


class ScrollStack(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class LayoutExemplesTabs(TabbedPanel):
    pass
