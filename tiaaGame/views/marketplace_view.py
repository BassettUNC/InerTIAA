from asyncio import constants
from tiaaGame import constants
from tiaaGame.player import Player as player
import arcade
import arcade.gui


class MarketPlaceView(arcade.View):
    """
    This class acts as the game view for the Marketplace screen and its buttons.That logic can be referenced in game_view.py
    """

    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element, a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()

        # Create a vertical BoxGroup to align buttons
        self.h_box = arcade.gui.UIBoxLayout(vertical = False)
        self.h2_box = arcade.gui.UIBoxLayout(vertical = False)

        # Load background image
        self.background = arcade.load_texture("././resources/views/screen2.png")

        # Create Buttons for cash
        t1_button = arcade.gui.UIFlatButton(text="Buy with Cash", width=200, style = constants.default_style)
        self.h_box.add(t1_button.with_space_around(top=450, right = 120))
        t1_button.on_click = self.on_click_t1
        t2_button = arcade.gui.UIFlatButton(text="Buy with Cash", width=200, style = constants.default_style)
        self.h_box.add(t2_button.with_space_around(top=450, right = 120))
        t2_button.on_click = self.on_click_t2
        t3_button = arcade.gui.UIFlatButton(text="Buy with Cash", width=200, style = constants.default_style)
        self.h_box.add(t3_button.with_space_around(top=450))
        t3_button.on_click = self.on_click_t3

        # Create Buttons for Finance
        b1_button = arcade.gui.UIFlatButton(text="Finance", width=200, style = constants.default_style)
        self.h2_box.add(b1_button.with_space_around(top=575, right = 120))
        b1_button.on_click = self.on_click_b1
        b2_button = arcade.gui.UIFlatButton(text="Finance", width=200, style = constants.default_style)
        self.h2_box.add(b2_button.with_space_around(top=575, right = 120))
        b2_button.on_click = self.on_click_b2
        b3_button = arcade.gui.UIFlatButton(text="Finance", width=200, style = constants.default_style)
        self.h2_box.add(b3_button.with_space_around(top=575))
        b3_button.on_click = self.on_click_b3

        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left", anchor_y="center_y", align_x = 75, child=self.h_box
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left", anchor_y="center_y", align_x = 75, child=self.h2_box
            )
        )

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(arcade.color.ALMOND)

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        """
        Method that redraws the UI buttons each time we call the pause menu. See game_view.py for more.
        input: None
        output: None
        """
        self.clear()
        # Draw Background image
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        
        self.manager.draw()
        arcade.draw_text(
            player.fname + "  " + player. lname,
            400,
            self.window.height - 66,
            constants.DARK_BLUE,
            15,
            anchor_x="center",
            anchor_y="center",
            align="right",
            width=self.window.width,
        )
        arcade.draw_text(
            str(int(player.balance)),
            400,
            self.window.height - 104,
            constants.DARK_BLUE,
            15,
            anchor_x="center",
            anchor_y="center",
            align="right",
            width=self.window.width,
        )

    # call back methods for buttons:
    def on_click_t1(self, event):
        player.buyItem("character0", False)

    def on_click_t2(self, event):
        player.buyItem("character1", False)

    def on_click_t3(self, event):
        player.buyItem("character2", False)

    def on_click_b1(self, event):
        player.buyItem("character0", True)

    def on_click_b2(self, event):
        player.buyItem("character1", True)

    def on_click_b3(self, event):
        player.buyItem("character2", True)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["game"])
