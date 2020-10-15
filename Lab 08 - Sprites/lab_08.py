# Sprites game

import arcade
import random

CHARACTER_SCALING = 2
COIN_SCALING = 0.25
ALIEN_SCALING = 0.25

COIN_COUNT = 50
ALIEN_COUNT = 50

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800


class Coin(arcade.Sprite):
   """Creating the coins"""

   def __init__(self, filename, sprite_scaling):

       super().__init__(filename, sprite_scaling)

       """Initializing change x and change y"""
       self.change_x = 0
       self.change_y = 0

   def update(self):

       # Moving the coin
       self.center_x += self.change_x
       self.center_y += self.change_y

       # Making the coins bounce off the side
       if self.right > SCREEN_WIDTH and self.change_x > 0:
           """Right Edge"""
           self.change_x *= -1

       if self.left < 0 and self.change_x < 0:
           """Left Edge"""
           self.change_x *= -1

       if self.top > SCREEN_HEIGHT and self.change_y > 0:
           """Top Edge"""
           self.change_y *= -1

       if self.bottom < 0 and self.change_y < 0:
           """Bottom Edge"""
           self.change_y *= -1


class Alien(arcade.Sprite):
   """Creating the coins"""

   def __init__(self, filename, sprite_scaling):

       super().__init__(filename, sprite_scaling)

       """Initializing change x and change y"""
       self.change_x = 0
       self.change_y = 0

   def update(self):

       # Moving the coin
       self.center_y += self.change_y

       # Resetting to the top of the screen
       if self.top < 0:
           self.center_x = random.randrange(SCREEN_WIDTH)
           self.bottom = SCREEN_HEIGHT


class MyGame(arcade.Window):

   def __init__(self):

       """Setting up the window"""
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Adventure")

       """Setting up the sprite lists"""
       self.player_list = None
       self.coin_list = None
       self.alien_list = None

       """Setting up the player"""
       self.player_sprite = None
       self.score = 0

       """Making the mouse invisible"""
       self.set_mouse_visible(False)

       arcade.set_background_color(arcade.color.BLACK)

   def setup(self):

       """Set up the game and initialize the variables"""

       """Set up the sprite lists"""
       self.player_list = arcade.SpriteList()
       self.coin_list = arcade.SpriteList()
       self.alien_list = arcade.SpriteList()

       # Set up the score
       self.score = 0

       # Setting up the player character
       # Image from Iconsdb
       self.player_sprite = arcade.Sprite("rocket-16.png", CHARACTER_SCALING)
       self.player_sprite.center_x = SCREEN_WIDTH/2
       self.player_sprite.center_y = SCREEN_HEIGHT/2
       self.player_list.append(self.player_sprite)

       # Creating coin
       for i in range(COIN_COUNT):

           # Setting up the coins
           # Image from Kenny.nl
           coin = Coin("coin_40.png", COIN_SCALING)

           # Position of the coins
           coin.center_x = random.randrange(SCREEN_WIDTH)
           coin.center_y = random.randrange(SCREEN_HEIGHT)
           coin.change_x = random.randrange(-3, 4)
           coin.change_y = random.randrange(-3, 4)

           # Adding coins to the list
           self.coin_list.append(coin)

       for i in range(ALIEN_COUNT):

           # Image from freepnglogos
           alien = Alien("ufo-26833.png", ALIEN_SCALING)

           # Positions of the aliens
           alien.center_x = random.randrange(SCREEN_WIDTH)
           alien.center_y = random.randrange(SCREEN_HEIGHT)
           alien.change_y = random.randrange(-3, 0)

           # Adding aliens to the list
           self.alien_list.append(alien)

       arcade.set_background_color(arcade.color.BLACK)

   def on_draw(self):

       """Draw all sprites coins and aliens"""

       # Starting the render
       arcade.start_render()

       # Draw all the sprites
       self.alien_list.draw()
       self.coin_list.draw()
       self.player_sprite.draw()

       # Showing the score at the bottom
       arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.RED, 24)

       if not self.coin_list:
           arcade.draw_text("Game Over", (SCREEN_WIDTH / 2) - 120, (SCREEN_HEIGHT / 2) - 20, arcade.color.RED, 40)

   def on_mouse_motion(self, x, y, dx, dy):
       if self.coin_list:
           self.player_sprite.center_x = x
           self.player_sprite.center_y = y

   def update(self, delta_time):
       """Update all the sprites and variables"""

       # Updating all the sprites
       if self.coin_list:
           self.player_list.update()
           self.coin_list.update()
           self.alien_list.update()

       for alien in self.alien_list:
           """Checking to see if the player hit an alien"""

           bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.alien_list)
           for item in bad_hit_list:
               item.remove_from_sprite_lists()
               self.score -= 1

       # Check for hitting coins
       for coin in self.coin_list:
           """Checking to see if the player hit a coin"""

           good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
           for item in good_hit_list:
               item.remove_from_sprite_lists()
               self.score += 1


def main():
   window = MyGame()
   window.setup()
   arcade.run()

if __name__ == '__main__':
   main()





