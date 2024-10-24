from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import NoTransition, SlideTransition
from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = []
    current_screen_name = StringProperty("")

    def start_app(self):
        self.current = "page_acceuil"

    def push(self, screen_name, transition_duration=0.1):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition = SlideTransition(direction="left", duration=transition_duration)
            self.current = screen_name

    def pop(self, transition_duration=0.3):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition = SlideTransition(direction="right", duration=transition_duration)
            self.current = screen_name

    def no_transition(self, screen_name):
        if screen_name not in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition = NoTransition()
            self.current = screen_name


class LeLabApp(App):
    def build(self):
        nav_manager = NavigationScreenManager()
        return nav_manager


if __name__ == "__main__":
    LeLabApp().run()
