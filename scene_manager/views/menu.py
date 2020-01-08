import arcade
from gui import ActionButton

class MenuView(arcade.View):
    def __init__(self, width, height, done_func=None):
        super().__init__()
        self.center_x = width / 2
        self.center_y = height / 2
        self.done_func = done_func

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        next_button = ActionButton(self.center_x,self.center_y + 100,'Next',self.button_handler)
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Start Screen", self.center_x, self.center_y,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        super().on_draw()
        
    def button_handler(self, button):
        self.done_func()