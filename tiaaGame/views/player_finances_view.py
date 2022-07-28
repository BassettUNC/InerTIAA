import arcade
import tiaaGame.constants as constants
from tiaaGame.player import Player as player

class PlayerFinancesView(arcade.View):
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
        self.background = arcade.load_texture("././resources/views/screen3.png")

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(constants.LIGHTER_BLUE)

    def on_hide_view(self):
        self.manager.disable()
    
    def stringMaker(self, a):
        madeString: str = ""
        i = 0
        for description in a:
            if i % 2 == 0:
                madeString + ": "
                i += 1
            else: 
                madeString + ",  "
                i+= 1
        if i == 0:
            return "N/A"
        return madeString


    def on_draw(self):
        self.clear()        
        self.manager.draw()
        arcade.draw_text(
            "Your Finances",
            self.window.width / 2,
            self.window.height - 80,
            constants.DARK_BLUE,
            constants.DEFAULT_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Beginning Yearly Balance:  " + str(int(player.balance_before_expenses)),
            self.window.width / 2,
            self.window.height - 250,
            constants.DARK_BLUE,
            constants.SMALL_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Ending Yearly Balance:  " + str(int(player.balance)),
            self.window.width / 2,
            self.window.height - 300,
            constants.DARK_BLUE,
            constants.SMALL_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Recurring Payments:  " + str(player.yearly_financed_expenses),
            self.window.width / 2,
            self.window.height - 400,
            constants.DARK_BLUE,
            constants.SMALL_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )
        arcade.draw_text(
            "Outright Payments:  " +  str(player.yearly_outright_expenses),
            self.window.width / 2,
            self.window.height - 550,
            constants.DARK_BLUE,
            constants.SMALL_FONT_SIZE,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )

    # call back methods for buttons:
    def on_click_t1(self, event):
        player.buyItem("house0", False)

    def on_click_t2(self, event):
        player.buyItem("house1", False)

    def on_click_t3(self, event):
        player.buyItem("house2", False)

    def on_click_b1(self, event):
        player.buyItem("house0", True)

    def on_click_b2(self, event):
        player.buyItem("house1", True)

    def on_click_b3(self, event):
        player.buyItem("house2", True)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["game"])
