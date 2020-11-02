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

        arcade.set_background_color(arcade.color.WHITE)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        for row in self.grid:
            print(row)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Draw a rectangle
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 0:
                    color = arcade.color.BLACK
                else:
                    color = arcade.color.DARK_MAGENTA

                arcade.draw_rectangle_filled((WIDTH / 2) + (column * (WIDTH + MARGIN)) + MARGIN, (HEIGHT / 2) +
                                            (row * (HEIGHT + MARGIN) + MARGIN), WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        grid_x = x // (WIDTH + MARGIN)
        grid_y = y // (HEIGHT + MARGIN)
        print(grid_x, grid_y)

        if self.grid[grid_y][grid_x] == 0:
            self.grid[grid_y][grid_x] = 1

            if grid_y - 1 > - 1 and self.grid[grid_y - 1][grid_x] == 0:
                self.grid[grid_y - 1][grid_x] = 1
            elif grid_y - 1 > - 1 and self.grid[grid_y - 1][grid_x] == 1:
                self.grid[grid_y - 1][grid_x] = 0

            if (grid_y + 1) < 10 and self.grid[grid_y + 1][grid_x] == 0:
                self.grid[grid_y + 1][grid_x] = 1
            elif (grid_y + 1) < 10 and self.grid[grid_y + 1][grid_x] == 1:
                self.grid[grid_y + 1][grid_x] = 0

            if  (grid_x + 1) < 10 and self.grid[grid_y][grid_x + 1] == 0:
                self.grid[grid_y][grid_x + 1] = 1
            elif (grid_x + 1) < 10 and self.grid[grid_y][grid_x + 1] == 1:
                self.grid[grid_y][grid_x + 1] = 0

            if grid_x - 1 > - 1 and self.grid[grid_y][grid_x - 1] == 0:
                self.grid[grid_y][grid_x - 1] = 1
            elif grid_x - 1 > - 1 and self.grid[grid_y][grid_x - 1] == 1:
                self.grid[grid_y][grid_x - 1] = 0

        elif self.grid[grid_y][grid_x] == 1:
            self.grid[grid_y][grid_x] = 0

            if self.grid[grid_y - 1][grid_x] == 0 and grid_y - 1 > - 1:
                self.grid[grid_y - 1][grid_x] = 1
            elif self.grid[grid_y - 1][grid_x] == 1 and grid_y - 1 > - 1:
                self.grid[grid_y - 1][grid_x] = 0

            if (grid_y + 1) < 10 and self.grid[grid_y + 1][grid_x] == 0:
                self.grid[grid_y + 1][grid_x] = 1
            elif (grid_y + 1) < 10 and self.grid[grid_y + 1][grid_x] == 1:
                self.grid[grid_y + 1][grid_x] = 0

            if  (grid_x + 1) < 10 and self.grid[grid_y][grid_x + 1] == 0:
                self.grid[grid_y][grid_x + 1] = 1
            elif (grid_x + 1) < 10 and self.grid[grid_y][grid_x + 1] == 1:
                self.grid[grid_y][grid_x + 1] = 0

            if self.grid[grid_y][grid_x - 1] == 0 and grid_x - 1 > - 1:
                self.grid[grid_y][grid_x - 1] = 1
            elif self.grid[grid_y][grid_x - 1] == 1 and grid_x - 1 > - 1:
                self.grid[grid_y][grid_x - 1] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()


