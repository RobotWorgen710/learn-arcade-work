import arcade

WIDTH = 40
HEIGHT = 40
MARGIN = 10
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_HEIGHT = (HEIGHT * ROW_COUNT) + ((ROW_COUNT + 1) * MARGIN)
SCREEN_WIDTH = (WIDTH * COLUMN_COUNT) + ((COLUMN_COUNT + 1) * MARGIN)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.DARK_RED)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Draw a rectangle
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                arcade.draw_rectangle_filled((WIDTH / 2) + (column * (WIDTH + MARGIN)) + MARGIN, (HEIGHT / 2) + (row * (HEIGHT + MARGIN) + MARGIN), WIDTH, HEIGHT, arcade.color.GOLD)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()