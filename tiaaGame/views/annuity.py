import arcade
import arcade.gui
import tiaaGame.constants as constants
import tiaaGame.player as player

class annuity(arcade.View):
    def __init__ (self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.v_boxL = arcade.gui.UIBoxLayout()
        self.v_boxR = arcade.gui.UIBoxLayout()

        buy_one_button = arcade.gui.UIFlatButton(text="Add 1000$", width = 200, style=constants.default_style)
        self.v_boxL.add(buy_one_button.with_space_around(bottom=50, left = 120, top=190))
        buy_one_button.on_click = self.on_click_buy_one

        buy_five_button = arcade.gui.UIFlatButton(text="Add 5000$", width = 200, style=constants.default_style)
        self.v_boxL.add(buy_five_button.with_space_around(bottom=50, left = 120))
        buy_five_button.on_click = self.on_click_buy_five
        
        buy_ten_button = arcade.gui.UIFlatButton(text="Add 10000$", width = 200, style=constants.default_style)
        self.v_boxR.add(buy_ten_button.with_space_around(bottom=50, right = 120, top=190))
        buy_ten_button.on_click = self.on_click_buy_ten

        return_to_invest = arcade.gui.UIFlatButton(text = "Return to Retirement", width = 200, style=constants.default_style)
        self.v_boxR.add(return_to_invest.with_space_around(bottom=50, right=120))
        return_to_invest.on_click = self.on_click_return

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

        self.background = arcade.load_texture("././resources/views/ATM2.png")

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(arcade.color.ARSENIC)
    
    def on_hide_view(self):
        self.manager.disable()
    
    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.manager.draw()
    
    def on_click_buy_one(self, event):
        player.Player.addinvestment("annuity", 1000)

    def on_click_buy_five(self, event):
        player.Player.addinvestment("annuity", 5000)

    def on_click_buy_ten(self, event):
        player.Player.addinvestment("annuity", 10000)

    def on_click_return(self, event):
        self.window.show_view(self.window.views["retirement"])
