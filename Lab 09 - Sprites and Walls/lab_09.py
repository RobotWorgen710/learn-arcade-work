""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
# Sprites are 64 pixels wide
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.65
SPRITE_SCALING_COIN = 0.35

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 7

VIEWPORT_MARGIN = 50

COIN_COUNT = random.randrange(40, 51)

TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1


class Player(arcade.Sprite):
    """ Represents the sprite the player will control"""
    def __init__(self):
        """ Initializer """
        super().__init__()

        # --- Allowing flipping the sprite ---
        self.scale = SPRITE_SCALING_PLAYER
        self.textures = []

        texture = arcade.load_texture("player_stand.png")
        self.textures.append(texture)
        self.texture = texture
        texture = arcade.load_texture("player_stand.png", flipped_horizontally=True)
        self.textures.append(texture)

    def update(self):

        # Flipping the sprite
        if self.change_x > 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x < 0:
            self.texture = self.textures[TEXTURE_RIGHT]


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Create the sprite
        self.player_sprite = None

        # Create the score
        self.score = None

        # Manage the view port
        self.view_left = 0
        self.view_bottom = 0

        # Tracking keys pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load coin collecting sound effect
        self.coin_sound = arcade.load_sound("coin1.wav")

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY)

        # Reset the view port
        self.view_left = 0
        self.view_bottom = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 760
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        # --- Walls in the first row ---
        for x in range(176, 496, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        for x in range(576, 784, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 100
        self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1008
        wall.center_y = 160
        self.wall_list.append(wall)

        for x in range(1264, 1648, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        for x in range(1872, 2000, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        for x in range(2224, 2480, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 160
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 2200
        wall.center_y = 100
        self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2784
        wall.center_y = 160
        self.wall_list.append(wall)

        # --- Walls in the second row ---
        for x in range(86, 278, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        for x in range(438, 694, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        for x in range(918, 1366, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        for x in range(1590, 1782, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 1680
        wall.center_y = 250
        self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1926
        wall.center_y = 304
        self.wall_list.append(wall)

        for x in range(2070, 2262, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        for x in range(2422, 2614, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        for x in range(2758, 2886, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 304
            self.wall_list.append(wall)

        # --- Walls in the third row ---
        for x in range(86, 598, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 550
        wall.center_y = 375
        self.wall_list.append(wall)

        for x in range(822, 1014, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        for x in range(1094, 1222, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        for x in range(1526, 1846, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        for x in range(1990, 2118, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2342
        wall.center_y = 448
        self.wall_list.append(wall)

        for x in range(2486, 2968, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        for x in range(86, 598, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 448
            self.wall_list.append(wall)

        # --- Walls in the fourth row ---
        for x in range(176, 304, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        for x in range(448, 576, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 800
        wall.center_y = 592
        self.wall_list.append(wall)

        for x in range(944, 1328, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 920
        wall.center_y = 540
        self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1632
        wall.center_y = 592
        self.wall_list.append(wall)

        for x in range(1776, 2096, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        for x in range(2240, 2432, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 2300
        wall.center_y = 530
        self.wall_list.append(wall)

        for x in range(2656, 2912, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 592
            self.wall_list.append(wall)

        # --- Walls in the fifth row ---
        for x in range(86, 214, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        for x in range(358, 550, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        for x in range(774, 1030, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1174
        wall.center_y = 738
        self.wall_list.append(wall)

        for x in range(1318, 1702, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        for x in range(1846, 2038, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        for x in range(2262, 2710, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        for x in range(2854, 2982, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 738
            self.wall_list.append(wall)

        # --- Walls in the sixth row ---
        for x in range(176, 368, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        for x in range(512, 768, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        for x in range(992, 1312, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        for x in range(1456, 1584, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        for x in range(1728, 2240, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        for x in range(2384, 2512, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2656
        wall.center_y = 880
        self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 2600
        wall.center_y = 830
        self.wall_list.append(wall)

        for x in range(2800, 2928, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 880
            self.wall_list.append(wall)

        # --- Walls in the seventh row ---
        for x in range(176, 304, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        for x in range(448, 704, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        for x in range(1008, 1200, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        for x in range(1344, 1600, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1744
        wall.center_y = 1024
        self.wall_list.append(wall)

        for x in range(1968, 2288, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2432
        wall.center_y = 1024
        self.wall_list.append(wall)

        for x in range(2576, 2704, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2848
        wall.center_y = 1024
        self.wall_list.append(wall)

        # --- Walls in the eighth row ---
        for x in range(86, 534, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 500
        wall.center_y = 1100
        self.wall_list.append(wall)

        for x in range(678, 870, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        for x in range(1094, 1286, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        for x in range(1590, 1718, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1862
        wall.center_y = 1168
        self.wall_list.append(wall)

        for x in range(2006, 2326, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 2250
        wall.center_y = 1090
        self.wall_list.append(wall)

        for x in range(2550, 2678, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1168
            self.wall_list.append(wall)

        # --- Walls in the ninth row ---
        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 176
        wall.center_y = 1312
        self.wall_list.append(wall)

        for x in range(320, 512, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1312
            self.wall_list.append(wall)

        for x in range(736, 992, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1312
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 1136
        wall.center_y = 1312
        self.wall_list.append(wall)

        for x in range(1360, 1808, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1312
            self.wall_list.append(wall)

        for x in range(2112, 2240, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1312
            self.wall_list.append(wall)

        for x in range(2384, 2640, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1312
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 2400
        wall.center_y = 1260
        self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2864
        wall.center_y = 1312
        self.wall_list.append(wall)

        # --- Walls in the tenth row ---
        for x in range(86, 214, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        for x in range(358, 550, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 774
        wall.center_y = 1451
        self.wall_list.append(wall)

        for x in range(918, 1238, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        wall = arcade.Sprite("rock.png", SPRITE_SCALING_BOX)
        wall.center_x = 1230
        wall.center_y = 1390
        self.wall_list.append(wall)

        for x in range(1542, 1990, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        for x in range(2134, 2326, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
        wall.center_x = 2470
        wall.center_y = 1451
        self.wall_list.append(wall)

        for x in range(2790, 2982, 64):
            wall = arcade.Sprite("lava.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1451
            self.wall_list.append(wall)

        # --- Creating walls around the edge ---

        # Placing the outer walls using loops
        for x in range(0, 3000, 100):
            wall = arcade.Sprite("tileOrange_25.png", SPRITE_SCALING_BOX)
            wall.bottom = 0
            wall.left = x + 25
            self.wall_list.append(wall)
        for x in range(0, 3000, 100):
            wall = arcade.Sprite("tileOrange_25.png", SPRITE_SCALING_BOX)
            wall.top = 1603
            wall.left = x + 25
            self.wall_list.append(wall)
        for y in range(0, 1500, 100):
            wall = arcade.Sprite("tileOrange_25.png", SPRITE_SCALING_BOX)
            wall.bottom = y + 75
            wall.left = 0
            wall.angle = 90
            self.wall_list.append(wall)
        for y in range(0, 1500, 100):
            wall = arcade.Sprite("tileOrange_25.png", SPRITE_SCALING_BOX)
            wall.bottom = y + 75
            wall.right = 3053
            wall.angle = 90
            self.wall_list.append(wall)

        # --- Creating coins ---

        # Creating that do not land on walls or other coins
        for i in range(COIN_COUNT):

            # Create the coin from the class
            coin = arcade.Sprite("tileGreen_05.png", SPRITE_SCALING_COIN)

            coin_successfully_placed = False
            while not coin_successfully_placed:

                # Place coin
                coin.center_x = random.randrange(50, 2951)
                coin.center_y = random.randrange(50, 1451)

                # Check to see if it hit a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # Check to see if it hit another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_successfully_placed = True

            self.coin_list.append(coin)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        arcade.draw_text(f"Score: " + str(self.score), self.view_left + 15, self.view_bottom + 15,
                         arcade.color.BRIGHT_GREEN, 20)
        arcade.draw_text(f"Emeralds remaining: " + str(COIN_COUNT - self.score), self.view_left + 15,
                         self.view_bottom + 40, arcade.color.BRIGHT_GREEN, 20)

    def update(self, delta_time):
        self.physics_engine.update()

        # Checking to see if the player hit a coin
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

        # --- Movement ---

        # If a key has been pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        if self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED

        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.S or key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.A or key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.D or key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()