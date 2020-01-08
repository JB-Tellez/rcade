import arcade
from ui import ActionButton
from lib import Character


class BaseView(arcade.View):

    def __init__(self, width, height, props):
        super().__init__()
        self.center_x = width / 2
        self.center_y = height / 2
        self.props = props or {}

    def button_handler(self, button):
        self.props['done_handler']()


class IntroView(BaseView):

    def __init__(self, *args, **kwargs):
        self.input_text = ''
        super().__init__(*args, **kwargs)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        next_button = ActionButton(
            self.center_x, self.center_y + 100, 'Next', self.button_handler)
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Oregon Trail", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        
        arcade.draw_text('Enter Text: ', self.center_x - 100, self.center_y - 100, arcade.color.RADICAL_RED)

        if self.input_text:
            arcade.draw_text(self.input_text, self.center_x, self.center_y - 100, arcade.color.RADICAL_RED)

        super().on_draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            self.input_text = self.input_text[:-1]
        elif key == arcade.key.ENTER:
            return self.input_text
        else:
            self.input_text += chr(key)

        return None


class ChoosePartyView(BaseView):

    def __init__(self, width, height, props):
        super().__init__(width, height, props)
        self.wagon_party = []

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

        eliza_button = ActionButton(self.center_x, self.center_y - 50,'Eliza',self.button_handler)
        self.button_list.append(eliza_button)
        jebediah_button = ActionButton(self.center_x, self.center_y - 100,'Jebediah',self.button_handler)
        self.button_list.append(jebediah_button)
        beulah_button = ActionButton(self.center_x, self.center_y - 150,'Beulah',self.button_handler)
        self.button_list.append(beulah_button)
        silas_button = ActionButton(self.center_x, self.center_y - 200,'Silas',self.button_handler)
        self.button_list.append(silas_button)
        ok_button = ActionButton(self.center_x, self.center_y - 250,'ok',self.button_handler)
        self.button_list.append(ok_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("ChooseParty", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        super().on_draw()

    def button_handler(self, button):

        if button.name == 'ok':
            starting_funds = 5000
            self.props['done_handler'](self.wagon_party, starting_funds)
        else:
            self.wagon_party.append(Character(button.name))


class StartJourneyView(BaseView):

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Start Journey", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

        travelers = [traveler.name for traveler in self.props['travelers']]

        arcade.draw_text(f"{', '.join(travelers)}", self.center_x, self.center_y - 100,
                         arcade.color.BLACK, font_size=24, anchor_x="center")

        super().on_draw()
