"""
Main Menu
"""
import arcade
import arcade.gui

from tiaaGame.views.minigame_view import View
from tiaaGame.views.minigame_view_game import GameView2
from tiaaGame.views.minigame_view_game_over import GameOverView
from tiaaGame.views.minigame_view_pause import PauseView
from tiaaGame.views.minigame_completed import Completed
from tiaaGame.constants import *


class WorkView(View):
    def __init__(self):
        super().__init__()

        # A Horizontal BoxGroup to align Buttons
        self.h_box_upper = None
        self.h_box_lower = None

        self.selected_player = None

    def setup(self):
        super().setup()
        self.ui_manager = arcade.gui.UIManager()

        self.setup_buttons()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.h_box_upper
            )
        )
        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                align_y=100,
                child=self.h_box_lower,
            )
        )

    def on_show_view(self):
        arcade.set_background_color(LIGHTER_BLUE)

    def setup_buttons(self):
        self.h_box_upper = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box_lower = arcade.gui.UIBoxLayout(vertical=False)

        button1 = arcade.gui.UIFlatButton(text="Platformer", height = 100, width=300, style = default_style )
        @button1.event("on_click")
        def on_click_button1(event):
            self.selected_player = "Platformer"
        
        self.h_box_upper.add(button1.with_space_around(right=20))


        button2 = arcade.gui.UIFlatButton(text="Snake", height = 100, width=300, style = default_style )
        @button2.event("on_click")
        def on_click_button2(event):
            self.selected_player = "Snake"
        
        self.h_box_upper.add(button2.with_space_around(right=20))

        button3 = arcade.gui.UIFlatButton(text="Tic Tac Toe", height = 100, width=300, style = default_style )
        @button3.event("on_click")
        def on_click_button3(event):
            self.selected_player = "Tic Tac Toe"
        
        self.h_box_upper.add(button3.with_space_around(right=20))

        play_button = arcade.gui.UIFlatButton(text="Start Work", width=200, style = default_style )

        @play_button.event("on_click")
        def on_click_play(event):
            self.window.show_view(self.window.views["platformer"])

        self.h_box_lower.add(play_button.with_space_around(right=20))

        back_button = arcade.gui.UIFlatButton(text="Back", width=200, style=default_style)

        @back_button.event("on_click")
        def on_click_back(event):
            self.window.show_view(self.window.views["game"])

        self.h_box_lower.add(back_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Select a Game",
            self.window.width / 2,
            self.window.height - 200,
            DARK_BLUE,
            font_size=44,
            font_name= DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            f"Selected Game: {self.selected_player}",
            self.window.width / 2,
            200,
            DARK_BLUE,
            font_size=24,
            font_name= DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
