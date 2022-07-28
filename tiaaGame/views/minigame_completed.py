import arcade
import arcade.gui

from tiaaGame.views.minigame_view import View
from tiaaGame.player import Player as ply
from tiaaGame.constants import *

class Completed(View):
    def __init__(self):
        super().__init__()

        self.v_box = None

    def setup(self):
        super().setup()

        self.ui_manager = arcade.gui.UIManager()

        self.setup_buttons()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxLayout()

        OK_button = arcade.gui.UIFlatButton(text="OK", width=200, style= default_style)

        @OK_button.event("on_click")
        def on_click_OK(event):
            self.window.views["game"].setup()
            self.window.show_view(self.window.views["game"])

        self.v_box.add(OK_button.with_space_around(top= 100))

        self.window.views.pop('game2', None)
        self.window.views.pop('game_over', None)
        self.window.views.pop('pause', None)
        self.window.views.pop('Completed', None)
        

        

        

    def on_show_view(self):
        arcade.set_background_color(LIGHT_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            f"Congrats You've Reached 100 Points!",
            self.window.width / 2,
            self.window.height / 2 + 100,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center",
        )
        arcade.draw_text(
            f"You've Earned ${ply.yearly_salary}",
            self.window.width / 2,
            self.window.height / 2 + 40,
            arcade.color.WHITE,
            30,
            anchor_x="center",
            anchor_y="center",
        )
        self.ui_manager.draw()