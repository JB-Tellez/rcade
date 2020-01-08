import arcade

class StoreView(arcade.View):

    def __init__(self, width, height, done_func=None):
        super().__init__()
        self.center_x = width / 2
        self.center_y = height / 2
        self.done_func = done_func

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over - press ESCAPE to advance", self.center_x, self.center_y,
                         arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            self.done_func()