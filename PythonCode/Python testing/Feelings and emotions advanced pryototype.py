"""
A prgram to display a list of feelings from which you can pick from and 
receive quotes based on your choice.
"""

import arcade
import arcade.gui
from arcade.gui import UIManager

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()

#window dimensions
WIDTH = 800
HEIGHT = 600

#Welcome page application class.
class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLANCHED_ALMOND)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


#Logic for the emotions



#Second page (how are you feeling?)
class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLANCHED_ALMOND)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text('How are you feeling today?',200,500,arcade.color.BLACK_BEAN, 30)
        arcade.draw_line(195,495,625,495,arcade.color.BLACK_OLIVE,2)

class MyGame(arcade.Window):
    """
    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    #button stuff
# right side elements



class MyFlatButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        """ Called when user lets off button """
        print("Click flat button. ")


button = MyFlatButton(
             'FlatButton',
             center_x=300,
            center_y=200 * 1,
             width=500,
             Height=200,)


class MyView(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()



    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLANCHED_ALMOND)
    


def main():
    window = arcade.Window(WIDTH, HEIGHT, "How are you feeling.")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()