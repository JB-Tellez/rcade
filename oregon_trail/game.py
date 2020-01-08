import arcade
import os
import sys

from views import IntroView, ChoosePartyView, StartJourneyView


class SceneManager:

    def __init__(self):
        self.window = arcade.Window(800, 600, "Oregon Trail")
        self.state = {}

    def start(self):
        self.show_next_view(IntroView, self.intro_done)
        arcade.run()

    def show_next_view(self, ViewClass, done_func=None):
        view = ViewClass(self.window.width, self.window.height, done_func)
        self.window.show_view(view)

    def intro_done(self):
        self.show_next_view(ChoosePartyView, self.choose_party_done)

    def choose_party_done(self, wagon_party, starting_funds):
        self.state['wagon_party'] = wagon_party
        self.state['starting_funds'] = starting_funds
        print(self.state)
        # show_next_view(StartJourneyView,self.start_journey_done)
        view = StartJourneyView(self.window.width, self.window.height, self.start_journey_done)
        view.state = self.state
        self.window.show_view(view)

    def start_journey_done(self):
        pass

    




if __name__ == "__main__":
    sm = SceneManager()
    sm.start()
