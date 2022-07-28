"""
Game View
"""
import math
import os

import arcade

from tiaaGame.constants import *
from tiaaGame.entities import Player, Robot, Zombie
from tiaaGame.player import Player as ply



from arcade import View as ArcadeView


class View(ArcadeView):
    def __init__(self):
        super().__init__()

        # Used to track if a view has been ran it's setup function or not
        self.started = False

        # The views UI manager, this is optional for a view to use
        self.ui_manager = None

    def setup(self):
        self.started = True

    def on_show(self):
        if not self.started:
            self.setup()

        if self.ui_manager:
            self.ui_manager.enable()

    def on_hide_view(self):
        if self.ui_manager:
            self.ui_manager.disable()


class GameView2(View):
    def __init__(self):
        """
        Initializer for the game
        """
        super().__init__()
        
        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.shoot_pressed = False
        self.jump_needs_reset = False

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our 'physics' engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        self.end_of_map = 0

        # Keep track of the score
        self.score = 0

        # Shooting mechanics
        self.can_shoot = False
        self.shoot_timer = 0

        # The selected player
        self.selected_player = 0

        # Load sounds
        # self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        # self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        # self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")
        # self.shoot_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        # self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        super().setup()

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.shoot_pressed = False
        self.jump_needs_reset = False

        # Setup the Cameras
        self.camera = arcade.Camera(self.window.width, self.window.height)
        self.gui_camera = arcade.Camera(self.window.width, self.window.height)

        # Map name
        map_name = ":resources:tiled_maps/map_with_ladders.json"

        # Layer Specific Options for the Tilemap
        layer_options = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_MOVING_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_LADDERS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
        }

        # Load in TileMap
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING_plt, layer_options)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Keep track of the score
        self.score = 0

        # Shooting mechanics
        self.can_shoot = True
        self.shoot_timer = 0

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = Player(self.selected_player)
        self.player_sprite.center_x = (
            self.tile_map.tiled_map.tile_size[0] * TILE_SCALING_plt * PLAYER_START_X
        )
        self.player_sprite.center_y = (
            self.tile_map.tiled_map.tile_size[1] * TILE_SCALING_plt * PLAYER_START_Y
        )
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player_sprite)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.tiled_map.map_size.width * GRID_PIXEL_SIZE_plt

        # -- Enemies
        enemies_layer = self.tile_map.object_lists[LAYER_NAME_ENEMIES]

        for my_object in enemies_layer:
            cartesian = self.tile_map.get_cartesian(
                my_object.shape[0], my_object.shape[1]
            )
            enemy_type = my_object.properties["type"]
            if enemy_type == "robot":
                enemy = Robot()
            elif enemy_type == "zombie":
                enemy = Zombie()
            enemy.center_x = math.floor(
                cartesian[0] * TILE_SCALING * self.tile_map.tile_width
            )
            enemy.center_y = math.floor(
                (cartesian[1] + 1) * (self.tile_map.tile_height * TILE_SCALING)
            )
            if "boundary_left" in my_object.properties:
                enemy.boundary_left = my_object.properties["boundary_left"]
            if "boundary_right" in my_object.properties:
                enemy.boundary_right = my_object.properties["boundary_right"]
            if "change_x" in my_object.properties:
                enemy.change_x = my_object.properties["change_x"]
            self.scene.add_sprite(LAYER_NAME_ENEMIES, enemy)

        # Add bullet spritelist to Scene
        self.scene.add_sprite_list(LAYER_NAME_BULLETS)

        # --- Other stuff
        # Set the background color
        if self.tile_map.tiled_map.background_color:
            arcade.set_background_color(self.tile_map.tiled_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            [
                self.scene.get_sprite_list(LAYER_NAME_PLATFORMS),
                self.scene.get_sprite_list(LAYER_NAME_MOVING_PLATFORMS),
            ],
            gravity_constant=GRAVITY,
            ladders=self.scene.get_sprite_list(LAYER_NAME_LADDERS),
        )

    def on_show_view(self):
        arcade.set_background_color(self.tile_map.background_color)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        arcade.start_render()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.BLACK,
            18,
        )

        # Draw hit boxes.
        # for wall in self.wall_list:
        #     wall.draw_hit_box(arcade.color.BLACK, 3)
        #
        # self.player_sprite.draw_hit_box(arcade.color.RED, 3)

    def process_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
            elif (
                self.physics_engine.can_jump(y_distance=10)
                and not self.jump_needs_reset
            ):
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.jump_needs_reset = True
               # arcade.play_sound(self.jump_sound)
        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.player_sprite.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        if key == arcade.key.Q:
            self.shoot_pressed = True

        if key == arcade.key.ESCAPE:
            self.window.show_view(self.window.views["pause"])

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        if key == arcade.key.Q:
            self.shoot_pressed = False

        self.process_keychange()

    def center_camera_to_player(self, speed=0.2):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, speed)

    def on_update(self, delta_time):
        """Movement and game logic"""
        if self.score > 100:
            ply.workProgress()
            self.window.show_view(self.window.views["Completed"])
            ply.popupError("You've completed work!")
            return


        # Move the player with the physics engine
        self.physics_engine.update()

        # Update animations
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        if self.physics_engine.is_on_ladder() and not self.physics_engine.can_jump():
            self.player_sprite.is_on_ladder = True
            self.process_keychange()
        else:
            self.player_sprite.is_on_ladder = False
            self.process_keychange()

        if self.can_shoot:
            if self.shoot_pressed:
                #arcade.play_sound(self.shoot_sound)
                bullet = arcade.Sprite(
                    ":resources:images/space_shooter/laserBlue01.png",
                    SPRITE_SCALING_LASER,
                )

                if self.player_sprite.facing_direction == RIGHT_FACING:
                    bullet.change_x = BULLET_SPEED
                else:
                    bullet.change_x = -BULLET_SPEED

                bullet.center_x = self.player_sprite.center_x
                bullet.center_y = self.player_sprite.center_y

                self.scene.add_sprite(LAYER_NAME_BULLETS, bullet)

                self.can_shoot = False
        else:
            self.shoot_timer += 1
            if self.shoot_timer == SHOOT_SPEED:
                self.can_shoot = True
                self.shoot_timer = 0

        # Update Animations
        self.scene.update_animation(
            delta_time,
            [
                LAYER_NAME_COINS,
                LAYER_NAME_BACKGROUND,
                LAYER_NAME_PLAYER,
                LAYER_NAME_ENEMIES,
            ],
        )

        # Update moving platforms, enemies, and bullets
        self.scene.update(
            [LAYER_NAME_MOVING_PLATFORMS, LAYER_NAME_ENEMIES, LAYER_NAME_BULLETS]
        )

        # See if the enemy hit a boundary and needs to reverse direction.
        for enemy in self.scene.get_sprite_list(LAYER_NAME_ENEMIES):
            if (
                enemy.boundary_right
                and enemy.right > enemy.boundary_right
                and enemy.change_x > 0
            ):
                enemy.change_x *= -1

            if (
                enemy.boundary_left
                and enemy.left < enemy.boundary_left
                and enemy.change_x < 0
            ):
                enemy.change_x *= -1

        # See if the moving wall hit a boundary and needs to reverse direction.
        for wall in self.scene.get_sprite_list(LAYER_NAME_MOVING_PLATFORMS):

            if (
                wall.boundary_right
                and wall.right > wall.boundary_right
                and wall.change_x > 0
            ):
                wall.change_x *= -1
            if (
                wall.boundary_left
                and wall.left < wall.boundary_left
                and wall.change_x < 0
            ):
                wall.change_x *= -1
            if wall.boundary_top and wall.top > wall.boundary_top and wall.change_y > 0:
                wall.change_y *= -1
            if (
                wall.boundary_bottom
                and wall.bottom < wall.boundary_bottom
                and wall.change_y < 0
            ):
                wall.change_y *= -1

        player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [
                self.scene.get_sprite_list(LAYER_NAME_COINS),
                self.scene.get_sprite_list(LAYER_NAME_ENEMIES),
            ],
        )

        for bullet in self.scene.get_sprite_list(LAYER_NAME_BULLETS):
            hit_list = arcade.check_for_collision_with_lists(
                bullet,
                [
                    self.scene.get_sprite_list(LAYER_NAME_ENEMIES),
                    self.scene.get_sprite_list(LAYER_NAME_PLATFORMS),
                    self.scene.get_sprite_list(LAYER_NAME_MOVING_PLATFORMS),
                ],
            )

            if hit_list:
                bullet.remove_from_sprite_lists()

                for collision in hit_list:
                    if (
                        self.scene.get_sprite_list(LAYER_NAME_ENEMIES)
                        in collision.sprite_lists
                    ):
                        # The collision was with an enemy
                        collision.health -= BULLET_DAMAGE

                        if collision.health <= 0:
                            collision.remove_from_sprite_lists()
                            self.score += 100

                        # Hit sound
                        #arcade.play_sound(self.hit_sound)

                return

            if (bullet.right < 0) or (
                bullet.left
                > (self.tile_map.width * self.tile_map.tile_width) * TILE_SCALING
            ):
                bullet.remove_from_sprite_lists()


        # Loop through each coin we hit (if any) and remove it
        for collision in player_collision_list:

            if self.scene.get_sprite_list(LAYER_NAME_ENEMIES) in collision.sprite_lists:
                #logic to make money with score in game
                #ply.balance += self.score
                #arcade.play_sound(self.game_over)
                self.window.show_view(self.window.views["game_over"])
                return
            else:
                # Figure out how many points this coin is worth
                if "Points" not in collision.properties:
                    print("Warning, collected a coin without a Points property.")
                else:
                    points = int(collision.properties["Points"])
                    self.score += points

            


                # Remove the coin
                collision.remove_from_sprite_lists()
                #arcade.play_sound(self.collect_coin_sound)
            

        # Position the camera
        self.center_camera_to_player()
