"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
from arcade import color

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# (The drawing code will go here.)

# Get ready to draw
arcade.start_render()

#draw a Rectangle
#left of 0, right of 599,
#top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_GREEN)

#tree trunk
#center of 100, 320
#width of 20
#height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#tree top
arcade.draw_circle_filled(100,350,30, arcade.csscolor.SEA_GREEN)

#another tree
arcade.draw_rectangle_filled(200,320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60 ,80, arcade.csscolor.SEA_GREEN)

#tree with arc for top
#Arc is centered at (300, 340) with width of 60 and hieght of 100
#starting angle is 0, ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.SEA_GREEN, 0, 180)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.SEA_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.SEA_GREEN)

                           # Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
# Specify start and end points
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

#drawing text
#specify coordinates, color and font size
arcade.draw_text("Good day to you", 
150, 230, arcade.color.BLACK, 24)

#specify parameters by name
#Polygon
arcade.draw_arc_outline(center_x=300,
                        center_y=340,
                        width=60,
                        height=100,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=45)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()