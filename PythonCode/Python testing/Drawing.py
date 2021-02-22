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
arcade.set_background_color(arcade.csscolor.MEDIUM_TURQUOISE)

# Get ready to draw
arcade.start_render()

#draw a Rectangle
#left of 0, right of 599,
#top of 599, bottom of 350
arcade.draw_lrtb_rectangle_filled(0, 599, 599, 350, arcade.csscolor.LIGHT_PINK)

#the sun
arcade.draw_arc_filled(300, 350, 500, 500, arcade.csscolor.KHAKI, 0, 180)

#Boat
arcade.draw_arc_filled(250, 250, 155, 60, arcade.csscolor.DARK_RED, 180, 360)
arcade.draw_rectangle_filled(253, 300, 6, 100, arcade.csscolor.BLACK)
arcade.draw_triangle_filled(250,250,180,250,250,350, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(255,250,320,250,255,350, arcade.csscolor.WHITE)

#drawing text
#('THE SS BOAT')
arcade.draw_text("THE SS BOAT", 
200, 230, arcade.color.GHOST_WHITE, 9)

#right hand land mass
arcade.draw_rectangle_filled(500,100,80,300, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(599,120,270,290, arcade.csscolor.GREEN, 90, 270)
arcade.draw_arc_filled(599,250,280,180, arcade.csscolor.GREEN, 90, 270)

#lines on side of landmass
arcade.draw_line(460,236,460,0, arcade.csscolor.BLACK, 4)

#picnic blanket
arcade.draw_lrtb_rectangle_filled(495,575,300,225, arcade.csscolor.RED)
#horizontal white lines
arcade.draw_line(495,250,575,250, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(495,225,575,225, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(495,275,575,275, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(495,300,575,300, arcade.csscolor.WHITE_SMOKE, 3)
#downwards white lines
arcade.draw_line(495,300,495,225, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(515,300,515,225, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(535,300,535,225, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(555,300,555,225, arcade.csscolor.WHITE_SMOKE, 3)
arcade.draw_line(575,300,575,225, arcade.csscolor.WHITE_SMOKE, 3)

#Bird 1
#specify parameters of an Arc by name
#Left wing
arcade.draw_arc_outline(center_x=515,
                        center_y=500,
                        width=40,
                        height=30,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=-15)
#Right wing
arcade.draw_arc_outline(center_x=555,
                        center_y=490,
                        width=40,
                        height=30,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=-15)

#Bird 2
#specify parameters of an Arc by name
#Left wing (bird 2)
arcade.draw_arc_outline(center_x=20,
                        center_y=500,
                        width=40,
                        height=30,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=12)
#Right wing (bird 2)
arcade.draw_arc_outline(center_x=60,
                        center_y=510,
                        width=40,
                        height=30,
                        color=arcade.csscolor.BLACK,
                        start_angle=0,
                        end_angle=180,
                        border_width=3,
                        tilt_angle=12)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()