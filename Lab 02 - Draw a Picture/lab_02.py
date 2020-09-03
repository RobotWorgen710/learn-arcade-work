import arcade

arcade.open_window(600, 600, "Computer Drawing")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# Drawing the Ground
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.DARK_GREEN)

# The Road on the Grass
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 100, arcade.csscolor.GRAY)

# Lines on the road
arcade.draw_lrtb_rectangle_filled(10, 40, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(70, 100, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(130, 160, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(190, 220, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(250, 280, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(310, 340, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(370, 400, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(430, 460, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(490, 520, 155, 145, arcade.csscolor.YELLOW)
arcade.draw_lrtb_rectangle_filled(550, 580, 155, 145, arcade.csscolor.YELLOW)

# Drawing Tires
arcade.draw_circle_filled(180, 180, 20, arcade.csscolor.BLACK)
arcade.draw_circle_filled(360, 180, 20, arcade.csscolor.BLACK)

# Wheels of the car
arcade.draw_circle_filled(180, 180, 10, arcade.csscolor.LIGHT_SLATE_GREY)
arcade.draw_circle_filled(360, 180, 10, arcade.csscolor.LIGHT_SLATE_GREY)

# Cabin of the car
arcade.draw_lrtb_rectangle_filled(205, 335, 220, 180, arcade.csscolor.RED)
arcade.draw_polygon_filled((
    (205, 220),  # Bottom left
    (335, 220),  # bottom right
    (315, 250),  # top  right
    (225, 250),  # top left
    ),
    arcade.csscolor.RED)
arcade.draw_line(206, 180, 206, 220, arcade.csscolor.BLACK)
arcade.draw_line(334, 180, 334, 220, arcade.csscolor.BLACK)
arcade.draw_line(267, 180, 267, 250, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(250, 260, 215, 210, arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(315, 325, 215, 210, arcade.csscolor.BLACK)

# Front Fender
arcade.draw_lrtb_rectangle_filled(140, 205, 220, 205, arcade.csscolor.RED)  # front
arcade.draw_lrtb_rectangle_filled(140, 155, 205, 180, arcade.csscolor.RED)
arcade.draw_polygon_filled((
    (155, 205),
    (155, 180),
    (156, 180),  # +- 1 x pixels. Same y
    (163, 195),  # +- 7 x pixels. Up 15 pixels
    (180, 203),  # +- 17 x pixels. Up 8 pixels
    (180, 205),  # Bring it up to the rest of the fender
    ),
    arcade.csscolor.RED)
arcade.draw_polygon_filled((
    (205, 205),
    (205, 180),
    (204, 180),
    (197, 195),
    (180, 203),
    (180, 205),
    ),
    arcade.csscolor.RED)
arcade.draw_lrtb_rectangle_filled(140, 150, 210, 200, arcade.csscolor.YELLOW)

# Rear Fender
arcade.draw_lrtb_rectangle_filled(335, 400, 220, 205, arcade.csscolor.RED)
arcade.draw_lrtb_rectangle_filled(385, 400, 205, 180, arcade.csscolor.RED)
arcade.draw_polygon_filled((
    (335, 205),
    (335, 180),
    (336, 180),
    (343, 195),
    (360, 203),
    (360, 205),
    ),
    arcade.csscolor.RED)
arcade.draw_polygon_filled((
    (385, 205),
    (385, 180),
    (384, 180),
    (377, 195),
    (360, 203),
    (360, 205),
    ),
    arcade.csscolor.RED)
arcade.draw_lrtb_rectangle_filled(390, 400, 210, 200, arcade.csscolor.DARK_RED)

# Left Window
arcade.draw_polygon_filled((
    (205, 220),  # bottom left
    (260, 220),  # bottom right
    (260, 245),  # top right
    (222, 245),  # top left
    ),
    arcade.csscolor.SKY_BLUE)

# Right Window
arcade.draw_polygon_filled((
    (275, 220),  # bottom left
    (326, 220),  # bottom right
    (310, 245),  # Top Right
    (275, 245),  # top left
    ),
    arcade.csscolor.SKY_BLUE)

# Mountains
arcade.draw_triangle_filled(0, 300, 300, 300, 175, 475, arcade.csscolor.GREY)
arcade.draw_triangle_filled(200, 300, 500, 300, 375, 500, arcade.csscolor.GREY)
arcade.draw_polygon_filled((
    (175, 475),
    (135, 435),
    (163, 425),
    (170, 435),
    (190, 420),
    (205, 435),
    ),
    arcade.csscolor.WHITE)
arcade.draw_polygon_filled((
    (375, 500),
    (330, 450),
    (340, 450),
    (350, 440),
    (370, 450),
    (380, 450),
    (400, 435),
    (408, 450),
    ),
    arcade.csscolor.WHITE)

# Hill
arcade.draw_ellipse_filled(500, 280, 400, 120, arcade.csscolor.DARK_GREEN)

# Sun
arcade.draw_circle_filled(540, 540, 50, arcade.csscolor.YELLOW)

# Apple Tree
arcade.draw_lrtb_rectangle_filled(540, 560, 370, 320, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(550, 395, 40, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(530, 400, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(570, 390, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(535, 370, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(540, 420, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(550, 390, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(569, 405, 5, arcade.csscolor.RED)
arcade.draw_circle_filled(555, 375, 5, arcade.csscolor.RED)


arcade.finish_render()

arcade.run()