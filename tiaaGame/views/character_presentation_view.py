"""
Settings
"""
import arcade
import tiaaGame.constants as constants
from tiaaGame.player import Player as player


class CharacterPresentation(arcade.View):
    def __init__(self):
        super().__init__()
        self.started = False
        arcade.set_background_color(constants.LIGHTER_GREY)

        # --- Required for all code that uses UI element, a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Load background image
        self.background = arcade.load_texture("././resources/views/startmenubackground.png")

        resume_button = arcade.gui.UIFlatButton(text="Continue", width=200, style = constants.default_style)
        self.v_box.add(resume_button.with_space_around(top = 300, bottom=20))
        resume_button.on_click = self.on_click_resume

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left", anchor_y="center_y", align_x = constants.SCREEN_WIDTH/2 - 100, child=self.v_box
            )
        )

        # Create new Player
        player.createPlayer()

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()
        arcade.draw_text(
            "Your Character",
            self.window.width / 2,
            self.window.height - 70,
            constants.DARK_BLUE,
            constants.HEADER_FONT_SIZE,
            font_name= constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Name:   " + player.fname + " " + player.lname,
            self.window.width / 2,
            self.window.height - 220,
            constants.MEDIUM_BLUE,
            constants.DEFAULT_FONT_SIZE,
            font_name= constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Occupation:   " + player.occupation,
            self.window.width / 2,
            self.window.height - 270,
            constants.MEDIUM_BLUE,
            constants.DEFAULT_FONT_SIZE,
            font_name= constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Age:   " + str(player.age),
            self.window.width / 2,
            self.window.height - 320,
            constants.MEDIUM_BLUE,
            constants.DEFAULT_FONT_SIZE,
            font_name=constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )

    def setup(self):
        pass

    def on_show_view(self):
        arcade.set_background_color(constants.LIGHTER_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        self.manager.enable()
    
    def on_hide_view(self):
        self.manager.disable()
    
    # call back methods for buttons:
    def on_click_resume(self, event):
        print("show game view")
        self.window.show_view(self.window.views["game"])

    def on_key_press(self, symbol: int, modifiers: int):
        pass