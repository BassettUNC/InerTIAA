import arcade
import arcade.gui
import tiaaGame.constants as constants

class BankView(arcade.View):
    """
    This class acts as the view for accessing the main bank menu.
    """

    def __init__(self):
        super().__init__()

        # Required for all code that uses UI element, a UIManger to handle the UI.
        self.manager = arcade.gui.UIManager()

        # Create a vertical BoxGroup to align buttons
        self.v_boxL = arcade.gui.UIBoxLayout()
        self.v_boxR = arcade.gui.UIBoxLayout()


        stocks_button = arcade.gui.UIFlatButton(text = "Stocks", width = 200, style=constants.default_style)
        self.v_boxL.add(stocks_button.with_space_around(bottom=50, left = 120, top=190))
        stocks_button.on_click = self.on_click_stocks

        financial_button = arcade.gui.UIFlatButton(text = "Financial Data", width = 200, style=constants.default_style)
        self.v_boxL.add(financial_button.with_space_around(bottom=50, left = 120))
        financial_button.on_click = self.on_click_financial

        retirement_button = arcade.gui.UIFlatButton(text = "Retirement", width = 200, style=constants.default_style)
        self.v_boxR.add(retirement_button.with_space_around(bottom=50, right=120, top=190))
        retirement_button.on_click = self.on_click_retirement

        resume_button = arcade.gui.UIFlatButton(text="Resume Game", width=200, style=constants.default_style)
        self.v_boxR.add(resume_button.with_space_around(bottom=50, right = 120))
        resume_button.on_click = self.on_click_resume

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                anchor_y = "center_y",
                child = self.v_boxL
            )
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "right",
                anchor_y = "center_y",
                child = self.v_boxR
            )
        )

        self.background = arcade.load_texture("././resources/views/ATM2.png")

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(constants.MEDIUM_BLUE)
         

    def on_hide_view(self):
        self.manager.disable()
        
    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)   
        self.manager.draw()

    def on_click_stocks(self, event):
        print("Stocks View Here")
        self.window.show_view(self.window.views["stock"])
        
    def on_click_financial(self, event):
        print("Financial View Here")
        self.window.show_view(self.window.views["player_finances"])
        
    def on_click_retirement(self, event):
        self.window.show_view(self.window.views["retirement"])
        
    def on_click_resume(self, event):
        print("Game View Here")
        self.window.show_view(self.window.views["game"])

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["game"])