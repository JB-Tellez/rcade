import arcade

from views import IntroView, ChoosePartyView, StartJourneyView


class SceneManager:

    def __init__(self):
        self.window = arcade.Window(800, 600, "Oregon Trail")
        self.state = {}

    def start(self):
        self.show_next_view(IntroView, {'done_handler':self.intro_done})
        arcade.run()

    def show_next_view(self, ViewClass, props):
        view = ViewClass(self.window.width, self.window.height, props)
        self.window.show_view(view)

    def intro_done(self):
        props = {
            'done_handler' : self.choose_party_done
        }

        self.show_next_view(ChoosePartyView, props)

    def choose_party_done(self, wagon_party, starting_funds):
        self.state['wagon_party'] = wagon_party
        self.state['starting_funds'] = starting_funds
        props = {
            'done_handler' : self.start_journey_done,
            'travelers' : wagon_party
        }
        self.show_next_view(StartJourneyView, props)

    def start_journey_done(self):
        print('Start Journey done')
        pass


if __name__ == "__main__":
    sm = SceneManager()
    sm.start()
