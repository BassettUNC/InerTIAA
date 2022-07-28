# """
# Start Menu
# """
import arcade
import arcade.gui
import tiaaGame.constants as constants

class StartMenuView(arcade.View):

    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element, a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Load background image
        self.background = arcade.load_texture("././resources/views/startmenubackground.png")

        resume_button = arcade.gui.UIFlatButton(text="New Game", width=200, style = constants.inverse_style)
        self.v_box.add(resume_button.with_space_around(top = 270, bottom=20))
        resume_button.on_click = self.on_click_resume

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200, style = constants.default_style)
        self.v_box.add(quit_button.with_space_around(bottom=20))
        quit_button.on_click = self.on_click_quit
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def on_show_view(self):
        self.manager.enable()
        arcade.set_background_color(arcade.color.WHITE)

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        #arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2 - 10, 300, 300, arcade.load_texture("././resources/views/logo.png"))
        self.manager.draw()
        arcade.draw_text(
            "InerTIAA",
            self.window.width / 2,
            self.window.height - 150,
            arcade.color.WHITE,
            170,
            font_name= constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )

    # call back methods for buttons:
    def on_click_resume(self, event):
        print("show game view")
        self.window.show_view(self.window.views["character_presentation"])

    def on_click_quit(self, event):
        print("quitting")
        self.window.close()

    def on_key_press(self, key, _modifiers):
       pass
