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


class CharacterSelectView(View):
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

        #character_one_image = "assets/images/sprites/players/download.png"
        character_one_image = "assets/images/sprites/players/person_female/character_femalePerson_idle.png"
        character_one_texture = arcade.load_texture(character_one_image)
        character_one_button = arcade.gui.UITextureButton(
            texture=character_one_texture, width=192, height=192
        )

        @character_one_button.event("on_click")
        def on_click_character_one(event):
            self.selected_player = 1

        self.h_box_upper.add(character_one_button.with_space_around(right=20))

        character_two_image = "assets/images/sprites/players/adventurer_male/character_maleAdventurer_idle.png"
        character_two_texture = arcade.load_texture(character_two_image)
        character_two_button = arcade.gui.UITextureButton(
            texture=character_two_texture, width=192, height=192
        )

        @character_two_button.event("on_click")
        def on_click_character_two(event):
            self.selected_player = 2

        self.h_box_upper.add(character_two_button.with_space_around(right=20))

        character_three_image = "assets/images/sprites/players/adventurer_female/character_femaleAdventurer_idle.png"
        character_three_texture = arcade.load_texture(character_three_image)
        character_three_button = arcade.gui.UITextureButton(
            texture=character_three_texture, width=192, height=192
        )

        @character_three_button.event("on_click")
        def on_click_character_three(event):
            self.selected_player = 3

        self.h_box_upper.add(character_three_button.with_space_around(right=20))

        character_four_image = (
            "assets/images/sprites/players/person_male/character_malePerson_idle.png"
        )
        character_four_texture = arcade.load_texture(character_four_image)
        character_four_button = arcade.gui.UITextureButton(
            texture=character_four_texture, width=192, height=192
        )

        @character_four_button.event("on_click")
        def on_click_character_four(event):
            self.selected_player = 4

        self.h_box_upper.add(character_four_button)

        play_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style = default_style )

        @play_button.event("on_click")
        def on_click_play(event):
            if self.selected_player:
                print(f"starting game with player {self.selected_player}")
                if "game2" not in self.window.views:
                    self.window.views["game2"] = GameView2()
                    self.window.views["game_over"] = GameOverView()
                    self.window.views["pause"] = PauseView()
                    self.window.views["Completed"] = Completed()
                self.window.views["game2"].selected_player = self.selected_player
                self.selected_player = None
                self.window.show_view(self.window.views["game2"])

        self.h_box_lower.add(play_button.with_space_around(right=20))

        back_button = arcade.gui.UIFlatButton(text="Quit", width=200, style=default_style)

        @back_button.event("on_click")
        def on_click_back(event):
            self.window.show_view(self.window.views["workview"])

        self.h_box_lower.add(back_button)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(
            "Select a Character",
            self.window.width / 2,
            self.window.height - 175,
            DARK_BLUE,
            font_size=44,
            font_name= DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
        )

        arcade.draw_text(
            f"Selected Character: {self.selected_player}",
            self.window.width / 2,
            200,
            DARK_BLUE,
            font_size=24,
            font_name= DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
        )

        self.ui_manager.draw()
