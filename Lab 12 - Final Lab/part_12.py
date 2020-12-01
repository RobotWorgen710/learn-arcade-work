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
VIEWPORT_MARGIN = 400
RIGHT_MARGIN = 400

TILE_SIZE = 128
SCALED_TILE_SIZE = TILE_SIZE * SPRITE_SCALING
MAP_HEIGHT = 7

# Physics
MOVEMENT_SPEED = 4
DEAD_ZONE = 0.2
JUMP_SPEED = 26
GRAVITY = 1.3

# Spawning Location
SPAWN_X = 224
SPAWN_Y = 224

# Animation constants
RIGHT_FACING = 0
LEFT_FACING = 1

LEVEL = 1
SCORE = 0


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

        controllers = arcade.get_game_controllers()
        if controllers:
            self.joystick = controllers[0]
            self.joystick.open()

            self.joystick.push_handlers(self)
        else:
            self.joystick = None

    def on_joybutton_press(self, joystick, button):
        print("Button")
        self.change_y = JUMP_SPEED

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

    def update(self):
        if self.joystick:
            self.change_x = self.joystick.x * MOVEMENT_SPEED
            if abs(self.change_x) < DEAD_ZONE:
                self.change_x = 0
        self.center_x += self.change_x


class InstructionView(arcade.View):

    def __init__(self):

        super().__init__()
        self.window.set_mouse_visible(True)
        self.score = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, arcade.color.WHITE, 50,
                         anchor_x="center")
        arcade.draw_text("Collect all the coins to advance to the next level", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("You lose lives when you hit spikes", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 300,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Each level will have new enemies", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 400,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Make it through all three levels to win", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 500,
                         arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("You will get 10 lives for each of the 3 levels", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 600, arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Keyboard: WASD or arrow keys to move and space bar to jump", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 700, arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Controller: Left stick to move and X or A to jump", SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 800, arcade.color.WHITE, 40, anchor_x="center")
        arcade.draw_text("Click to Play", SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 8) - 75, arcade.color.WHITE, 30,
                         anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView(self.score)
        game_view.setup(LEVEL)
        self.window.show_view(game_view)


class GameOverView(arcade.View):

    def __init__(self, score):

        super().__init__()
        self.score = score
        self.window.set_mouse_visible(True)

    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.RED, 70, anchor_x="center")
        arcade.draw_text("Click to Restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8, arcade.color.RED, 30,
                         anchor_x="center")
        arcade.draw_text(f"You score was {self.score}", SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 70,
                         arcade.color.RED, 50, anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView()
        self.window.show_view(game_view)


class GameWinView(arcade.View):

    def __init__(self):

        super().__init__()
        self.window.set_mouse_visible(True)

    def on_show(self):
        arcade.set_background_color([84, 2, 2])

    def on_draw(self):
        arcade.start_render()

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.draw_text("Congratulations", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.GOLD, 70, anchor_x="center")
        arcade.draw_text("You Win!", SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 100,
                         arcade.color.GOLD, 70, anchor_x="center")
        arcade.draw_text("Click to play again", SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 8), arcade.color.GOLD, 30,
                         anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = InstructionView()
        self.window.show_view(game_view)


class LevelCompletedView(arcade.View):

    def __init__(self, level, score):
        super().__init__()
        self.level = level + 1
        self.score = score
        self.window.set_mouse_visible(True)

    def on_show(self):
        arcade.set_background_color([84, 2, 2])

    def on_draw(self):
        arcade.start_render()

        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        arcade.draw_text(f"You completed level {self.level - 1}", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.GOLD
                         , 60, anchor_x="center")
        arcade.draw_text(f"Click to continue", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8, arcade.color.GOLD, 30,
                         anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        game_view = GameView(self.score)
        game_view.setup(self.level)
        self.window.show_view(game_view)


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self, score):
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
        self.moving_platform_list = None
        self.moving_enemies_list = None

        # Other
        self.score = None
        self.lives = None

        # Set up sounds
        self.coin_sound = None
        self.die_sound = None
        self.next_level_sound = None

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
        self.level = 1

        # Score
        self.score = score

    def setup(self, level):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.moving_platform_list = arcade.SpriteList()
        self.moving_enemies_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerCharacter()

        # Starting position of the player
        self.player_sprite.center_x = SPAWN_X
        self.player_sprite.center_y = SPAWN_Y
        self.player_list.append(self.player_sprite)

        # Setting up score and other constants
        self.lives = 10

        # Making mouse invisible
        self.window.set_mouse_visible(False)

        # Load in Sounds
        self.coin_sound = arcade.load_sound("coin1.wav")
        self.die_sound = arcade.load_sound("error4.wav")
        self.next_level_sound = arcade.load_sound("secret2.wav")

        # Get the level
        self.level = level

        # --- Load in the map ---
        map_name = f"Level{self.level}.tmx"

        # Different Layers
        platforms_layer = 'Platforms'
        enemies_layer = 'Enemies'
        coin_layer = 'Coins'
        moving_platform_layer = 'Moving Platforms'
        moving_enemies_layer = 'Moving Enemies'

        my_map = arcade.tilemap.read_tmx(map_name)

        # --- Layer Lists ---

        # Platforms layers
        self.wall_list = arcade.tilemap.process_layer(my_map, platforms_layer, PLATFORM_SCALING)
        self.moving_platform_list = arcade.tilemap.process_layer(my_map, moving_platform_layer, PLATFORM_SCALING)
        for block in self.moving_platform_list:
            self.wall_list.append(block)
            block.change_x = -3

        # Enemies layer
        self.enemies_list = arcade.tilemap.process_layer(my_map, enemies_layer, PLATFORM_SCALING)
        self.moving_enemies_list = arcade.tilemap.process_layer(my_map, moving_enemies_layer, PLATFORM_SCALING)
        for sprite in self.moving_enemies_list:
            self.enemies_list.append(sprite)
            sprite.change_x = -10

        # Coins layer
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

        arcade.draw_text(f"Score: {self.score}", self.view_left + 20, self.view_bottom + 60, arcade.color.BLUE, 24)
        arcade.draw_text(f"Lives: {self.lives}", self.view_left + 20, self.view_bottom + 30, arcade.color.BLUE, 24)

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

        self.wall_list.update()

        self.moving_enemies_list.update()

        # --- Player Movement and animation ---

        # Update Animation
        if self.physics_engine.can_jump():
            self.player_sprite.can_jump = False
        else:
            self.player_sprite.can_jump = True

        self.player_list.update_animation(delta_time)
        self.player_sprite.update()

        # Calculate movement based on which keys are pressed
        self.player_sprite.change_x = 0

        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        self.player_sprite.update()

        # See if the player moves on the the next level
        if len(self.coin_list) == 0:

            # Advance to the next level
            if self.level < 3:
                # Show a Level Complete Screen
                view = LevelCompletedView(self.level, self.score)
                self.window.show_view(view)
            else:
                view = GameWinView()
                self.window.show_view(view)

        for wall in self.moving_platform_list:

            if self.moving_platform_list[0].left < 768:
                for sprite in self.moving_platform_list:
                    sprite.change_x *= -1

            if self.moving_platform_list[2].right > 2496:
                for sprite in self.moving_platform_list:
                    sprite.change_x *= -1

        for enemy in self.moving_enemies_list:

            if enemy.left < 128:
                enemy.change_x *= -1

            if enemy.right > 896:
                enemy.change_x *= -1

        # Track if we need to change the view port

        changed = False

        # --- Checking if we hit a coin or spike
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)

        enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemies_list)
        for enemy in enemies_hit_list:
            self.player_sprite.center_x = SPAWN_X
            self.player_sprite.center_y = SPAWN_Y
            self.lives -= 1
            arcade.play_sound(self.die_sound)
            break

        if self.lives < 1:
            view = GameOverView(self.score)
            self.window.show_view(view)

        # --- Manage Scrolling ---

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


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    main()
