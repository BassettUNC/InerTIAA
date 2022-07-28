"""
Constant values for the game
"""
from unittest.mock import DEFAULT
import arcade

SCREEN_WIDTH = 992
SCREEN_HEIGHT = 702
SCREEN_TITLE = "TIAA Innovation Game"
TILE_SCALING = 1.0
SPRITE_SIZE = 32

# How fast does the player move
MOVEMENT_SPEED = 3

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 300
RIGHT_VIEWPORT_MARGIN = 300
BOTTOM_VIEWPORT_MARGIN = 300
TOP_VIEWPORT_MARGIN = 300

# What map, and what position we start at
STARTING_MAP = "main_map"
STARTING_X = 38
STARTING_Y = 18

# Key mappings
KEY_UP = [arcade.key.UP, arcade.key.W]
KEY_DOWN = [arcade.key.DOWN, arcade.key.S]
KEY_LEFT = [arcade.key.LEFT, arcade.key.A]
KEY_RIGHT = [arcade.key.RIGHT, arcade.key.D]
INVENTORY = [arcade.key.I]
SEARCH = [arcade.key.E]

# Message box
MESSAGE_BOX_FONT_SIZE = 38
MESSAGE_BOX_MARGIN = 30

# How fast does the camera pan to the user
CAMERA_SPEED = 0.1

# TIAA colors
DARK_BLUE = (0, 56, 101)
MEDIUM_BLUE = (0, 103, 135)
LIGHT_BLUE = (0, 163, 224)
LIGHTER_BLUE = (153, 214, 234)
ACCENT_GOLD = (225, 164, 0)
WHITE = (256, 256, 256)
LIGHT_GREY = (188, 188, 188)
LIGHTER_GREY = (235, 235, 235)

# Font
DEFAULT_FONT = "Kenney Pixel"
HEADER_FONT_SIZE = 80
DEFAULT_FONT_SIZE = 40
SMALL_FONT_SIZE = 25

#Button Styles
default_style = {
    "font_name": "Kenney Pixel",
    "font_size": 30,
    "font_color": ACCENT_GOLD,
    "border_width": 2,
    "border_color": DARK_BLUE,
    "bg_color": DARK_BLUE,
    "bold": True,

    # used if button is pressed
    "bg_color_pressed": ACCENT_GOLD,
    "border_color_pressed":ACCENT_GOLD,  # also used when hovered
    "font_color_pressed": DARK_BLUE,
}

inverse_style = {
    "font_name": "Kenney Pixel",
    "font_size": 30,
    "font_color": DARK_BLUE,
    "border_width": 2,
    "border_color": ACCENT_GOLD,
    "bg_color": ACCENT_GOLD,

    # used if button is pressed
    "bg_color_pressed": DARK_BLUE,
    "border_color_pressed":DARK_BLUE,  # also used when hovered
    "font_color_pressed": ACCENT_GOLD,
}



#platformer
LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_ENEMIES = "Enemies"
LAYER_NAME_BULLETS = "Bullets"

RIGHT_FACING = 0
LEFT_FACING = 1

PLAYER_START_X = 2
PLAYER_START_Y = 1

LEFT_VIEWPORT_MARGIN_plt = 200
RIGHT_VIEWPORT_MARGIN_plt = 200
BOTTOM_VIEWPORT_MARGIN_plt = 150
TOP_VIEWPORT_MARGIN_plt = 100



SCREEN_WIDTH_plt = 1024
SCREEN_HEIGHT_plt = 768
SCREEN_TITLE_plt = "Arcade Community Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING_plt = 0.5
CHARACTER_SCALING_plt = TILE_SCALING_plt * 2
COIN_SCALING_plt = TILE_SCALING_plt
SPRITE_PIXEL_SIZE_plt = 128
GRID_PIXEL_SIZE_plt = SPRITE_PIXEL_SIZE_plt * TILE_SCALING_plt

# Shooting Constants
SPRITE_SCALING_LASER = 0.8
SHOOT_SPEED = 15
BULLET_SPEED = 12
BULLET_DAMAGE = 25

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.0
PLAYER_JUMP_SPEED = 20

