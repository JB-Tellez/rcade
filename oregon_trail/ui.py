import arcade
from arcade.gui import TextButton

class ActionButton(TextButton):
    def __init__(self, center_x, center_y, text, action_function=None, name=None):
        super().__init__(center_x, center_y, 100, 40, text, 18, "Arial", font_color=arcade.color.ALIZARIN_CRIMSON)
        self.action_function = action_function
        self.name = name or text
    
    def on_press(self):
        self.action_function(self)