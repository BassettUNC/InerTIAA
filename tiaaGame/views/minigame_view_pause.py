"""
Main Menu
"""
import arcade
import arcade.gui

from tiaaGame.views.minigame_view import View
from tiaaGame.constants import *


class PauseView(View):
    def __init__(self):
        super().__init__()

        # A Vertical BoxGroup to align Buttons
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

    def on_show_view(self):
        arcade.set_background_color(LIGHTER_BLUE)

    def setup_buttons(self):
        self.v_box = arcade.gui.UIBoxLayout()

        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200, style=default_style)

        @resume_button.event("on_click")
        def on_click_play(event):
            self.window.show_view(self.window.views["game2"])

        self.v_box.add(resume_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200, style= default_style)

        @quit_button.event("on_click")
        def on_click_quit(event):
            self.window.views["game"].started = False
            self.window.show_view(self.window.views["game"])

        self.v_box.add(quit_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Paused",
            self.window.width / 2,
            self.window.height - 125,
            DARK_BLUE,
            font_size=44,
            font_name= DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
