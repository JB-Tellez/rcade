"""
Modified from http://arcade.academy/examples/view_screens_minimal.html#view-screens-minimal
So go there and read that, for real
"""

import arcade
import os
from views.menu import MenuView
from views.party import PartyView
from views.store import StoreView

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 800
HEIGHT = 600

window = arcade.Window(WIDTH, HEIGHT, "Multi View Example")

# transition functions 

def show_next_view(ViewClass, done_func=None):
    view = ViewClass(WIDTH, HEIGHT, done_func)
    window.show_view(view)

def store_done():
    print('all done')

# look, you can send things back from scene/view
def party_done(things, num):
    print('things', things)
    print('number', num)
    show_next_view(StoreView, lambda : show_next_view(StoreView, store_done))

def menu_done():
    show_next_view(PartyView, party_done)

def main():
    show_next_view(MenuView, menu_done)
    arcade.run()


if __name__ == "__main__":
    main()