from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.config import Config
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.window import Window

import os
from server_link import get_sentiment

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ui.kv'))

# don't include this line when compiling for mobile
Window.size = (440,836)

# Define the colors we need in RGB
BLACK = [0, 0, 0]
RED = [1, 0, 0]
GREEN = [0, 1, 0]

class SeparatorBar(Widget):
    pass

class MainInterface(Widget):
    
    # Points to the TextInput panel where user can enter text
    text_input = ObjectProperty(None)
    background_color = ListProperty(BLACK)

    def go_button_pressed(self):
        current_text = self.text_input.text
        if current_text == "":
            return
        
        # Attempt to get the sentiment from the server. 
        try:
            sentiment = get_sentiment(current_text)
        except IOError:
            popup = Popup(title='Error', content=Label(text='Server Error!'))
            popup.open()
            return
        if sentiment is None:
            return

        # If we successfully got the sentiment from the server, then choose
        # a RED or GREEN background (for negative or positive, respectively),
        # and change the alpha (opacity) of the background to reflect the
        # intensity.
        if sentiment < 0:
            self.background_color = RED + [abs(sentiment)]
        else:
            self.background_color = GREEN + [abs(sentiment)]

if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainInterface())
