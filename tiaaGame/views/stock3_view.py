import arcade
import arcade.gui
import tiaaGame.constants as constants
import tiaaGame.player as player

class StockThree(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.v_boxL = arcade.gui.UIBoxLayout()
        self.v_boxR = arcade.gui.UIBoxLayout()

        buy_button = arcade.gui.UIFlatButton(text="Buy", width = 200, style=constants.default_style)
        self.v_boxL.add(buy_button.with_space_around(bottom=50, left = 120, top=510))
        buy_button.on_click = self.on_click_buy

        sell_button = arcade.gui.UIFlatButton(text="Sell", width = 200, style=constants.default_style)
        self.v_boxR.add(sell_button.with_space_around(bottom=50, right = 130, top=510))
        sell_button.on_click = self.on_click_sell

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="center_y",
                child = self.v_boxL
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="center_y",
                child = self.v_boxR
            )
        )

        self.background = arcade.load_texture("././resources/views/ATM1.png")

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(arcade.color.ARSENIC)
    
    def on_hide_view(self):
        self.manager.disable()
    
    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.manager.draw()

    def on_click_buy(self, event):
        player.Player.addStock("stockHigh", 1)

    def on_click_sell(self, event):
        print("Sell Stock")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["stock"])

