from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Builder.load_file("snail_game.kv")


class Snail(FloatLayout):
    is_active = BooleanProperty(False)
    opacite_fondu = NumericProperty(0)
    collision = True

    sounds = {
        "snail": SoundLoader.load("sons/snail.ogg"),
        "mole": SoundLoader.load("sons/ploc.ogg"),
        "tada": SoundLoader.load("sons/tada.ogg"),
        "game_over": SoundLoader.load("sons/game_over.ogg"),
        "clic": SoundLoader.load("sons/clic_mouse.ogg"),
        "friction": SoundLoader.load("sons/friction.ogg")
    }

    def play_sound(self, sound_name, volume=0.3):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.volume = volume
            sound.play()

    # ------------------------------------------------------------------------------

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.snail = Image(source="images/Escargot.png", pos=(dp(100), dp(10)), size_hint=(
            0.13, 0.13))

        self.mole = Image(source="images/taupe.png", pos=(dp(100), dp(200)), size_hint=(0.2, 0.2))

        self.rock0 = Image(source="images/pierres.png", pos=(dp(20), dp(120)), size_hint=(0.2, 0.2))
        self.rock0.vx = dp(5)
        self.rock0.vy = dp(5)

        self.rock1 = Image(source="images/pierres.png", pos=(dp(200), dp(220)), size_hint=(0.2, 0.2))
        self.rock1.vx = dp(6)
        self.rock1.vy = dp(6)

        self.rock2 = Image(source="images/pierres.png", pos=(dp(100), dp(320)), size_hint=(0.2, 0.2))
        self.rock2.vx = dp(7)
        self.rock2.vy = dp(7)

        self.rock3 = Image(source="images/pierres.png", pos=(dp(20), dp(420)), size_hint=(0.2, 0.2))
        self.rock3.vx = dp(8)
        self.rock3.vy = dp(8)

        self.rock_list = [self.rock0, self.rock1, self.rock2, self.rock3]

        for e in self.rock_list:
            self.add_widget(e)

        self.add_widget(self.snail)
        self.add_widget(self.mole)

        self.vx_mole = dp(5)
        self.vy_mole = dp(5)

        self.update_event = Clock.schedule_interval(self.general_update, 1 / 30)

    def general_update(self, dt):
        if self.is_active:

            self.update_mole(dt)
            self.update_rocks(dt)

    def update_mole(self, dt):

        if not self.is_active:
            return

        x, y = self.mole.pos

        x += self.vx_mole
        y += self.vy_mole

        parent = self.mole.parent

        if parent:

            if self.is_active and y + self.mole.height > parent.height:

                y = parent.height - self.mole.height
                self.vy_mole = -self.vy_mole
                self.play_sound("mole")

            elif self.is_active and x + self.mole.width > parent.width:

                x = parent.width - self.mole.width
                self.vx_mole = -self.vx_mole
                self.play_sound("mole")

            elif self.is_active and y < 0:

                y = 0
                self.vy_mole = -self.vy_mole
                self.play_sound("mole")

            elif self.is_active and x < 0:

                x = 0
                self.vx_mole = -self.vx_mole
                self.play_sound("mole")

            self.mole.pos = x, y

        if self.check_collision_mole(self.mole, self.snail):

            Clock.unschedule(self.update_event)

            self.ids.play_game.text = "  Perdu :(\nRecommencer ?"

            self.disable_arrows()

            self.play_sound("game_over", 0.2)

            self.active_play_boutton()

    def update_rocks(self, dt):

        for element in self.rock_list:

            x, y = element.pos

            x += element.vx

            parent = element.parent

            if parent:

                if x + element.width > parent.width:
                    x = parent.width - element.width
                    element.vx = -element.vx

                elif x <= 0:
                    x = 0
                    element.vx = -element.vx

            if self.check_collision_rocks(self.snail, self.rock_list):

                self.opacite_fondu = 0.5

                self.play_sound("friction")

                self.collision = True  # Bool pour stopper la progression de l'escargot

            else:

                self.opacite_fondu = 0

                self.collision = False  # Remettre à false sinon stuck dans le true

            element.pos = (x, y)

    def move_snail(self, dx=0, dy=0):

        new_x = self.snail.x + dx
        new_y = self.snail.y + dy

        if not (0 <= new_x <= self.width - self.snail.width):
            new_x = self.snail.x

        if not (0 <= new_y <= self.height - self.snail.height):
            new_y = self.snail.y

        if self.is_active and self.snail.y + dp(100) >= self.height:
            self.play_sound("tada")

            self.active_play_boutton()

            self.ids.play_game.text = "  Bravo ! :)\nRecommencer?"

            self.is_active = False

            self.disable_arrows()

        self.snail.pos = new_x, new_y

    def up(self):

        if self.is_active:

            self.snail.source = "images/Escargot.png"
            self.snail.size_hint = (0.13, 0.13)

            self.play_sound("snail")

            if self.collision:
                self.move_snail(dy=int(dp(0)))
            else:
                self.move_snail(dy=int(dp(15)))

        else:
            pass

    def down(self):

        if self.is_active:

            self.play_sound("snail")
            self.snail.source = "images/Escargot_bas.png"
            self.snail.size_hint = (0.13, 0.13)

            if self.collision:
                self.move_snail(dy=int(dp(0)))
            else:
                self.move_snail(dy=int(dp(-15)))

        else:
            pass

    def right(self):

        if self.is_active:

            self.snail.source = "images/Escargot_D.png"
            self.snail.size_hint = (0.23, 0.23)

            self.move_snail(dx=int(dp(15)))

            self.play_sound("snail")

        else:
            pass

    def left(self):

        if self.is_active:

            self.snail.source = "images/Escargot_G.png"
            self.snail.size_hint = (0.23, 0.23)

            self.move_snail(dx=int(dp(-15)))

            self.play_sound("snail")

        else:
            pass

    def check_collision_mole(self, widget1, widget2):

        collision_zone_snail = [widget1.x + widget1.width * 0.25, widget1.y + widget1.height * 0.25,
                                widget1.width * 0.5, widget1.height * 0.5]

        collision_zone_mole = [widget2.x + widget2.width * 0.25, widget2.y + widget2.height * 0.25,
                               widget2.width * 0.5, widget2.height * 0.5]

        return not (collision_zone_snail[0] + collision_zone_snail[2] < collision_zone_mole[0] or
                    collision_zone_snail[0] > collision_zone_mole[0] + collision_zone_mole[2] or
                    collision_zone_snail[1] + collision_zone_snail[3] < collision_zone_mole[1] or
                    collision_zone_snail[1] > collision_zone_mole[1] + collision_zone_mole[3])

    def check_collision_rocks(self, widget1, liste):
        for element in liste:
            collision_zone_snail = [widget1.x + widget1.width * 0.25, widget1.y + widget1.height * 0.25,
                                    widget1.width * 0.5, widget1.height * 0.5]

            collision_zone_rocks = [element.x + element.width * 0.25, element.y + element.height * 0.25,
                                    element.width * 0.5, element.height * 0.5]

            collision = not (collision_zone_snail[0] + collision_zone_snail[2] < collision_zone_rocks[0] or
                             collision_zone_snail[0] > collision_zone_rocks[0] + collision_zone_rocks[2] or
                             collision_zone_snail[1] + collision_zone_snail[3] < collision_zone_rocks[1] or
                             collision_zone_snail[1] > collision_zone_rocks[1] + collision_zone_rocks[3])

            if collision:
                return True

        return False

    def active_play_boutton(self):

        self.ids.play_game.disabled = False
        self.ids.play_game.opacity = 1
        self.is_active = False

    def deactivate_play_button(self):
        self.ids.play_game.disabled = True
        self.ids.play_game.opacity = 0
        self.is_active = True

    def start_game(self):

        self.clic_sound()

        self.snail.pos = (dp(0), dp(0))
        self.mole.pos = (dp(100), dp(200))

        self.snail.opacity = 1

        self.deactivate_play_button()

        self.vx_mole = dp(5)
        self.vy_mole = dp(5)

        self.snail.pos = (dp(100), dp(10))
        self.mole.pos = (dp(100), dp(200))

        self.update_event()

        self.enable_arrows()

        self.is_active = True

    def stop_game(self):

        self.is_active = False

        self.disable_arrows()

        Clock.unschedule(self.update_event)

        self.active_play_boutton()

        self.disable_arrows()

        self.sound_stop()

    def sound_stop(self):

        for sound_name in self.sounds.keys():
            sound = self.sounds.get(sound_name)
            if sound:
                sound.stop()

    def enable_arrows(self):

        self.ids.up.disabled = False
        self.ids.down.disabled = False
        self.ids.left.disabled = False
        self.ids.right.disabled = False

        self.ids.up.opacity = 1
        self.ids.down.opacity = 1
        self.ids.left.opacity = 1
        self.ids.right.opacity = 1

    def disable_arrows(self):

        self.ids.up.disabled = True
        self.ids.down.disabled = True
        self.ids.left.disabled = True
        self.ids.right.disabled = True

        self.ids.up.opacity = 0
        self.ids.down.opacity = 0
        self.ids.left.opacity = 0
        self.ids.right.opacity = 0

    def clic_sound(self):
        self.play_sound("clic", 1)

    def bye(self):
        self.stop_game()
