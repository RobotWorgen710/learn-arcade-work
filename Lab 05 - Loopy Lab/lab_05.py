# Nested Loops

import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    """Print all white squares"""
    for row in range(30):
        for column in range(30):
            x = (column * 10) + 5  # Instead of zero, calculate the proper x location using 'column'
            y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    """White and black squares every other column"""
    for row in range(30):
        for column in range(30):
            if column % 2 == 0:
                x = (column * 10) + 305  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = (column * 10) + 305  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    """Black and white alternating rows"""
    for column in range(30):
        for row in range(30):
            if row % 2 == 0:
                x = (column * 10) + 605  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = (column * 10) + 605  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    """Black and White alternating rows and alternating Black and White on Even rows"""
    for column in range(30):
        for row in range(30):
            if row % 2 == 0 and column % 2 == 0:
                x = (column * 10) + 905  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                x = (column * 10) + 905  # Instead of zero, calculate the proper x location using 'column'
                y = (row * 10) + 5  # Instead of zero, calculate the proper y location using 'row'
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_5():
    """Triangle going to the middle"""
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for column in range(30):
        for row in range(30 - (column + 1)):
            x = 295 - (column * 10)   # Instead of zero, calculate the proper x location using 'column'
            y = (row * 10) + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    """Triangle going from the middle"""
    for column in range(30):
        for row in range(30 - column):
            x = (column * 10) + 305  # Instead of zero, calculate the proper x location using 'column'
            y = (row * 10) + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    """Upside down triangle getting smaller toward the center"""
    for column in range(30):
        for row in range(30 - column):
            x = 605 + (column * 10)
            y = 595 - (row * 10)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    """Upside down triangle getting smaller as it moves toward the middle"""
    for column in range(30):
        for row in range(30 - column):
            x = 1195 - (column * 10)
            y = 595 - (row * 10)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()