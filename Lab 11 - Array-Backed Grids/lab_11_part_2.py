import arcade

WIDTH = 40
HEIGHT = 40
MARGIN = 10
ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_HEIGHT = (HEIGHT * ROW_COUNT) + ((ROW_COUNT + 1) * MARGIN)
SCREEN_WIDTH = (WIDTH * COLUMN_COUNT) + ((COLUMN_COUNT + 1) * MARGIN)
number_cells_selected = 0


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

        if self.grid[grid_y][grid_x] == 0:
            self.grid[grid_y][grid_x] = 1
        else:
            self.grid[grid_y][grid_x] = 0

        number_cells_selected = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    number_cells_selected += 1
        print("Total of " + str(number_cells_selected) + " cells are selected.")

        for row in range(ROW_COUNT):
            number_row_cells_selected = 0
            continuous_count = 0

            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    number_row_cells_selected += 1
                    continuous_count += 1
                if self.grid[row][column] == 0:
                    if continuous_count > 2:
                        print("Row " + str(row) + " has " + str(continuous_count) + " continuous blocks selected.")
                    continuous_count = 0
            print("Row " + str(row) + " has " + str(number_row_cells_selected) + " cells selected.")

        for column in range(COLUMN_COUNT):
            number_column_cells_selected = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    number_column_cells_selected += 1
            print("Column " + str(column) + " has " + str(number_column_cells_selected) + " cells selected.")
        print("")


def main():

   window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
   arcade.run()


if __name__ == "__main__":
   main()


