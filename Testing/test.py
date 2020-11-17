"""
Final Project for Intro to Programming

Artwork from: http://kenney.nl
Tiled available from: http://www.mapeditor.org/
"""
import arcade

SPRITE_SCALING = 1
PLATFORM_SCALING = 0.5

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 300
RIGHT_MARGIN = 300

TILE_SIZE = 128
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING
MAP_HEIGHT = 7

# Physics
MOVEMENT_SPEED = 6
JUMP_SPEED = 16
GRAVITY = .95

# Spawning Location
SPAWN_X = 224
SPAWN_Y = 224

# Animation constants
RIGHT_FACING = 0
LEFT_FACING = 1

LEVEL = 1


def load_texture_pair(filename):
    """ Load both directions of a image"""
    return [
    arcade.load_texture(filename),
    arcade.load_texture(filename, flipped_horizontally=True)
    ]


class PlayerCharacter(arcade.Sprite):
    """ Player Sprite"""
    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default Facing
        self.character_face_direction = RIGHT_FACING

        # Flipping between image sequences
        self.cur_texture = 0
        self.scale = SPRITE_SCALING

        # Track current state
        self.jumping = False

        # Load in the textures for idle standing
        self.idle_texture_pair = load_texture_pair("player_stand.png")
        self.jump_texture_pair = load_texture_pair("player_jump.png")

        # Textures for walking
        self.walk_textures = []
        for i in range(2):
            texture = load_texture_pair(f"player_walk{i + 1}.png")
            self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box
        self.set_hit_box(self.texture.hit_box_points)

    def update_animation(self, delta_time: float = 1/60):

        # Calculate if we need to face right or left
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        if self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Jumping Animation
        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return

        # Idle Animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        # Walking Animation
        self.cur_texture += 1
        if self.cur_texture > 1:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.character_face_direction]


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLUE)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, arcade.color.WHITE, 50, anchor_x="center")
        arcade.draw_text("Collect all the coins to advance to the next level", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("You lose lives when you hit spikes", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 300,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Click to Play", SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 8), arcade.color.WHITE, 30, anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup(LEVEL)
        self.window.show_view(game_view)


class GameOverView(arcade.View):

    def __init__(self, score):

        super().__init__()
        self.score = score
        self.window.set_mouse_visible(True)

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED, 70, anchor_x="center")
        arcade.draw_text("Click to Restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8, arcade.color.RED, 30, anchor_x="center")
        arcade.draw_text("You score was " + str(self.score), SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 70,
                         arcade.color.RED, 50, anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup(LEVEL)
        self.window.show_view(game_view)


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        # Call the parent class
        super().__init__()

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.enemies_list = None
        self.coin_list = None
        self.score = None

        # Set up the player
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

        # Used for scrolling map
        self.view_left = 0
        self.view_bottom = 0

        # Track what keys are pressed
        self.left_pressed = False
        self.right_pressed = False

        # Level
        self.level = 2

    def setup(self, level):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerCharacter()

        # Starting position of the player
        self.player_sprite.center_x = SPAWN_X
        self.player_sprite.center_y = SPAWN_Y
        self.player_list.append(self.player_sprite)

        # Setting up score and other constants
        self.score = 0
        self.lives = 5

        # Making mouse invisible
        self.window.set_mouse_visible(False)

        # Load in Sounds
        self.coin_sound = arcade.load_sound("coin1.wav")
        self.die_sound = arcade.load_sound("error4.wav")
        self.next_level_sound = arcade.load_sound("secret2.wav")

        # --- Load in the map ---
        map_name = f"Level{self.level}.tmx"

        # Different Layers
        platforms_layer = 'Platforms'
        enemies_layer = 'Enemies'
        coin_layer = 'Coins'

        my_map = arcade.tilemap.read_tmx(map_name)

        # --- Layer Lists ---
        self.wall_list = arcade.tilemap.process_layer(my_map, platforms_layer, PLATFORM_SCALING)

        self.enemies_list = arcade.tilemap.process_layer(my_map, enemies_layer, PLATFORM_SCALING)

        self.coin_list = arcade.tilemap.process_layer(my_map, coin_layer, PLATFORM_SCALING)

        # Create out platformer physics engine with gravity
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Set the view port boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()
        self.enemies_list.draw()

        arcade.draw_text("Score: " + str(self.score), self.view_left + 20, self.view_bottom + 60, arcade.color.BLUE, 24)
        arcade.draw_text("Lives: " + str(self.lives), self.view_left + 20, self.view_bottom + 30, arcade.color.BLUE, 24)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP or key == arcade.key.W:
            # This line below is new. It checks to make sure there is a platform underneath
            # the player. Because you can't jump if there isn't ground beneath your feet.

            if self.physics_engine.can_jump():

                self.player_sprite.change_y = JUMP_SPEED

        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False

    def update(self, delta_time):
        """ Movement and game logic """

        self.physics_engine.update()

        # Update Animation
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        self.player_list.update_animation(delta_time)

        # See if the player moves on the the next level
        if len(self.coin_list) == 0:

            # Advance to the next level
            self.level += 1

            # Load the next Level
            self.setup(self.level)

            # Set the camera to the start
            self.view_left = 0
            self.view_bottom = 0

        # --- Manage Scrolling ---

        # Track if we need to change the view port

        changed = False

        # Scroll left
        left_bndry = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # --- Checking if we hit a coin or spike
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)
            print(len(self.coin_list))

        enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemies_list)
        for enemy in enemies_hit_list:
            self.player_sprite.center_x = SPAWN_X
            self.player_sprite.center_y = SPAWN_Y
            self.lives -= 1
            arcade.play_sound(self.die_sound)
            break

        # Calculate movement based on which keys are pressed
        self.player_sprite.change_x = 0

        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        self.player_sprite.update()

        if self.lives < 1:
            view = GameOverView(self.score)
            self.window.show_view(view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


main()