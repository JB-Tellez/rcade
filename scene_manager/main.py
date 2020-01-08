"""
Modified from http://arcade.academy/examples/view_screens_minimal.html#view-screens-minimal
So go there and read that, for real
"""

import arcade
import os
import sys

from views.menu import MenuView
from views.party import PartyView
from views.store import StoreView


class SceneManager:

    def __init__(self):
        self.window = arcade.Window(800, 600, "Scene Manager Example")
        self.state = {}

    def start(self):
        self.show_next_view(MenuView, self.menu_done)
        arcade.run()

    def show_next_view(self, ViewClass, done_func=None):
        view = ViewClass(self.window.width, self.window.height, done_func)
        self.window.show_view(view)

    def store_done(self):
        print('all done')
        print(self.state)
        sys.exit()

    # look, you can send things back from scene/view
    def party_done(self, things, num):
        self.state['things'] = things
        self.state['num'] = num
        self.show_next_view(StoreView, self.store_done)

    def menu_done(self):
        self.show_next_view(PartyView, self.party_done)


if __name__ == "__main__":
    sm = SceneManager()
    sm.start()
