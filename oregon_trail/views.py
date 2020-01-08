import arcade
from gui import ActionButton
from lib import Character


class BaseView(arcade.View):

    def __init__(self, width, height, done_func=None):
        super().__init__()
        self.center_x = width / 2
        self.center_y = height / 2
        self.done_func = done_func

    def button_handler(self, button):
        self.done_func()


class IntroView(BaseView):

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        next_button = ActionButton(
            self.center_x, self.center_y + 100, 'Next', self.button_handler)
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Oregon Trail", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        super().on_draw()


class ChoosePartyView(BaseView):

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        next_button = ActionButton(
            self.center_x, self.center_y + 100, 'Next', self.button_handler)
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("ChooseParty", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        super().on_draw()

    def button_handler(self, button):
        wagon_party = [Character('Eliza'), Character(
            'Jed'), Character('Silas'), Character('Beulah')]
        starting_funds = 5000
        self.done_func(wagon_party, starting_funds)


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
