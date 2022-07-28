import arcade
import arcade.gui
import tiaaGame.constants as constants

class StocksView(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.v_boxL = arcade.gui.UIBoxLayout()
        self.v_boxR = arcade.gui.UIBoxLayout()

        stock_button_one = arcade.gui.UIFlatButton(text="Low Stock", width = 200, style=constants.default_style)
        self.v_boxL.add(stock_button_one.with_space_around(bottom=50, left = 120, top=190))
        stock_button_one.on_click = self.on_click_stock_one

        stock_button_second = arcade.gui.UIFlatButton(text="Mid Stock", width = 200, style=constants.default_style)
        self.v_boxL.add(stock_button_second.with_space_around(bottom=50, left = 120))
        stock_button_second.on_click = self.on_click_stock_second

        stock_button_third = arcade.gui.UIFlatButton(text="High Stock", width = 200, style=constants.default_style)
        self.v_boxR.add(stock_button_third.with_space_around(bottom=50, right=120, top=190))
        stock_button_third.on_click = self.on_click_stock_third

        to_bank_button = arcade.gui.UIFlatButton(text = "Return to the Bank Menu", width = 200, style=constants.default_style)
        self.v_boxR.add(to_bank_button.with_space_around(bottom=50, right=120))
        to_bank_button.on_click = self.on_click_to_bank

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

    def on_click_to_bank(self, event):
        print("show bank view")
        self.window.show_view(self.window.views["bank"])
    
    def on_click_stock_one(self, event):
        print("Stock 1")
        self.window.show_view(self.window.views["stock_one"])
    
    def on_click_stock_second(self, event):
        print("Stock 2")
        self.window.show_view(self.window.views["stock_two"])
    
    def on_click_stock_third(self, event):
        print("Stock 3")
        self.window.show_view(self.window.views["stock_three"])

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["bank"])