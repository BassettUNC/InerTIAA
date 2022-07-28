import arcade
import arcade.gui
import tiaaGame.constants as constants

class RetireView(arcade.View):

    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()

        self.v_boxL = arcade.gui.UIBoxLayout()
        self.v_boxR = arcade.gui.UIBoxLayout()

        fourthreeb_button = arcade.gui.UIFlatButton(text = "401k/403b", width=200, style=constants.default_style)
        self.v_boxL.add(fourthreeb_button.with_space_around(bottom=50, left=120, top=190))
        fourthreeb_button.on_click = self.on_click_fourthreeb

        ira_button = arcade.gui.UIFlatButton(text = "IRA", width=200, style=constants.default_style)
        self.v_boxL.add(ira_button.with_space_around(bottom=50, left=120))
        ira_button.on_click = self.on_click_ira

        annuity_button = arcade.gui.UIFlatButton(text = "Annuity", width=200, style=constants.default_style)
        self.v_boxR.add(annuity_button.with_space_around(bottom=50, right=120, top=190))
        annuity_button.on_click = self.on_click_annuity

        bank_home_button = arcade.gui.UIFlatButton(text = "Return to the Bank Menu", width=200, style=constants.default_style)
        self.v_boxR.add(bank_home_button.with_space_around(bottom=50, right=120))
        bank_home_button.on_click = self.on_click_return

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
        arcade.set_background_color(constants.MEDIUM_BLUE)

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self.manager.draw()

    def on_click_return(self, event):
        print("show bank view")
        self.window.show_view(self.window.views["bank"])
    
    def on_click_annuity(self, event):
        print("show annuity view")
        self.window.show_view(self.window.views["annuity"])

    def on_click_fourthreeb(self, event):
        print("show 403b/401k view")
        self.window.show_view(self.window.views["403b"])

    def on_click_ira(self, event):
        print("show ira view")
        self.window.show_view(self.window.views["ira"])

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            print("show game view")
            self.window.show_view(self.window.views["bank"])

        