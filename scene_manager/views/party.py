import arcade
from gui import ActionButton

class PartyView(arcade.View):

    def __init__(self, width, height, done_func=None):
        super().__init__()
        self.center_x = width / 2
        self.center_y = height / 2
        self.done_func = done_func
        self.fruits = []

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)
        apple_button = ActionButton(self.center_x, self.center_y - 50,'apple',self.button_handler)
        self.button_list.append(apple_button)
        banana_button = ActionButton(self.center_x, self.center_y - 100,'banana',self.button_handler)
        self.button_list.append(banana_button)
        cucumber_button = ActionButton(self.center_x, self.center_y - 150,'cucumber',self.button_handler)
        self.button_list.append(cucumber_button)
        ok_button = ActionButton(self.center_x, self.center_y - 200,'ok',self.button_handler)
        self.button_list.append(ok_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game - Choose something", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        super().on_draw()

    def button_handler(self, button):
        if button.name == 'ok':
            self.done_func(self.fruits, 123)
        else:
            self.fruits.append(button.name)
