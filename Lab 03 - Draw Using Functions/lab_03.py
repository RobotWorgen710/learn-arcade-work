# Drawing using functions
import arcade
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800


def draw_sun():
    """Drawing the gas ball of death that powers our world"""
    arcade.draw_circle_filled(1500, 700, 60, arcade.csscolor.YELLOW)


def draw_clouds(x, y):
    """Drawing the fluffy white pillows in the sky"""
    arcade.draw_ellipse_filled(x, y, 150, 80, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 35, y + 30, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 15, y + 30, 40, arcade.csscolor.WHITE)


def draw_ground():
    """Drawing the grass"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 400, 0, arcade.csscolor.GREEN)


def draw_road(bottom, top):
    """Drawing the road and the lines on the road"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, top, bottom, arcade.csscolor.GREY)
    x = 15
    for i in range(23):
        arcade.draw_lrtb_rectangle_filled(x, x + 30, top - 45, bottom + 45, arcade.csscolor.YELLOW)
        x += 70


def draw_left_facing_car(x, y, color):
    """Drawing the cars on the road"""
    # Drawing Tires
    arcade.draw_circle_filled(x - 90, y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 90, y, 20, arcade.csscolor.BLACK)

    # Wheels of the car
    arcade.draw_circle_filled(x - 90, y, 10, arcade.csscolor.LIGHT_SLATE_GREY)
    arcade.draw_circle_filled(x + 90, y, 10, arcade.csscolor.LIGHT_SLATE_GREY)

    # Cabin of the car
    arcade.draw_lrtb_rectangle_filled(x - 65, x + 65, y + 40, y, color)
    arcade.draw_polygon_filled((
        (x - 65, y + 40),  # Bottom left
        (x + 65, y + 40),  # bottom right
        (x + 45, y + 70),  # top  right
        (x - 45, y + 70),  # top left
    ),
        color)
    arcade.draw_line(x - 64, y, x - 64, y + 40, arcade.csscolor.BLACK)
    arcade.draw_line(x + 64, y, x + 64, y + 40, arcade.csscolor.BLACK)
    arcade.draw_line(x, y, x, y + 70, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x - 20, x - 10, y + 35, y + 30, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x + 45, x + 55, y + 35, y + 30, arcade.csscolor.BLACK)

    # Front Fender
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 65, y + 40, y + 25, color)  # front
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 115, y + 25, y, color)
    arcade.draw_polygon_filled((
        (x - 115, y + 25),
        (x - 115, y),
        (x - 114, y),  # +- 1 x pixels. Same y
        (x - 107, y + 15),  # +- 7 x pixels. Up 15 pixels
        (x - 90, y + 23),  # +- 17 x pixels. Up 8 pixels
        (x - 90, y + 25),  # Bring it up to the rest of the fender
    ),
        color)
    arcade.draw_polygon_filled((
        (x - 65, y + 25),
        (x - 65, y),
        (x - 66, y),
        (x - 73, y + 15),
        (x - 90, y + 23),
        (x - 90, y + 25),
    ),
        color)
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 120, y + 30, y + 20, arcade.csscolor.YELLOW)

    # Rear Fender
    arcade.draw_lrtb_rectangle_filled(x + 65, x + 130, y + 40, y + 25, color)
    arcade.draw_lrtb_rectangle_filled(x + 115, x + 130, y + 25, y, color)
    arcade.draw_polygon_filled((
        (x + 65, y + 25),
        (x + 65, y),
        (x + 66, y),
        (x + 73, y + 15),
        (x + 90, y + 23),
        (x + 90, y + 25),
    ),
        color)
    arcade.draw_polygon_filled((
        (x + 115, y + 25),
        (x + 115, y),
        (x + 114, y),
        (x + 107, y + 15),
        (x + 90, y + 23),
        (x + 90, y + 25),
    ),
        color)
    arcade.draw_lrtb_rectangle_filled(x + 120, x + 130, y + 30, y + 20, arcade.csscolor.DARK_RED)

    # Left Window
    arcade.draw_polygon_filled((
        (x - 65, y + 40),  # bottom left
        (x - 10, y + 40),  # bottom right
        (x - 10, y + 65),  # top right
        (x - 48, y + 65),  # top left
    ),
        arcade.csscolor.SKY_BLUE)

    # Right Window
    arcade.draw_polygon_filled((
        (x + 5, y + 40),  # bottom left
        (x + 56, y + 40),  # bottom right
        (x + 40, y + 65),  # Top Right
        (x + 5, y + 65),  # top left
    ),
        arcade.csscolor.SKY_BLUE)


def draw_right_facing_car(x, y, color):
    """Drawing the cars on the road"""
    # Drawing Tires
    arcade.draw_circle_filled(x - 90, y, 20, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 90, y, 20, arcade.csscolor.BLACK)

    # Wheels of the car
    arcade.draw_circle_filled(x - 90, y, 10, arcade.csscolor.LIGHT_SLATE_GREY)
    arcade.draw_circle_filled(x + 90, y, 10, arcade.csscolor.LIGHT_SLATE_GREY)

    # Cabin of the car
    arcade.draw_lrtb_rectangle_filled(x - 65, x + 65, y + 40, y, color)
    arcade.draw_polygon_filled((
        (x - 65, y + 40),  # Bottom left
        (x + 65, y + 40),  # bottom right
        (x + 45, y + 70),  # top  right
        (x - 45, y + 70),  # top left
    ),
        color)
    arcade.draw_line(x - 64, y, x - 64, y + 40, arcade.csscolor.BLACK)
    arcade.draw_line(x + 64, y, x + 64, y + 40, arcade.csscolor.BLACK)
    arcade.draw_line(x, y, x, y + 70, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x - 55, x - 45, y + 35, y + 30, arcade.csscolor.BLACK)  # Back
    arcade.draw_lrtb_rectangle_filled(x + 10, x + 20, y + 35, y + 30, arcade.csscolor.BLACK)  # Front

    # Front Fender
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 65, y + 40, y + 25, color)  # front
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 115, y + 25, y, color)
    arcade.draw_polygon_filled((
        (x - 115, y + 25),
        (x - 115, y),
        (x - 114, y),  # +- 1 x pixels. Same y
        (x - 107, y + 15),  # +- 7 x pixels. Up 15 pixels
        (x - 90, y + 23),  # +- 17 x pixels. Up 8 pixels
        (x - 90, y + 25),  # Bring it up to the rest of the fender
    ),
        color)
    arcade.draw_polygon_filled((
        (x - 65, y + 25),
        (x - 65, y),
        (x - 66, y),
        (x - 73, y + 15),
        (x - 90, y + 23),
        (x - 90, y + 25),
    ),
        color)
    arcade.draw_lrtb_rectangle_filled(x - 130, x - 120, y + 30, y + 20, arcade.csscolor.DARK_RED)

    # Rear Fender
    arcade.draw_lrtb_rectangle_filled(x + 65, x + 130, y + 40, y + 25, color)
    arcade.draw_lrtb_rectangle_filled(x + 115, x + 130, y + 25, y, color)
    arcade.draw_polygon_filled((
        (x + 65, y + 25),
        (x + 65, y),
        (x + 66, y),
        (x + 73, y + 15),
        (x + 90, y + 23),
        (x + 90, y + 25),
    ),
        color)
    arcade.draw_polygon_filled((
        (x + 115, y + 25),
        (x + 115, y),
        (x + 114, y),
        (x + 107, y + 15),
        (x + 90, y + 23),
        (x + 90, y + 25),
    ),
        color)
    arcade.draw_lrtb_rectangle_filled(x + 120, x + 130, y + 30, y + 20, arcade.csscolor.YELLOW)

    # Left Window
    arcade.draw_polygon_filled((
        (x - 57, y + 40),  # bottom left
        (x - 10, y + 40),  # bottom right
        (x - 10, y + 65),  # top right
        (x - 41, y + 65),  # top left
    ),
        arcade.csscolor.SKY_BLUE)

    # Right Window
    arcade.draw_polygon_filled((
        (x + 5, y + 40),  # bottom left
        (x + 65, y + 40),  # bottom right
        (x + 49, y + 65),  # Top Right
        (x + 5, y + 65),  # top left
    ),
        arcade.csscolor.SKY_BLUE)


def draw_hill(x, y, width, height):
    """Drawing the hills in the background"""
    arcade.draw_ellipse_filled(x, y, width, height, arcade.csscolor.GREEN)


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Busy highway")

arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

arcade.start_render()


if __name__ == '__main__':
    draw_ground()
    draw_hill(200, 350, 600, 200)
    draw_hill(350, 350, 400, 300)
    draw_hill(600, 300, 600, 350)
    draw_hill(1200, 325, 1000, 250)
    draw_sun()
    draw_clouds(400, 700)
    draw_clouds(150, 725)
    draw_clouds(875, 690)
    draw_clouds(1330, 740)
    draw_clouds(1200, 600)
    draw_road(100, 200)
    draw_road(250, 350)
    draw_left_facing_car(200, 335, arcade.csscolor.DARK_GREEN)  # Back Lane first of each road
    draw_left_facing_car(900, 335, arcade.csscolor.DARK_RED)
    draw_left_facing_car(1350, 335, arcade.csscolor.GHOST_WHITE)
    draw_left_facing_car(1030, 275, arcade.csscolor.BLUE)
    draw_left_facing_car(700, 275, arcade.csscolor.DARK_GREY)
    draw_left_facing_car(30, 275, arcade.csscolor.RED)
    draw_right_facing_car(200, 180, arcade.csscolor.DARK_MAGENTA)
    draw_right_facing_car(1250, 180, arcade.csscolor.SIENNA)
    draw_right_facing_car(1550, 180, arcade.csscolor.CRIMSON)
    draw_right_facing_car(1325, 125, arcade.csscolor.CYAN)
    draw_right_facing_car(350, 125, arcade.csscolor.BLUE)
    draw_right_facing_car(800, 180, arcade.csscolor.GOLD)


arcade.finish_render()

arcade.run()
